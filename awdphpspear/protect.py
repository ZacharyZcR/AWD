"""File monitoring and restoration from a separate backup directory."""

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import tempfile
import time


def get_file_md5(filename):
    digest = hashlib.md5()
    with Path(filename).open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def file_md5_build(startpath):
    root = Path(startpath).resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)
    snapshot = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symbolic links are not supported: {path}")
        snapshot[path.relative_to(root)] = None if path.is_dir() else get_file_md5(path)
    return snapshot


def _paths(startpath, backup):
    root = Path(startpath).resolve()
    target = Path(backup).resolve() if backup else root.with_name(root.name + ".awd-backup")
    if root == target or root in target.parents or target in root.parents:
        raise ValueError("Source and backup directories must not overlap")
    return root, target


def file_backup(startpath=".", backup=None):
    root, target = _paths(startpath, backup)
    file_md5_build(root)
    shutil.copytree(root, target)
    return target


def _changes(baseline, current):
    added = current.keys() - baseline.keys()
    removed = baseline.keys() - current.keys()
    changed = {path for path in baseline.keys() & current.keys() if baseline[path] != current[path]}
    return added, removed, changed


def _copy_file(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=destination.parent)
    os.close(descriptor)
    try:
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        Path(temporary).unlink(missing_ok=True)


def _remove(path):
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def _restore(root, backup, baseline, current):
    added, removed, changed = _changes(baseline, current)
    for relative in sorted(added | changed, key=lambda path: len(path.parts), reverse=True):
        destination = root / relative
        if relative in added or baseline[relative] is None or current[relative] is None:
            _remove(destination)
    for relative in sorted(removed | changed, key=lambda path: (len(path.parts), path)):
        destination = root / relative
        if baseline[relative] is None:
            destination.mkdir(parents=True, exist_ok=True)
        else:
            _copy_file(backup / relative, destination)


def _monitor(startpath, backup, interval, restore):
    if interval <= 0:
        raise ValueError("Interval must be positive")
    root, target = _paths(startpath, backup)
    baseline = file_md5_build(target if restore else root)
    while True:
        current = file_md5_build(root)
        for label, paths in zip(("Added", "Removed", "Changed"), _changes(baseline, current)):
            for path in sorted(paths):
                print(f"{label}: {path}", flush=True)
        if restore:
            _restore(root, target, baseline, current)
        time.sleep(interval)


def file_md5_check(startpath=".", *, interval=5):
    _monitor(startpath, None, interval, restore=False)


def file_md5_defense(startpath=".", backup=None, *, interval=5):
    if interval <= 0:
        raise ValueError("Interval must be positive")
    root, target = _paths(startpath, backup)
    if not target.exists():
        file_backup(root, target)
    _monitor(root, target, interval, restore=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("backup", "check", "restore"))
    parser.add_argument("directory", type=Path)
    parser.add_argument("--backup", type=Path)
    parser.add_argument("--interval", type=float, default=5)
    args = parser.parse_args()
    try:
        if args.action == "backup":
            print(file_backup(args.directory, args.backup))
        elif args.action == "check":
            file_md5_check(args.directory, interval=args.interval)
        else:
            file_md5_defense(args.directory, args.backup, interval=args.interval)
    except KeyboardInterrupt:
        pass
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()

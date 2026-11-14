"""Small file helpers used by the original toolbox."""

from pathlib import Path


def read_array(target_file):
    return Path(target_file).read_text(encoding="utf-8").splitlines()


def read_var(target_file):
    with Path(target_file).open(encoding="utf-8") as stream:
        return stream.readline().rstrip("\r\n")


def write_txt(target_file, content):
    if content is None:
        return
    with Path(target_file).open("a", encoding="utf-8") as stream:
        stream.write(content + "\n")


def dir_tree(startpath):
    root = Path(startpath)
    print(root)
    for path in sorted(root.rglob("*")):
        depth = len(path.relative_to(root).parts)
        print("|---" * depth + path.name)


def get_php_list(startpath):
    return [str(path) for path in sorted(Path(startpath).rglob("*.php")) if path.is_file()]

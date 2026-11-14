from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import requests

from awdphpspear import files, protect, request


class FileTests(unittest.TestCase):
    def test_text_round_trip_and_empty_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.txt"
            files.write_txt(path, "父亲")
            files.write_txt(path, "second")
            files.write_txt(path, None)
            self.assertEqual(files.read_array(path), ["父亲", "second"])
            self.assertEqual(files.read_var(path), "父亲")
            path.write_text("")
            self.assertEqual(files.read_array(path), [])
            self.assertEqual(files.read_var(path), "")

    def test_missing_file_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                files.read_array(Path(directory) / "missing")


class RequestTests(unittest.TestCase):
    @patch("awdphpspear.request.requests.post")
    def test_json_encoding_and_timeout(self, post):
        payload = {"message": "hello"}
        self.assertIs(request.post_json("https://example.invalid", payload), post.return_value)
        post.assert_called_once_with("https://example.invalid", json=payload, timeout=10)
        post.return_value.raise_for_status.assert_called_once()

    @patch("awdphpspear.request.requests.get")
    def test_http_errors_propagate(self, get):
        get.return_value.raise_for_status.side_effect = requests.HTTPError("server error")
        with self.assertRaises(requests.HTTPError):
            request.get("https://example.invalid", timeout=2)
        get.assert_called_once_with("https://example.invalid", params=None, timeout=2)

    @patch("awdphpspear.request.requests.post")
    def test_form_encoding(self, post):
        request.post_xwf("https://example.invalid", {"key": "value"})
        post.assert_called_once_with("https://example.invalid", data={"key": "value"}, timeout=10)


class ProtectTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "site"
        self.backup = Path(temporary.name) / "backup"
        self.root.mkdir()
        (self.root / "changed.txt").write_text("original")
        (self.root / "deleted.php").write_text("original")
        (self.root / "empty").mkdir()
        (self.root / "nested").mkdir()
        (self.root / "nested" / "file").write_text("nested")
        protect.file_backup(self.root, self.backup)
        self.baseline = protect.file_md5_build(self.backup)

    def restore(self):
        protect._restore(self.root, self.backup, self.baseline, protect.file_md5_build(self.root))
        self.assertEqual(protect.file_md5_build(self.root), self.baseline)

    def test_restore_simultaneous_add_change_and_delete(self):
        (self.root / "changed.txt").write_text("modified")
        (self.root / "deleted.php").unlink()
        (self.root / "extra").mkdir()
        (self.root / "extra" / "file").write_text("new")
        (self.root / "empty").rmdir()
        self.restore()

    def test_restore_file_directory_type_changes(self):
        (self.root / "changed.txt").unlink()
        (self.root / "changed.txt").mkdir()
        (self.root / "changed.txt" / "child").write_text("new")
        (self.root / "empty").rmdir()
        (self.root / "empty").write_text("new")
        self.restore()

    def test_restore_deleted_directory_with_contents(self):
        shutil.rmtree(self.root / "nested")
        self.restore()

    def test_failed_copy_preserves_existing_file(self):
        path = self.root / "changed.txt"
        path.write_text("keep me")
        with patch.object(protect.shutil, "copy2", side_effect=OSError("copy failed")):
            with self.assertRaises(OSError):
                self.restore()
        self.assertEqual(path.read_text(), "keep me")
        self.assertFalse(any(path.name.startswith("tmp") for path in self.root.iterdir()))

    def test_backup_cannot_overlap_or_overwrite(self):
        for target in (self.root, self.root / "backup", self.root.parent):
            with self.subTest(target=target), self.assertRaises(ValueError):
                protect.file_backup(self.root, target)
        with self.assertRaises(FileExistsError):
            protect.file_backup(self.root, self.backup)

    def test_symlinks_are_reported(self):
        (self.root / "link").symlink_to(self.root / "changed.txt")
        with self.assertRaises(ValueError):
            protect.file_md5_build(self.root)

    def test_monitor_reports_changes_and_restores_without_sleeping(self):
        (self.root / "changed.txt").write_text("modified")
        (self.root / "deleted.php").unlink()
        with patch.object(protect.time, "sleep", side_effect=KeyboardInterrupt):
            with patch("builtins.print") as output, self.assertRaises(KeyboardInterrupt):
                protect.file_md5_defense(self.root, self.backup)
        messages = [call.args[0] for call in output.call_args_list]
        self.assertIn("Removed: deleted.php", messages)
        self.assertIn("Changed: changed.txt", messages)
        self.assertEqual(protect.file_md5_build(self.root), self.baseline)

    def test_invalid_interval_does_not_create_backup(self):
        with self.assertRaises(ValueError):
            protect.file_md5_check(self.root, interval=0)
        target = self.root.parent / "unused-backup"
        with self.assertRaises(ValueError):
            protect.file_md5_defense(self.root, target, interval=0)
        self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()

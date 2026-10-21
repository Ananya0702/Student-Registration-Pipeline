import unittest
from pathlib import Path

class StudentRegistrationTests(unittest.TestCase):

    def test_required_files_exist(self):
        for filename in ["index.html", "style.css", "script.js"]:
            with self.subTest(filename=filename):
                self.assertTrue(Path(filename).is_file())

    def test_registration_form_exists(self):
        html = Path("index.html").read_text(encoding="utf-8")
        self.assertIn('id="registrationForm"', html)

    def test_required_fields_exist(self):
        html = Path("index.html").read_text(encoding="utf-8")
        for field in ["name", "email", "roll", "course"]:
            with self.subTest(field=field):
                self.assertIn(f'id="{field}"', html)

    def test_javascript_validation_exists(self):
        js = Path("script.js").read_text(encoding="utf-8")
        self.assertIn("Registration successful", js)

if __name__ == "__main__":
    unittest.main(verbosity=2)

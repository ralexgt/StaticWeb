import unittest
from generatepage import extract_title

class TestMGenPage(unittest.TestCase):
  def test_extract_title(self):
    markdown = """
# Title
## Text text text
#### text
> texttext 
"""
    self.assertEqual(extract_title(markdown), "Title")
  def test_extract_no_title(self):
    markdown = """
### Title
## Text text text
#### text
> texttext 
"""
    try:
      extract_title(markdown)
      self.fail("should raise an error")
    except ValueError as e:
      return


if __name__ == "__main__":
    unittest.main()
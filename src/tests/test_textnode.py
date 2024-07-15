import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("Test 2", "bold", "https://github.com")
        node2 = TextNode("Test 2", "bold", "https://github.com")
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)
    def test_eq4(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
    def test_eq5(self):
        node = TextNode("", "italic", "https://google.com")
        node2 = TextNode("", "italic", "https://google.com")
        self.assertEqual(node, node2)

class TestTextToHTMLNode(unittest.TestCase):
  def test_raw_text(self):
    text_node = TextNode("This is a text node", text_type_text)
    self.assertEqual(text_node_to_html_node(text_node).__repr__(),
                     LeafNode(tag = None, value = "This is a text node").__repr__())
    
  def test_bold_text(self):
    text_node = TextNode("This is a bold node", text_type_bold)
    self.assertEqual(text_node_to_html_node(text_node).__repr__(),
                     LeafNode(tag = "b", value = "This is a bold node").__repr__())
    
  def test_link_text(self):
    text_node = TextNode("This is a link node", text_type_link, "google.com")
    self.assertEqual(text_node_to_html_node(text_node).__repr__(),
                     LeafNode(tag = "a", value = "This is a link node", props = {"href": "google.com"}).__repr__())
    
  def test_image_text(self):
    text_node = TextNode("This is an image node", text_type_image, "image.jpg")
    self.assertEqual(text_node_to_html_node(text_node).__repr__(),
                     LeafNode(tag = "img", value = "", props = {"src": "image.jpg", "alt": "This is an image node"}).__repr__())
    


if __name__ == "__main__":
    unittest.main()
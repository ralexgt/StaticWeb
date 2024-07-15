import unittest
from inline_markdown import (
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
  split_text_nodes_links,
  split_text_nodes_images,
  text_to_textnodes,
)

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_link,
  text_type_image,
)


class TestInlineMarkdown(unittest.TestCase):
  def test_delim_bold(self):
    node = TextNode("This is text with a **bolded** word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word", text_type_text),
      ],
      new_nodes,
    )

  def test_delim_bold_double(self):
    node = TextNode(
      "This is text with a **bolded** word and **another**", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word and ", text_type_text),
        TextNode("another", text_type_bold),
      ],
      new_nodes,
    )

  def test_delim_bold_multiword(self):
    node = TextNode(
      "This is text with a **bolded word** and **another**", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("bolded word", text_type_bold),
        TextNode(" and ", text_type_text),
        TextNode("another", text_type_bold),
      ],
      new_nodes,
    )

  def test_delim_italic(self):
    node = TextNode("This is text with an *italic* word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
    self.assertListEqual(
      [
        TextNode("This is text with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word", text_type_text),
      ],
      new_nodes,
    )

  def test_delim_bold_and_italic(self):
    node = TextNode("**bold** and *italic*", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    self.assertListEqual(
      [
        TextNode("bold", text_type_bold),
        TextNode(" and ", text_type_text),
        TextNode("italic", text_type_italic),
      ],
      new_nodes,
    )

  def test_delim_code(self):
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" word", text_type_text),
      ],
      new_nodes,
    )

class TestExtractImgsLinks(unittest.TestCase):
  def test_no_image(self):
    text = "This text has no image"
    self.assertListEqual(extract_markdown_images(text), [])
  def test_one_image(self):
    text = "This text has one ![image](image.jpg)"
    self.assertListEqual(extract_markdown_images(text), [("image", "image.jpg")])
  def test_more_image(self):
    text = "This text has more ![image1](image1.jpg) images like ![image3](image3.jpg) and ![image2](image2.jpg)"
    self.assertListEqual(extract_markdown_images(text), [("image1", "image1.jpg"), ("image3", "image3.jpg"), ("image2", "image2.jpg")])
  def test_no_links(self):
    text = "This text has no links"
    self.assertListEqual(extract_markdown_links(text), [])
  def test_one_image(self):
    text = "This text has one [link](link.url)"
    self.assertListEqual(extract_markdown_links(text), [("link", "link.url")])
  def test_more_links(self):
    text = "This text has more ![l1](http://l1) links like ![l2](http://l2) and ![l3](http://l3)"
    self.assertListEqual(extract_markdown_links(text), [("l1", "http://l1"), ("l2", "http://l2"), ("l3", "http://l3")])
  def test_link_image(self):
    text = "This is a link [link](http://link) and this is an image ![image](image.jpg)"
    self.assertListEqual(extract_markdown_images(text), [("image", "image.jpg")])
  def test_link_image_2(self):
    text = "This is a link [link](http://link) and this is an image ![image](image.jpg)"
    self.assertListEqual(extract_markdown_links(text), [("link", "http://link"), ("image", "image.jpg")])

class TestSplitNodes(unittest.TestCase):
  def test_split_image(self):
    node = TextNode(
      "This is text with an ![image](https://image.png)",
      text_type_text,
    )
    new_nodes = split_text_nodes_images([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", text_type_text),
        TextNode("image", text_type_image, "https://image.png"),
      ],
      new_nodes
    )

  def test_split_image_single(self):
    node = TextNode(
      "![image](https://image.png)",
      text_type_text,
    )
    new_nodes = split_text_nodes_images([node])
    self.assertListEqual(
      [
          TextNode("image", text_type_image, "https://image.png"),
      ],
      new_nodes
    )

  def test_split_images(self):
    node = TextNode(
      "This is text with an ![image](https://image.jpg) and another ![second image](https://image2.jpg)",
      text_type_text,
    )
    new_nodes = split_text_nodes_images([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", text_type_text),
        TextNode("image", text_type_image, "https://image.jpg"),
        TextNode(" and another ", text_type_text),
        TextNode(
            "second image", text_type_image, "https://image2.jpg"
        ),
      ],
      new_nodes
    )

  def test_split_links(self):
    node = TextNode(
      "This is text with a [link](https://google.com) and [another link](https://youtube.com) with text that follows",
      text_type_text,
    )
    new_nodes = split_text_nodes_links([node])
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("link", text_type_link, "https://google.com"),
        TextNode(" and ", text_type_text),
        TextNode("another link", text_type_link, "https://youtube.com"),
        TextNode(" with text that follows", text_type_text),
      ],
      new_nodes
    )

class TextToTextNodes(unittest.TestCase):
  def test_text_to_textnodes(self):
    nodes = text_to_textnodes(
      "This is **text** with an *italic* word and a `code block` and an ![image](https://image.png) and a [link](https://google.com)"
    )
    self.assertListEqual(
      [
        TextNode("This is ", text_type_text),
        TextNode("text", text_type_bold),
        TextNode(" with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word and a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" and an ", text_type_text),
        TextNode("image", text_type_image, "https://image.png"),
        TextNode(" and a ", text_type_text),
        TextNode("link", text_type_link, "https://google.com"),
      ],
      nodes,
    )

    
if __name__ == "__main__":
    unittest.main()

class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    result = ""
    if self.props:
      for item in self.props:
        result += f" {item}=\"{self.props[item]}\""
    return result
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props = None):
    super().__init__(tag = tag, value = value, props = props)
  
  def to_html(self):
    if not self.value:
      raise ValueError("No value")
    if not self.tag:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props = None):
    super().__init__(tag = tag, children = children, props = props)
  
  def to_html(self):
    if not self.tag:
      raise ValueError("No tag")
    if not self.children:
      raise ValueError("No children")
    children_html = ""
    for child in self.children:
        children_html += child.to_html()
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
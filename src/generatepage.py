import os
from block_markdown import markdown_to_html_node

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def is_md_html(file_path):
  file_name = file_path.split("/")[-1]
  if '.' in file_name:
    if file_name.split(".")[1] == "md" or file_name.split(".")[1] == "html":
      return True
  return False
def read_file(file_path):
  if not is_md_html(file_path):
    raise Exception("not a valid file")
  with open(file_path) as file:
    return file.read()
  
def write_file(file_path, content):
  with open(file_path) as file:
    file.write(content)

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  md_file = read_file(from_path)
  template_file = read_file(template_path)
  html = markdown_to_html_node(md_file).to_html()
  title = extract_title(md_file)
  template_file = template_file.replace("{{ Title }}", title)
  template_file = template_file.replace("{{ Content }}", html)
  
  # write the html file in dest_path
  dest_dir_path = os.path.dirname(dest_path)
  if dest_dir_path != "":
    os.makedirs(dest_dir_path, exist_ok=True)
  to_file = open(dest_path, "w")
  to_file.write(template_file)
  
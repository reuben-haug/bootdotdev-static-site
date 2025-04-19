# src/generate_page.py
import os
from .markdown_to_html_node import markdown_to_html_node
from .markdown_parser import extract_title

def generate_page(basepath: str, src_path: str, template_path: str, dest_path:str) -> None:
    '''
    Generates an HTML page from a Markdown file using a specified HTML template.

    This function reads a Markdown file, extracts its title and content, and integrates them into an HTML template. 
    The final HTML content is then written to the specified destination file.

    Args:
        src_path (str): The file path to the source Markdown file (e.g., "content/index.md").
        template_path (str): The file path to the HTML template file (e.g., "template.html").
        dest_path (str): The file path where the generated HTML file will be saved (e.g., "public/index.html").

    Returns:
        None
    '''
    print(f"Generating page from {src_path} to {dest_path} using {template_path}...")
    # /content/index.md
    with open(src_path, 'r') as src_file:
        markdown_content = src_file.read()

    # /template.html
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_content)
    final_content = final_content.replace('href="/', 'href="' + basepath)
    final_content = final_content.replace('src="/', 'src="' + basepath)

    # public/index.html
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_content)

def generate_pages_recursive(basepath: str, src_dir: str, template_path: str, dest_dir: str) -> None:
    '''
    For each markdown file found, generate a new .html file using the same template.html.  The generated pages should be written to the 'public' directory in the same directory structure.
    '''
    
    print(f"Searching source path for markdown files in {src_dir}...")

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.scandir(src_dir):
        src_item_path = os.path.join(src_dir, item.name)
        dest_item_path =  os.path.join(dest_dir, item.name)

        if item.is_file() and item.name.endswith(".md"):
            dest_html_path = os.path.splitext(dest_item_path)[0] + ".html"
            generate_page(basepath, src_item_path, template_path, dest_html_path)

        elif item.is_dir():
            generate_pages_recursive(basepath, src_item_path, template_path, dest_item_path)
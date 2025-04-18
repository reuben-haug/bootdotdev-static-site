# src/generate_page.py

from .markdown_to_html_node import markdown_to_html_node
from .markdown_parser import extract_title

def generate_page(src_path, template_path, dest_path):
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

    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # public/index.html
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_content)
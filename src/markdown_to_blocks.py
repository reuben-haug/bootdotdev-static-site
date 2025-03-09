# src/markdown_to_blocks.py

def markdown_to_blocks(md):
    """
    Takes a raw Markdown string and returns a list of block strings.
    """
    
    blocks = []
    lines = md.split("\n")
    current_block = []

    for line in lines:
        # If the line is empty (or just whitespace), it's a block separator
        # only if we already have content in the current block
        if line.strip() == "":
            if current_block:
                # Join the current block and add to blocks list
                blocks.append("\n".join(current_block))
                current_block = []
        else:
            # Strip leading whitespace from each line and add to current block
            current_block.append(line.lstrip())

    # Add the last block if there's any content
    if current_block:
        blocks.append("\n".join(current_block))

    return blocks
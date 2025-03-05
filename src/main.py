from textnode import TextNode, TextType

def main():
    testNode = TextNode("This is some text", TextType.TEXT)

    print(testNode.__repr__())
if __name__ == "__main__":
    main()
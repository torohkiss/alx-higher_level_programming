#!?usr/bin/python3
"""Function that prints 2 new lines"""

def text_indentation(text):
        """Prints a text with 2 new lines after each"""
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        for char in ".?:":
            text = text.replace(char, char + "\n\n")
        list_lines = [lines.strip(' ') for lines in text.split('\n')]
        revised = "\n".join(list_lines)
        print(revised, end="")

import re


def text_replaser(text):
    return re.sub("\n", " ", text)


def underscore(text):
    change = re.sub(" ", "_", text)
    return print(change)


def add_separator(text: str) -> str:
    text = text_replaser(text)
    if len(text) < 4899:
        return text

    separator = '_' * 50
    parts = [text[i:i + 4899] for i in range(0, len(text), 4899)]
    result = ''

    for part in parts:
        index = part.rfind('.')
        if index >= 0 and index < 4899:
            part = part[:index + 1] + separator + part[index + 1:]
        result += part

    return result


underscore("""

""")

print(add_separator(
"""

"""
))

def pin_extractor(poems):
    secret_codes = []

    for poem in poems:
        code = ""

        lines = poem.split("\n")

        for line_index, line in enumerate(lines):
            words = line.split()

            # Pick the word at the same index as the line number
            if line_index < len(words):
                code += str(len(words[line_index]))
            else:
                code += "0"

        secret_codes.append(code)

    return secret_codes



poem1 = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = """The grass is green
here and there
hoping for rain
before it turns yellow"""

poem3 = """There
once
was
a
dragon"""

print(pin_extractor([poem1, poem2, poem3]))

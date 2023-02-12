def bracket_checker(text):
    stack = []
    for i in range(len(text)):
        if text[i] in OPENING_BRACKETS:
            stack.append(text[i])
        elif text[i] in CLOSING_BRACKETS:
            bracket_type = CLOSING_BRACKETS[OPENING_BRACKETS.index(
                stack[-1])]  # Oh god
            if bracket_type == text[i]:
                stack.pop(-1)
            else:
                return i+1
    if len(stack) != 0:
        return len(text)
    return "Success"


OPENING_BRACKETS = ('(', '[', '{')
CLOSING_BRACKETS = (')', ']', '}')

text = input()

print(bracket_checker(text))

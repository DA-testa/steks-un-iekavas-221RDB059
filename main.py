import os


def bracket_checker(text):
    # if text[0:5] == "I\\r\\n":
    #     text = text[5:]
    stack = []
    for i in range(len(text)):
        if text[i] in OPENING_BRACKETS:
            stack.append(text[i])
        elif text[i] in CLOSING_BRACKETS:
            if len(stack) == 0:
                return i+1
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
file_or_input = input()
if file_or_input.lower() == "f":
    test_amount = len(os.listdir("test/"))
    good_tests = 0
    total_tests = 0
    for i in range(test_amount // 2):
        print(f"test {i+1}____________________________________________")

        with open(f"test/{i}") as f:
            lines = f.readline()
            answer = bracket_checker(lines)
            print(f"your answer: {answer}")
        with open(f"test/{i}.a") as f:
            lines = f.readline()
            print(f"actual answer: {lines}")
            if str(answer) == lines:
                print("good")
                good_tests += 1
        total_tests += 1
        i += 1
        print()
else:
    text = input()
    print(bracket_checker(text))
    

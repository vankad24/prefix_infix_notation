operator_chars = ['/', '*', '+', '-']

# bad attempt on which i spent a lot of time
# def to_infix2(lexemes):
#     stack = []
#     result = ""
#     is_left = True
#     for l in lexemes:
#         if l in operator_chars:
#             stack.append(l)
#             result+="("
#             is_left = True
#         else:
#             if not stack:
#                 op = ""
#             else:
#                 op = stack.pop()
#             if is_left:
#                 result+=f"{l} {op} "
#                 is_left = False
#             else:
#                 result+=f"{l}) {op} "
#                 is_left = True
#     return result

def validate(lexemes):
    numers = operators = 0
    for l in lexemes:
        if l in operator_chars:
            operators+=1
        else:
            if not l.isdigit():
                raise TypeError("Invalid character")
            numers+=1
    if operators + 1 != numers:
        raise ValueError("Not enough values to translate")


def to_infix(lexemes):
    validate(lexemes)
    stack = []
    for l in lexemes[::-1]:
        if l in operator_chars:
            try:
                left = stack.pop()
                right = stack.pop()
            except IndexError:
                raise ValueError("Ivalid expression")
            stack.append(f"({left} {l} {right})")
        else:
            stack.append(l)
    return stack[0]

def start():
    expr = input("Input an expression in prefix form:\n")
    lexemes = expr.split()
    try:
        validate(lexemes)
        return to_infix(lexemes)
    except Exception as e:
        return e.msg

if __name__ == "__main__":
    print(start())

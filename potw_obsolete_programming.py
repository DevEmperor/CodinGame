out = []
code = "stack = []\n"
instruction = " ".join(input() for _ in range(int(input()))).split()
t = 0

for idx, i in enumerate(instruction):
    if (i.startswith("-") and i[1:].isdigit()) or i.isdigit():
        code += " " * t + f"stack += [{i}]\n"
    elif i == "ADD":
        code += " " * t + "stack = stack[:-2] + [stack[-2] + stack[-1]]\n"
    elif i == "SUB":
        code += " " * t + "stack = stack[:-2] + [stack[-2] - stack[-1]]\n"
    elif i == "MUL":
        code += " " * t + "stack = stack[:-2] + [stack[-2] * stack[-1]]\n"
    elif i == "DIV":
        code += " " * t + "stack = stack[:-2] + [stack[-2] // stack[-1]]\n"
    elif i == "MOD":
        code += " " * t + "stack = stack[:-2] + [stack[-2] % stack[-1]]\n"
    elif i == "POP":
        code += " " * t + "stack.pop()\n"
    elif i == "DUP":
        code += " " * t + "stack += [stack[-1]]\n"
    elif i == "SWP":
        code += " " * t + "stack = stack[:-2] + [stack[-1]] + [stack[-2]]\n"
    elif i == "ROT":
        code += " " * t + "stack = stack[:-3] + stack[-2:] + [stack[-3]]\n"
    elif i == "OVR":
        code += " " * t + "stack += [stack[-2]]\n"
    elif i == "POS":
        code += " " * t + "stack += [int(stack.pop() >= 0)]\n"
    elif i == "NOT":
        code += " " * t + "stack += [int(stack.pop() == 0)]\n"
    elif i == "OUT":
        code += " " * t + "out.append(stack[-1])\n" + " " * t + "stack = stack[:-1]\n"
    elif i == "DEF":
        code += f"def {instruction[idx+1]}():\n" + " " * t + " global stack\n"
        t += 1
    elif i == "END":
        t -= 1
    elif i == "IF":
        code += " " * t + "if stack.pop() != 0:\n"
        t += 1
    elif i == "ELS":
        code += " " * (t - 1) + "else:\n"
    elif i == "FI":
        t -= 1
    elif instruction[idx - 1] != "DEF":
        code += " " * t + f"{i}()\n"

exec(code)
print(*out, sep="\n")

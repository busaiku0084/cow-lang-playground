#!/usr/bin/env python3
import sys

COW_CODE = {
    "MoO": "+",
    "MOo": "-",
    "moO": ">",
    "mOo": "<",
    "Moo": ".",
    "mOO": ",",
    "Ooo": "[",
    "oOo": "]"
}

def interpret_cow(code):
    tape = [0] * 30000
    ptr = 0
    output = []
    loop_stack = []
    i = 0

    while i < len(code):
        cmd = code[i]
        if cmd == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == ">":
            ptr += 1
        elif cmd == "<":
            ptr -= 1
        elif cmd == ".":
            output.append(chr(tape[ptr]))
        elif cmd == "[":
            if tape[ptr] == 0:
                loop_level = 1
                while loop_level > 0:
                    i += 1
                    if code[i] == "[":
                        loop_level += 1
                    elif code[i] == "]":
                        loop_level -= 1
            else:
                loop_stack.append(i)
        elif cmd == "]":
            if tape[ptr] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1
    # 標準出力に表示
    print("".join(output), flush=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: cow.py <filename>", flush=True)
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        cow_code = f.read().split()

    brainfuck_code = [COW_CODE[token] for token in cow_code if token in COW_CODE]
    interpret_cow(brainfuck_code)

if __name__ == "__main__":
    main()

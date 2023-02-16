# Anna Marija Liepina 221rdb078 14. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                print(i + 1)
                return
            opening_brackets_stack.pop()

    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack[-1].position)
    return


def main():
        command = input()
        if command[0] != 'I':
            return
        # while True:
        #     if command[0] in "([{}])":
        #         break
        #     else:
        #         command = command[1:]
        text = input()
        mismatch = find_mismatch(text)

if __name__ == "__main__":
    main()
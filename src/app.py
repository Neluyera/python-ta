import sys
import os


def prime(s):
    # your code goes here

    s = int(s)
    if s <= 1:
        return False
    for factor in range(2,s):
        if s % factor == 0:
            return False
    return True

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))

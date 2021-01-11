import sys
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    if arg1.isdigit():
        print(sum(list(map(int, arg1))))
    else:
        print("argument #1 is not a number")
else:
    print(f"usage: {sys.argv[0]} number")

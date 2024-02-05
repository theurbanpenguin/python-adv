import sys

if __name__ == '__main__':
    greeting = sys.argv[1].capitalize()
    name = sys.argv[2].capitalize()
    print(f"{greeting} {name}")
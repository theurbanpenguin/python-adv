import sys

if __name__ == '__main__':
    try:
        greeting = sys.argv[1].capitalize()
        name = sys.argv[2].capitalize()
    except IndexError:
        print(f"Usage {sys.argv[0]} <greeting> <name>")
        greeting = input("Enter a greeting: ").strip().capitalize()
        name = input("Enter a name: ").strip().capitalize()

    print(f"{greeting} {name}")
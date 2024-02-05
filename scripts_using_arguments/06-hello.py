import argparse, os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--greet', help='Enter a greeting such as Hello or Hi', type=str, default='Hello')
    parser.add_argument('-n', '--name', help='Enter a name', type=str, default=os.getlogin())
    args = parser.parse_args()

    greeting = args.greet.capitalize()
    name = args.name.capitalize()

    print(f"{greeting} {name}")

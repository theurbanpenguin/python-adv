import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--greet', help='Enter a greeting such as Hello or Hi', type=str, required=True)
    parser.add_argument('-n', '--name', help='Enter a name', type=str, required=True)
    args = parser.parse_args()

    greeting = args.greet.capitalize()
    name = args.name.capitalize()

    print(f"{greeting} {name}")
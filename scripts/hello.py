import sys


def greet(name):
    return f"Bonjour {name}"


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(target))

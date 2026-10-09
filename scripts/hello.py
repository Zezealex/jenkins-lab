import sys


def greet(name):
    greeting = "Bonjour " + name
    return greeting


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(target))

import sys

def main(argv):
    file = open(argv[1], "r").read()
    parsedFile = file.splitlines()
    print(parsedFile)

if __name__ == "__main__":
    main(sys.argv)
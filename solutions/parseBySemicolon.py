import sys

def main(argv):
    file = open(argv[1], "r")
    file = file.read()
    file = file.split(";")

    print(file)

if __name__ == "__main__":
    main(sys.argv)
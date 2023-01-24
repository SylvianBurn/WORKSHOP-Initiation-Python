import sys

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def main(argv):
    print(gcd(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
import sys

def fibonacci(nb):
    if nb <= 0:
        return 0
    elif nb == 1:
        return 1
    elif nb >= 2:
        nb0 = 0
        nb1 = 1

        next = nb0 + nb1
        for i in range(2, nb):
            nb0 = nb1
            nb1 = next
            next = nb0 + nb1
        return next


def main(argv):
    print(fibonacci(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
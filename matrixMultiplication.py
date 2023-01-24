import sys

def main(argv):
    matrix = [
        [3, 7, 13, 3],
        [6, 8, 1, 9],
        [4, 4, 10, 0],
        [8, 4, 5, 2]
    ]
    vector = [8, 16, 11, 3]

    result = []
    for line in matrix:
        tmp = 0
        for index, nb in enumerate(line):
            tmp += nb * vector[index]
        result.append(tmp)
    print(result)


if __name__ == "__main__":
    main(sys.argv)
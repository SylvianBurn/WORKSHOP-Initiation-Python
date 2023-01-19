import sys

# Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(2, n + 1):
            res *= i
        return(res)

def main(argv):
    try:
        int(argv[1])
    except:
        exit(84)
    print(factorial(int(argv[1])))



if __name__ == "__main__":
    main(sys.argv)
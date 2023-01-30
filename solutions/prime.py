import sys

def isPrime(nb):
    if nb > 1:
        for i in range(2, nb):
            if nb % i == 0:
                return f"{nb} is not a prime number"
                break
        else:
            return f"{nb} is a prime number"
    else:
        return f"{nb} is not a prime number"
    

def main(argv):
    print(isPrime(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
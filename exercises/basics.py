import sys

# Attention en Python, l'indentation est primordiale.
# Sans la bonne inndentation, votre programme ne fonctionnera pas.
# En python, il n'y a pas de point-virgule à la fin d'une ligne


# Prototype d'une fonction
def myFunc(a):
    # équivaut à for (int i = 0; i < 3; i++)
    for i in range(3):
        print(i, a)

def main(argv):
    # Déclaration de variables
    a = 10
    b = "oui"

    # Imprimer des variables
    print(a, b)
    myFunc(a)



if __name__ == "__main__":
    main(sys.argv)
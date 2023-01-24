import sys
import math

def distanceBetween2DPoints(x1, y1, x2, y2):
    dist = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
    return dist

def distanceBetween3DPoints(x1, y1, z1, x2, y2, z2):
    dist = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)) + ((z2 - z1) * (z2 - z1)))
    return dist

def main(argv):
    l = len(argv)

    if l == 5:
        print(distanceBetween2DPoints(float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4])))
    elif l == 7:
        print(distanceBetween3DPoints(float(argv[1]), float(argv[2]), float(argv[3]), float(argv[4]), float(argv[5]), float(argv[6])))


if __name__ == "__main__":
    main(sys.argv)
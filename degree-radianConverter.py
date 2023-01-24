import sys
import math

def radiansToDegrees(rad):
    deg = rad * 180 / math.pi
    return deg

def degreesToRadians(deg):
    rad = deg * math.pi / 180
    return rad

def main(argv):
    print(f"{float(argv[1])} radians corresponds to {radiansToDegrees(float(argv[1]))} degree")
    print(f"{float(argv[2])} degree corresponds to {degreesToRadians(float(argv[2]))} radian")

if __name__ == "__main__":
    main(sys.argv)
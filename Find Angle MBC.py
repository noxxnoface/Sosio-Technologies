import math

AB = float(input())
BC = float(input())
AC = math.hypot(AB, BC)
BM = AC / 2  # Length of median on to hypotenuse = half of hypotenuse
BE = BC / 2
print(str(round(math.degrees(math.acos(BE / BM)))) + "°")

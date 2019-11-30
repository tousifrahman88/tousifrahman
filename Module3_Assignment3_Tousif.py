import math
n = int (input ("Enter no of polygon point (>3): "))

if n > 3:
    print("Go ahead")
else:
    n = int (input ("Enter again (>3): "))



xcoordinate = []
ycoordinate = []

print("Enter x and y coordinates for polygon points:")

i = 1.0 
while i < (n+1):
    xcoordinate.append(int(input(f"x{i:<2.0f}:")))
    ycoordinate.append(int(input(f"y{i:<2.0f}:")))
    i = i + 1

print("-" * 20)

print(f"{'Point':<7} {'x':<7} {'y':<7}")

print("-" * 20)

for t in range(0,int(n)):
    print(f"{t+1:<6} {xcoordinate[t]:<7.2f} {ycoordinate[t]:<7.2f}")



print("-" * 30)


Ax = 0.0
for i in range(n-1):
    Ax = Ax + (xcoordinate [i+1] + xcoordinate [i]) * (ycoordinate [i+1] - ycoordinate [i])

Ax = 0.5 * Ax

print("the Ax of the polygon", Ax)


Sx = 0.0
for i in range(n-1):
    Sx = Sx + (xcoordinate [i+1] - xcoordinate [i]) * ((ycoordinate [i+1] * ycoordinate [i+1]) + (ycoordinate [i+1]* ycoordinate [i])+ (ycoordinate [i] * ycoordinate [i]))


Sx = (Sx / 6) * -1


print("the Sx of the polygon", Sx)

Sy = 0.0
for i in range(n-1):
    Sy = Sy + (ycoordinate [i+1] - ycoordinate [i]) * ((xcoordinate [i+1] * xcoordinate [i+1]) + (xcoordinate [i+1]* xcoordinate [i])+ (xcoordinate [i] * xcoordinate [i]))


Sy = (Sy / 6)


print("the Sy of the polygon", Sy)



Ix = 0.0
for i in range(n-1):
    Ix = Ix + (xcoordinate [i+1] - xcoordinate [i]) * ((ycoordinate [i+1] * ycoordinate [i+1] * ycoordinate [i+1]) + (ycoordinate [i+1] * ycoordinate [i+1] * ycoordinate [i]) + (ycoordinate [i] * ycoordinate [i] * ycoordinate [i+1]) + (ycoordinate [i] * ycoordinate [i] * ycoordinate [i])) 


Ix = (Ix / 12) * -1


print(f"the Ix of the polygon {Ix:.2f}")


Iy = 0.0
for i in range(n-1):
    Iy = Iy + (ycoordinate [i+1] - ycoordinate [i]) * ((xcoordinate [i+1] * xcoordinate [i+1] * xcoordinate [i+1]) + (xcoordinate [i+1] * xcoordinate [i+1] * xcoordinate [i]) + (xcoordinate [i] * xcoordinate [i] * xcoordinate [i+1]) + (xcoordinate [i] * xcoordinate [i] * xcoordinate [i])) 


Iy = (Iy / 12) 


print(f"the Iy of the polygon {Iy:.2f}")


Ixy = 0.0
for i in range(n-1):
    Ixy = Ixy + (ycoordinate [i+1] - ycoordinate [i]) * ((ycoordinate [i+1] * (3 * xcoordinate [i+1]**2 + 2 * xcoordinate [i+1] * xcoordinate [i] + xcoordinate [i]**2)) + (ycoordinate [i] * (3 * xcoordinate [i]**2 + 2 * xcoordinate [i+1] * xcoordinate [i] + xcoordinate [i+1]**2)))


Ixy = (Ixy / 24) * -1


print(f"the Ixy of the polygon {Ixy:.2f}")



Xt = 0.0

Xt = Sy / Ax


print(f"the Xt of the polygon {Xt:.2f}")


Yt = 0.0

Yt = Sx / Ax


print(f"the Yt of the polygon {Yt:.2f}")


Ixt = 0.0

Ixt = Ix - (Yt**2 * Ax)


print(f"the Ixt of the polygon {Ixt:.2f}")

Iyt = 0.0

Iyt = Iy - (Xt**2 * Ax)


print(f"the Iyt of the polygon {Iyt:.2f}")

Ixyt = 0.0

Ixyt = Ixy + (Xt * Yt * Ax)



print(f"the Ixyt of the polygon {Ixyt:.2f}")

print("-" * 30)

print("Thank You")






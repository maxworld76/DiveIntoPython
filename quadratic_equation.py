import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

X1 = X2 = None
D = b**2-4*a*c
if D < 0:
    pass    # no solution
elif D > 0:
    X1 = (-b + D**0.5)/(2*a)
    X2 = (-b - D**0.5)/(2*a)
else:
    X1 = X2 = -b/(2*a)
print(int(X1))
print(int(X2))

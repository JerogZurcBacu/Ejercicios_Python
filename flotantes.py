x = 0.0

for i in range(10):
    x += 0.1

if x >= 0.9999:
    print("x = " + str(x))
else:
    print("x != " + str(x))
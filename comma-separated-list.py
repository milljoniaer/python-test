import sys;

if (len(sys.argv) < 2) : sys.exit(1)

input = "".join(sys.argv[1:])

inputArray = input.split(",")

inputArrayInt = list(map(int, inputArray))

print("Array: " + str(inputArray))
print("Tuple: " + str(tuple(inputArray)))

print("Sum:   " + str(sum(inputArrayInt)))


sum = 0
for i in inputArrayInt:
    sum += i

print("Sum with Loop: " + str(sum))
from curses.ascii import isdigit
import sys;

if len(sys.argv) != 2: sys.exit(1)
if not isdigit(sys.argv[1]): sys.exit(1)
if int(sys.argv[1]) <= 0: sys.exit(1)

current = int(sys.argv[1])
print(current)

while current != 1 and current != 5 and current != 17:
    if current % 2 == 0:
        current = int(current / 2)
    else: 
        current = int(3 * current - 1)

    print(current)


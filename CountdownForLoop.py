# Name: Georgia Vrana
# Date Submitted: Saturday, Febuary 24th, 2024
# Assignment-3: CountdownForLoop
# Description: The program `CountdownForLoop.py` outputs a descending sequence of numbers from 99 to 0 
#              in a 10x10 grid, with each row reversing the order from right to left.

for x in range(100, 0, -10):
    for y in range(x - 1, x - 11, -1):
        print(f"{y:02d}", end=" ")
    print()



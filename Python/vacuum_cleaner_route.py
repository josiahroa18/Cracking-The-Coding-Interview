# Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. 
# The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

# Ex: Given the following strings...

# "LR", return true
# "URURD", return false
# "RUULLDRD", return true

# Plan
# Use a coordinate system [x, y] and run through the instructions
# if the robot returns to [0, 0]: return true
# otherwise: return false

# Reflect
# Algorithm runs in O(n) time complexity where n is the number of directions in the path
# Space complexity is O(1) since the only space we allocate is an array with 2 indices to keep track of coordinates
def route(path):
    position = [0, 0]
    for char in path:
        if char == 'L':
            position[0] -= 1
        elif char == 'R':
            position[0] += 1
        elif char == 'D':
            position[1] -= 1
        elif char == 'U':
            position[1] += 1
    if position[0] == 0 and position[1] == 0:
        return True
    else:
        return False

def main():
    # Tests
    path = 'LR'
    print(route(path)) # Expect True

    path = 'URURD'
    print(route(path)) # Expect False

    path = 'RUULLDRD'
    print(route(path)) # Expect True

if __name__ == "__main__":
    main()
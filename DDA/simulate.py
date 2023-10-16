'''
You are tasked with simulating the motion of a particle in 2D space. 
The particle starts at coordinates (0, 0) and moves randomly in either the positive or negative
x or y direction by a random amount at each time step. 
The simulation will run for a specified number of steps.
Write a Python program that simulates this motion and prints out the final position of the particle.
'''

import random

# starting point
x ,y = (0, 0)

# specify the number of steps to simulate
num_step = int(input("Enter number of steps: "))

for step in range(num_step):
    # generate random steps in x, y direction
    x_step = random.choice([-1, 1])
    y_step = random.choice([-1, 1])
    # update the positions
    x += x_step
    y += y_step

print(f'Final position: ({x}, {y})')
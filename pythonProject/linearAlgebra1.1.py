import numpy as np

# Example 2 from Chapter 1.1 in Linear Algebra book

# Define the coefficient matrix A and the right-hand side vector b
A = np.array([[1, -2, 1],
              [0, 2, -8],
              [5, 0, -5]])

b = np.array([0, 8, 10])

# Try to solve the system
try:
    solution = np.linalg.solve(A, b)
    print("The system is consistent. Solution:", solution)
except np.linalg.LinAlgError:
    print("The system is inconsistent.")


# A solution of the linear system is a list (s1, s2,..., sn) of numbers that makes each equation a true statement when
# the values s1,..., sn are substituted for x1,..., xn, respectively. A list is an ordered sequence. A solution is a
# set of constants.
#
# The set of all possible solutions is called the solution set of the system. Two linear systems are called equivalent
# if they have the same solution set.

import matplotlib.pyplot as plt

# Define the equations as functions
def line1(x1):
    return (x1 + 1) / 2

def line2(x1):
    return (3 + x1) / 3

# Set up the range for x1 values
x_values = np.linspace(-10, 10, 400)

# Calculate the point of intersection
A = np.array([[1, -2], [-1, 3]])
B = np.array([-1, 3])
intersection = np.linalg.solve(A, B)
x_intersect, y_intersect = intersection

# Plot the lines
plt.plot(x_values, line1(x_values), label='$x_1 - 2x_2 = -1$')
plt.plot(x_values, line2(x_values), label='$-x_1 + 3x_2 = 3$')

# Mark the point of intersection
plt.plot(x_intersect, y_intersect, 'ro')  # red dot at the intersection
plt.text(x_intersect, y_intersect, f' ({x_intersect:.1f}, {y_intersect:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right', weight='bold')

# Configure the plot
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xticks(np.arange(-10, 11, 2))
plt.yticks(np.arange(-10, 11, 2))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.title('Graph of the equations $x_1 - 2x_2 = -1$ and $-x_1 + 3x_2 = 3$')

# Show the plot
plt.show()


## Define the augmented matrix [A|b]
augmented_matrix = np.array([[1, -2, 1, 0],
                             [0, 2, -8, 8],
                             [-4, 5, 9, -9]], dtype=float)

# Step 2.1: R3 -> R3 + 4 * R1
augmented_matrix[2] = augmented_matrix[2] + 4 * augmented_matrix[0]

# Step 2.2: R3 -> R3 + (3/2) * R2
augmented_matrix[2] = augmented_matrix[2] + (3/2) * augmented_matrix[1]

# Back substitution to solve for x1, x2, x3
# Extract the values from the augmented matrix
a31 = augmented_matrix[2, 3]  # x3 = 3
a22, b2 = augmented_matrix[1, 1], augmented_matrix[1, 3]
a12, a13, b1 = augmented_matrix[0, 1], augmented_matrix[0, 2], augmented_matrix[0, 3]

# Solve for x3
x3 = a31

# Solve for x2
x2 = (b2 + 8 * x3) / a22

# Solve for x1
x1 = b1 + 2 * x2 - x3

# Display the solution
print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")

print()
#--------------------EASIER WAY------------

# Define the coefficient matrix A and the right-hand side vector b
A = np.array([[1, -2, 1],
              [0, 2, -8],
              [-4, 5, 9]], dtype=float)

b = np.array([0, 8, -9], dtype=float)

# Solve the system using np.linalg.solve
try:
    solution = np.linalg.solve(A, b)
    x1, x2, x3 = solution
    print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
except np.linalg.LinAlgError:
    print("The system is inconsistent or does not have a unique solution.")
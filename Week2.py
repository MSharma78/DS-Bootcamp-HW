import numpy as np

# Define two custom numpy arrays A and B
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# Stack A and B vertically and horizontally
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

# Find common elements between A and B (Intersection)
common_elements = np.intersect1d(A, B)

# Extract all numbers from A which are within a specific range (5 to 10)
numbers_in_range = A[(A >= 5) & (A <= 10)]

# Load the iris dataset (first four columns only)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_2d = np.genfromtxt(url, delimiter=',', dtype=float, usecols=[0, 1, 2, 3])

# Filter rows where petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]

# Print results
print("Vertical Stack:\n", vertical_stack)
print("\nHorizontal Stack:\n", horizontal_stack)
print("\nCommon Elements:", common_elements)
print("\nNumbers in Range (5-10):", numbers_in_range)
print("\nFiltered Iris Dataset Rows:\n", filtered_rows)

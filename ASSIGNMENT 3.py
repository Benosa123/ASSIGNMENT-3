import numpy as np

# Saving and Writing Files Using NumPy

# 1 - Save a 2D array to a CSV file
data_matrix = np.array([[10, 25, 13], [15, 24, 14], [17, 35, 18]])
np.savetxt('data_matrix.csv', data_matrix, delimiter=',')

print("CSV file saved successfully.")

# 2 - Save a 1D array to a binary file
names_array = np.array([["kai"], ["kai"], ["kai"]])
np.save('names_array.npy', names_array)

print("Binary file saved successfully.")

# 3 - Save multiple arrays to a compressed file
array_one = np.array([[14, 8, 19], [5, 12, 7]])
array_two = np.array([[19, 15, 14], [7, 16, 13]])
np.savez_compressed('compressed_arrays.npz', array_one=array_one, array_two=array_two)

print("Compressed file saved successfully.")

# Loading Data from Files Using NumPy

# 1 - Load a 2D array from a CSV file
loaded_matrix = np.loadtxt('data_matrix.csv', delimiter=',')
print("Loaded from CSV file:\n", loaded_matrix)

print()

# 2 - Load a 1D array from a binary file
loaded_names = np.load('names_array.npy')
print("Loaded from binary file:\n", loaded_names)

print()

# 3 - Load multiple arrays from a compressed file
compressed_file = np.load('compressed_arrays.npz')
loaded_array_one = compressed_file['array_one']
loaded_array_two = compressed_file['array_two']
print("Loaded from compressed file:\nArray One:\n", loaded_array_one, "\nArray Two:\n", loaded_array_two)

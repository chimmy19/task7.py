
import numpy as np 

#arrays
A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

print('Array A = ', A)
print('Array B = ', B)

#operations
adding = A + B
subtracting = A - B
multiplying = A * B
dividing = A / B

print('A + B = ', adding)
print('A - B = ', subtracting)
print('A * B = ', multiplying)
print('A / B = ', dividing)

#functions
mean_A = np.mean(A)
max_A = np.max(A)
min_A = np.min(A)
dot_product = np.dot(A, B)
reshaped_A = A.reshape(5, 1)


print('mean_A = ', mean_A)
print('max_A = ', max_A)
print('min_A = ', min_A)
print('Dot product of A and B = ', dot_product)
print('Reshaped A(5, 1) = \n', reshaped_A)


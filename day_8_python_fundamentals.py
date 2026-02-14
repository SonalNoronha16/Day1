import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
result = a + b
print(result)

#1D Array
import numpy as np
a_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(a_1d)

#2D Array
a_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D Array:")
print(a_2d)

#3D Array
a_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])
print("\n3D Array:")
print(a_3d)

#0D Array
import numpy as np
a_0d = np.array(10)
print("0D Array:")
print(a_0d)

import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)
# Vectorized vs Loop example
arr = np.random.rand(1000000)
# Vectorized
squared = arr ** 2

#reshape
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)

#hstack
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(np.hstack((a, b)))

#Statistics
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=1))

#Linear Algebra
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print(np.dot(A, B))

#The Normalizer
import numpy as np

np.random.seed(42) 
scores = np.random.randint(50, 101, size=(5, 3))

subject_mean = np.mean(scores, axis=0)

centered_scores = scores - subject_mean

print("Original Scores:")
print(scores)

print("\nSubject-wise Mean:")
print(subject_mean)

print("\nCentered Scores (After Broadcasting):")
print(centered_scores)

#The Reshaper
import numpy as np

data = np.arange(24)

reshaped_data = data.reshape(4, 3, 2)

final_data = reshaped_data.transpose(0, 2, 1)

print("Final Shape:", final_data.shape)
print("Final Array:")
print(final_data)







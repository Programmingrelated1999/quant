import numpy as np

# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Main Function
def main():
    # Simple Matrix Addition
    print("Simple Matrix Addition: ")
    result = A + B
    print("Answer: \n", result)
    # Simple Matrix Subtraction
    print("Simple Matrix Subtraction: ")
    result = A - B
    print("Answer: \n", result)
    # Simple Matrix Multiplication
    print("Simple Matrix Multiplication: ")
    result = A @ B
    print("Answer: \n", result)
    # Simple Matrix Scalar Multiplication
    C = 4
    print("Simple Matrix Scalar Multiplication: ")
    result = A * C
    print("Answer: \n", result)
    # Simple Matrix Transpose
    print("Simple Matrix Transpose: ")
    result = A.T
    print("Answer: \n", result)
    # Simple Matrix Inverse
    print("Simple Matrix Inverse: ")
    result = np.linalg.inv(A)
    print("Answer: \n", result)



# Run Main Function 
if __name__ == "__main__":
    main()
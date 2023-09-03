# Gradient Descent to find the minimum of a quadratic function

# Define the quadratic function (example: f(x) = x^2)
def quadratic_function(x):
    return x**2

# Define the gradient of the function (df/dx = 2x)
def gradient(x):
    return 2 * x

# Initialize the starting point
x_start = 5.0

# Set the learning rate
learning_rate = 0.1

# Number of iterations
num_iterations = 100

# Perform gradient descent
for i in range(num_iterations):
    # Calculate the gradient at the current point
    grad = gradient(x_start)
    
    # Update the point using gradient descent
    x_start = x_start - learning_rate * grad
    
    # Calculate the value of the function at the updated point
    f_x = quadratic_function(x_start)
    
    # Print the progress
    print(f"Iteration {i+1}: x = {x_start:.4f}, f(x) = {f_x:.4f}")

# Print the final result
print(f"Minimum found at x = {x_start:.4f}, f(x) = {f_x:.4f}")

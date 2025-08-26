import math

# Use a predefined number instead of input
num = 5  # Change this value for different tests

# Perform calculations with error handling
try:
    # Square root (only valid for non-negative numbers)
    if num >= 0:
        square_root = math.sqrt(num)
    else:
        square_root = "Error (Square root not defined for negative numbers)"
    
    # Logarithm (only valid for positive numbers)
    if num > 0:
        logarithm = math.log(num)
    else:
        logarithm = "Error (Logarithm not defined for zero or negative numbers)"
    
    # Sine (valid for all real numbers)
    sine_value = math.sin(num)

    # Display results
    print(f"Square root: {square_root}")
    print(f"Logarithm: {logarithm}")
    print(f"Sine: {sine_value}")

except Exception as e:
    print("An error occurred:", e)

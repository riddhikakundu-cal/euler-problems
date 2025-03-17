def digit_sum(n):
    """Returns the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

# Taking user input for maximum base and exponent
max_base = int(input("Enter the maximum base: "))
max_exponent = int(input("Enter the maximum exponent: "))

max_sum = 1

# Iterate through all values of a^b where a, b < user input
for base in range(1, max_base):
    power = 1  # Initial value (base^0)
    for exponent in range(1, max_exponent):
        power *= base  # Calculate base^exponent
        current_sum = digit_sum(power)  # Compute digit sum
        
        # Update max_sum if current_sum is larger
        if current_sum > max_sum:
            max_sum = current_sum

print("Maximum digital sum:", max_sum)

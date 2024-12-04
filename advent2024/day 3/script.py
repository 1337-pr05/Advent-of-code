import re

def extract_compute_with_conditions(input_string):
    # Regex patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Split the input into instructions
    instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_string)
    
    # Initial state
    is_mul_enabled = True
    total_sum = 0
    
    for instruction in instructions:
        if re.match(do_pattern, instruction):
            is_mul_enabled = True  # Enable mul instructions
        elif re.match(dont_pattern, instruction):
            is_mul_enabled = False  # Disable mul instructions
        elif re.match(mul_pattern, instruction) and is_mul_enabled:
            # Extract numbers and compute product
            x, y = map(int, re.findall(r"\d+", instruction))
            total_sum += x * y
    
    return total_sum

# Read input string from file
with open("text.txt") as f:
    input_string = f.read()

# Compute the result
result = extract_compute_with_conditions(input_string)
print("Sum of enabled mul results:", result)


import re

def extract_compute(input_string):
    # Regular expression 
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches
    matches = re.findall(pattern, input_string)
    # Compute the sum of products
    total = 0
    for match in matches:
        x, y = map(int, match) 
        total += x * y
    
    return total


with open("text.txt") as f:
    input_string = f.read()

# Compute the result
result = extract_compute(input_string)
print("Sum of all valid multiplications:", result)

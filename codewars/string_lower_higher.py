#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers_str):
    numbers = numbers_str.split()  # Split the input string into separate numbers
    numbers = [int(num) for num in numbers]  # Convert the numbers to integers

    highest = max(numbers)  # Find the highest number
    lowest = min(numbers)  # Find the lowest number

    result = f"{highest} {lowest}"  # Format the result as a string
    return result

# Example usage:
numbers_str = "0 2 3 4 5"
result = high_and_low(numbers_str)
print(result)

def calculate_average(numbers):
    if not numbers:  # Handle empty list
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")
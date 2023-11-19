def calculate_sum_multiply(list):
    if not list:  # Check for an empty list
        return 0
    sum_even_indexes = sum(list[i] for i in range(0, len(list), 2))
    result = sum_even_indexes * list[-1]
    return result

# Example:
# my_list = [0, 1, 7, 2, 4, 8]
# result = calculate_sum_multiply(my_list)
# print(result)

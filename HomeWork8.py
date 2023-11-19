def sum_multiply(list):
    if not list:  # Check for an empty list
        return 0
    sum_even_i = sum(list[i] for i in range(0, len(list), 2))  # Sum elements with even indexes
    result = sum_even_i * list[-1]  # Multiply by the last element
    return result

list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zeros = [x for x in list if x != 0]
zeros = [0] * (len(list) - len(non_zeros))
new_list = non_zeros + zeros
print(new_list)

def common_elements():
    list_3 = [i for i in range(1, 101) if i % 3 == 0]
    list_5 = [i for i in range(1, 101) if i % 5 == 0]

    common_set = set(list_3) & set(list_5)

    return common_set

result = common_elements()
print(result)

import random
first_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
second_list = [first_list[0], first_list[2], first_list[-2]]
print("Перший список:", first_list)
print("Другий список:", second_list)

# запит вводу
x = int (input("Please enter a 4-digit whole number:  "))
# перевірка
a = int(x) // 1000
x = int(x) % 1000
b = x // 100
x = x % 100
c = x // 10
d = x % 10
# вивод
print(a)
print(b)
print(c)
print(d)

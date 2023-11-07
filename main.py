# запит вводу
x = int (input("Please enter a 5-digit whole number:  "))
# перевірка
a = int(x) // 10000
x = int(x) % 10000
b = x // 1000
x = x % 1000
c = x // 100
x = x % 100
d = x // 10
e = x % 10
# вивід
print(e,d,c,b,a)

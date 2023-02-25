numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)

# List comprehension
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

numbers_v3 = [element * 2 for element in range(1, 11)]
print(numbers_v3)  # Lista de los numeros multiplicado por 2

### Solo agregar los pares y multiplicar por dos

# Version for
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)

# Version list comprehension
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)
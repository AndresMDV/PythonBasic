#-----------Dict comprehension con coniciones------------

#Crear un dict comprehension con una lista
import random
countries = ['colombia', 'bolivia', 'mexico']

population = { country: random.randint(1, 100) for country in countries}
print(population)

#crear un dict comprehension con una condicion
#paises con poblacion mayor a 30
result = {country: population for (country, population) in population.items() if population > 30}
print(result)

#dict comprehension de las vocales de una oracion
text = 'Hola nuevo mundo'
unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)
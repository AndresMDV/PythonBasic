# Funciones anónimas: lambda
# https://www.w3schools.com/python/python_lambda.asp

# Funcion
def increment(x):
  return x + 1

# Transformar en lambda function
increment_v2 = lambda x: x + 1

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}' # La funcion title hace que las palabras inicien en mayuscula

text = full_name("sara maria", "mejia sanchez")
print(text)
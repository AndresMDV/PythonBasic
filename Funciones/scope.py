# El scope
# https://www.w3schools.com/python/python_scope.asp

'''
Global scope:
La variable puede ser usada en cualquier bloque de código dentro del programa
'''
price = 100

'''
Local scope: 
La variable solo va a tener sentido dentro del bloque de código donde fue creada (en este caso dentro de la funcion)
'''
def increment():
  price = 200
  price = price + 10
  return price


print(price) # Variable Global scope
price_2 = increment() # Retorna el valor de variable Local Scope
print(price_2)
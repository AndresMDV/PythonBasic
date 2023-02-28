import random

dic_v1 = {}

for i in range(1,11):
  dic_v1[i] = i * 2

print(dic_v1)

dic_v2 = {i: i * 2 for i in range(1,11)}
print(dic_v2)


contries_mercosur = ['ar','br','pr','uy']
population = {}
for i in contries_mercosur:
  population[i] = random.randint(3,220)
print(population)

pop_v2 = {i: random.randint(3,220) for i in contries_mercosur}
print(pop_v2)

names = ['pedro','marcelo','cacho']
ages = [21,54,35]

print(list(zip(names,ages)))

new_dic = {names: ages for (names,ages) in zip(names,ages)}
print(new_dic)
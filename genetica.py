import random

def calculate_aptitud(individuo):
  aptitud = sum([x**2 + 2 for x in individuo])
  return aptitud

def most_apt(array1):
  apts = [calculate_aptitud(individuo) for individuo in array1]
  better_index = apts.index(max(apts))
  return array1[better_index]

def cruza(padre1, padre2):
  cross_point = random.randint(1, len(padre1))
  hijo1 = padre1[:cross_point] + padre2[cross_point:]
  hijo2 = padre2[:cross_point] + padre1[cross_point:]
  return hijo1, hijo2

people = 30 # Ajustable
bits = 1
range_num = range(1, 16)

array1 = [[random.choice(range_num) for i in range(bits)] for i in range(people)]
binary_array = [[format(num, '04b') for num in individuo] for individuo in array1]

print("Población inicial:")
for i, individuo in enumerate(binary_array, start=1):
  print(f"Individuo {i}: {individuo}")

print('\n')

parent_index1 = 0
parent_index2 = 1

parent1 = array1[parent_index1]
parent2 = array1[parent_index2]

hijo1, hijo2 = cruza(parent1, parent2)

array1[parent_index1] = hijo1
array1[parent_index2] = hijo2

for i, individuo in enumerate(array1, start = 1):
  individual_aptitud = calculate_aptitud(individuo)
  print(f'Aptitud del individuo {i}: {individual_aptitud}')

print('\n')

individuo_mas_apto = most_apt(array1)
print('El individuo más apto tiene un:', individuo_mas_apto)

print('\n')

# Realiza la cruza entre todos los padres
num_padres = len(array1)

for i in range(num_padres):
  for j in range(i + 1, num_padres):
    padre1 = array1[i]
    padre2 = array1[j]
    
    hijo1, hijo2 = cruza(padre1, padre2)
    
    # Reemplazar a los padres con sus hijos en el array1
    array1[i] = hijo1
    array1[j] = hijo2

# Convierte el arreglo a representación binaria
arreglo_binario = [[format(num, '04b') for num in individuo] for individuo in array1]

# Encuentra el individuo más apto después de la cruza
individuo_mas_apto = most_apt(array1)

print("Arreglo después de la cruza:")
for i, individuo in enumerate(arreglo_binario, start=1):
  print(f"Individuo {i}: {individuo}")

print("El individuo más apto tiene un:", individuo_mas_apto)

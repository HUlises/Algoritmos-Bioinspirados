import random

def calcular_aptitud(individuo):
    aptitud = sum([x**2 + 2 for x in individuo])
    return aptitud

def most_apt(arreglo):
    apts = [calcular_aptitud(individuo) for individuo in arreglo]
    better_index = apts.index(max(apts))
    return arreglo[better_index], apts[better_index]

def cruza(padre1, padre2):
    cross_point = random.randint(1, len(padre1))
    hijo1 = padre1[:cross_point] + padre2[cross_point:]
    hijo2 = padre2[:cross_point] + padre1[cross_point:]
    return hijo1, hijo2

poblacion = 30
bits = 1
rango = range(1,16)

arreglo = [[random.choice(rango) for i in range(bits)] for i in range(poblacion)]
arreglo_binario = [[format(num,'04b') for num in individuo] for individuo in arreglo]

print(arreglo_binario)
print('\n')

parent1_index = 0
parent2_index = 1

parent1 = arreglo[parent1_index]
parent2 = arreglo[parent2_index]

hijo1, hijo2 = cruza(parent1, parent2)

arreglo[parent1_index] = hijo1
arreglo[parent2_index] = hijo2

for i, individuo in enumerate(arreglo, start = 1):
    aptitud_individual = calcular_aptitud(individuo)
    print(f'Aptitud del individuo {i}: {aptitud_individual}')

print('\n')

individuo, aptitud = most_apt(arreglo)
print('Aptitud del individuo con mejor aptitud: ', individuo)
print('Con una aptitud de: ', aptitud)

print('Padre 1: ', parent1)
print('Padre 2; ', parent2)
print('Hijo 1: ', hijo1)
print('Hijo 2: ', hijo2)
arreglo_binario = [[format(num,'04b') for num in individuo] for individuo in arreglo]
print('Arreglo despues de la cruza: ', arreglo_binario)
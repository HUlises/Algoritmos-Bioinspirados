import math
import random

# Función de costo (puede ser reemplazada por la función que desees minimizar)
def cost_function(x):
  return x ** 2

# Parámetros del algoritmo
initial_solution = random.uniform(-10, 10)  # Solución inicial aleatoria
initial_temperature = 100.0
cooling_rate = 0.95
num_iterations = 1000

# Función para generar una solución vecina
def get_neighbor(solution, temperature):
  # Genera una solución vecina haciendo un pequeño cambio aleatorio
  neighbor = solution + random.uniform(-0.1, 0.1)
  return neighbor

# Algoritmo de recocido simulado
current_solution = initial_solution
best_solution = current_solution
current_cost = cost_function(current_solution)
best_cost = current_cost
temperature = initial_temperature

for _ in range(num_iterations):
  neighbor_solution = get_neighbor(current_solution, temperature)
  neighbor_cost = cost_function(neighbor_solution)

  # Si la solución vecina es mejor, aceptarla
  if neighbor_cost < current_cost:
    current_solution = neighbor_solution
    current_cost = neighbor_cost
    # Actualizar la mejor solución si es necesario
    if current_cost < best_cost:
      best_solution = current_solution
      best_cost = current_cost
  else:
    # Si la solución vecina es peor, aceptarla con una cierta probabilidad
    probability = math.exp(-(neighbor_cost - current_cost) / temperature)
    if random.random() < probability:
      current_solution = neighbor_solution
      current_cost = neighbor_cost

  # Enfriar la temperatura
  temperature *= cooling_rate

print("Mejor solución encontrada:", best_solution)
print("Valor de la función objetivo en la mejor solución:", best_cost)

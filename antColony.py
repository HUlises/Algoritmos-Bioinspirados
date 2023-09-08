import numpy as np

def hormigas(n_hormigas, n_iteraciones, matriz_costo):
  """
  Algoritmo de colonia de hormigas para encontrar el camino más corto entre dos puntos en un grafo.

  Args:
    n_hormigas: Número de hormigas a utilizar.
    n_iteraciones: Número de iteraciones a realizar.
    matriz_costo: Matriz de costos de los arcos del grafo.

  Returns:
    Un vector con la secuencia de vértices del camino más corto.
  """

  # Inicializamos las hormigas.
  hormigas = []
  for _ in range(n_hormigas):
    hormigas.append(Hormiga(matriz_costo.shape[0]))

  # Inicializamos las feromonas.
  feromonas = np.ones(matriz_costo.shape)

  # Realizamos las iteraciones.
  for iteracion in range(n_iteraciones):
    # Las hormigas recorren el grafo.
    for hormiga in hormigas:
      hormiga.recorrer(feromonas)

    # Actualizamos las feromonas.
    feromonas = actualizar_feromonas(feromonas, hormigas)

  # Devolvemos el camino más corto.
  mejor_hormiga = hormigas[np.argmin([hormiga.costo for hormiga in hormigas])]
  return mejor_hormiga.camino


class Hormiga:
  """
  Representa una hormiga en el algoritmo de colonia de hormigas.

  Atributos:
    n_vertice_actual: Vértice actual de la hormiga.
    n_vertice_siguiente: Vértice siguiente de la hormiga.
    camino: Secuencia de vértices del camino recorrido por la hormiga.
    costo: Costo del camino recorrido por la hormiga.
  """

  def __init__(self, n_vertices):
    self.n_vertice_actual = 0
    self.n_vertice_siguiente = 0
    self.camino = []
    self.costo = 0

  def recorrer(self, feromonas):
    self.camino.append(self.n_vertice_actual)

    # Elegimos el vértice siguiente.
    posibles_vecinos = [
        vertice for vertice in range(feromonas.shape[0])
        if vertice != self.n_vertice_actual
    ]
    probabilidad = np.array([
        feromonas[self.n_vertice_actual, vertice] / sum(feromonas[self.n_vertice_actual, posibles_vecinos])
        for vertice in posibles_vecinos
    ])
    self.n_vertice_siguiente = posibles_vecinos[np.random.choice(len(posibles_vecinos), p=probabilidad)]

    # Actualizamos el costo del camino.
    self.costo += matriz_costo[self.n_vertice_actual, self.n_vertice_siguiente]


def actualizar_feromonas(feromonas, hormigas):
  """
  Actualiza las feromonas del grafo.

  Args:
    feromonas: Matriz de feromonas del grafo.
    hormigas: Lista de hormigas.

  Returns:
    Una matriz con las feromonas actualizadas.
  """

  for hormiga in hormigas:
    for i in range(len(hormiga.camino) - 1):
      feromonas[hormiga.camino[i], hormiga.camino[i + 1]] += hormiga.costo

  # Evaporamos las feromonas.
  feromonas *= (1 - evap)

  return feromonas

def imprimir_resultados(camino, matriz_costo):
  """
  Imprime los resultados del algoritmo de colonia de hormigas.

  Args:
    camino: Camino encontrado por el algoritmo.
    matriz_costo: Matriz de costos de los arcos del grafo.
  """

  print("Camino más corto:")
  for vertice in camino:
    print(vertice)

  print("Costo del camino:", matriz_costo[camino[0], camino[-1]])


if __name__ == "__main__":
  # Definimos los parámetros del algoritmo.
  n_hormigas = 100
  n_iteraciones = 100
  evap = 0.9

  # Generamos un grafo aleatorio.
  n_vertices = 10
  matriz_costo = np.random.randint(1, 10, (n_vertices, n_vertices))

  # Encontramos el camino más corto.
  camino = hormigas(n_hormigas, n_iteraciones, matriz_costo)

  # Imprimimos los resultados.
  imprimir_resultados(camino, matriz_costo)
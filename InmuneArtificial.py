import numpy as np

class Cell:
    def __init__(self, weights):
        self.weights = weights

    def fitness(self, data):
        # Calculate the fitness of the cell
        return 1.0 / sum((self.predict(x) - y)**2 for x, y in data)

    def predict(self, x):
        # Predict the output of the cell
        return np.dot(self.weights, x)

class AIS:
    def __init__(self, data, population_size=100):
        self.data = data
        self.population_size = population_size

    def fit(self, epochs=100):
        # Initialize the population
        self.population = [Cell(np.random.rand(len(self.data[0][0]))) for _ in range(self.population_size)]

        for _ in range(epochs):
            # Evaluate the fitness of the population
            fitnesses = [cell.fitness(self.data) for cell in self.population]

            # Select the best cells
            selected = np.argsort(fitnesses)[-self.population_size // 2:]

            # Mutate the best cells
            for i in selected:
                self.population[i].weights = self.mutate(self.population[i].weights)

            # Recombine the best cells
            for i in range(len(self.population) - 1, -1, -1):
                if i % 2 == 0:
                    self.population[i] = self.recombine(self.population[i], self.population[i - 1])

    def mutate(self, weights):
        # Mutate the weights of the cell
        for i in range(len(weights)):
            if np.random.rand() < 0.1:
                weights[i] += np.random.rand() - 0.5
        return weights

    def recombine(self, cell1, cell2):
        # Combine the weights of two cells
        weights = np.array(cell1.weights)
        for i in range(len(weights)):
            if np.random.rand() < 0.5:
                weights[i] = cell2.weights[i]
        return Cell(weights)


# Example
data = [(np.array([1, 2]), 1), (np.array([3, 4]), 2)]
ais = AIS(data)
ais.fit(100)

# Print the best cell
print(ais.population[0].weights)

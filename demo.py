import random

# Define the fitness function (customize based on the problem)
def fitness_function(solution):
    # Example fitness function: maximizing the sum of binary digits
    return sum(solution)

# Generate an initial population
def generate_population(population_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

# Select parents for crossover based on tournament selection
def tournament_selection(population, tournament_size):
    selected_parents = []
    population_size = len(population)
    
    for _ in range(population_size):
        tournament = random.sample(population, tournament_size)
        best_solution = max(tournament, key=fitness_function)
        selected_parents.append(best_solution)
    
    return selected_parents

# Perform one-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Perform mutation with adaptive mutation rate
def mutate(solution, mutation_rate):
    mutated_solution = solution[:]
    for i in range(len(mutated_solution)):
        if random.random() < mutation_rate:
            mutated_solution[i] = 1 - mutated_solution[i]  # Flip the bit
    return mutated_solution

# Genetic algorithm with adaptive mutation rate
def adaptive_genetic_algorithm(population_size, chromosome_length, tournament_size, initial_mutation_rate, generations):
    population = generate_population(population_size, chromosome_length)
    mutation_rate = initial_mutation_rate
    best_solution = None
    
    for generation in range(generations):
        parents = tournament_selection(population, tournament_size)
        next_generation = []
        
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
        
        population = next_generation
        best_solution = max(population, key=fitness_function)
        
        # Adjust mutation rate based on performance
        mutation_rate = adjust_mutation_rate(mutation_rate, best_solution, generation)
        
        # Print best solution and fitness at each generation
        print(f"Generation {generation + 1}: Best solution: {best_solution}, Fitness: {fitness_function(best_solution)}")
    
    return best_solution

# Adaptive mutation rate adjustment function
def adjust_mutation_rate(current_mutation_rate, best_solution, generation):
    # Example: Decrease mutation rate if no improvement in the last 10 generations
    if generation % 10 == 0:
        return current_mutation_rate * 0.9
    else:
        return current_mutation_rate

# Example usage
population_size = 100
chromosome_length = 20
tournament_size = 5
initial_mutation_rate = 0.1
generations = 50

best_solution = adaptive_genetic_algorithm(population_size, chromosome_length, tournament_size, initial_mutation_rate, generations)
print("\nFinal best solution:", best_solution)
print("Final fitness:", fitness_function(best_solution))

import random
from math import exp,dist

def simulated_annealing(state):
  initial_temp = 90
  final_temp = .1
  alpha = 0.01
  i = 0

  #define antes da primeira iteraçao o estado atual como o estado inicial
  current_temp = initial_temp
  solution = state.copy()

  while current_temp > final_temp:
    i += 1
    neighbor = get_neighbors(solution)
    #calcula a diferenca de custo do vizinho e avalia a entrada
    cost_diff = get_cost(solution) - get_cost(neighbor)
    if cost_diff > 0:
      solution = neighbor.copy()
    else:
      try:
        heuristic = exp(-cost_diff / current_temp)
        print(heuristic)
      except OverflowError:
        heuristic = float('inf')
      if random.uniform(1, 10) > heuristic:
        solution = neighbor.copy()
    #diminui a temperatura
    current_temp -= alpha

  return solution

#Calcula a distancia total da solucao
def get_cost(state):
  cost = 0
  for i in range(0,len(state)-1):
    cost += dist(state[i][1],state[i+1][1])
  return cost

#Perturba a solucao fazendo no mínimo um swap e no máximo cinco, gerando um vizinho
def get_neighbors(state):
  neighbor = state.copy()
  for i in range(5):
    index_a = random.randint(0,50)
    index_b = random.randint(0,50)
    neighbor[index_a],neighbor[index_b] = neighbor[index_b],neighbor[index_a] #swap

  return neighbor

def main():
  #carrega os dados e salva no array de cidades
  f= open('51cities.txt','r')
  cities = []
  for row in f:
    cities.append([int(row.strip().split()[0]),(int(row.strip().split()[1]),int(row.strip().split()[2]))])

  #gera um estado inicial aleatorio
  initial_state = random.sample(cities,len(cities))

  #aplica o simulated_annealing
  optimizedRoute = simulated_annealing(initial_state)
  print(optimizedRoute)
  print('Custo total:{cost}'.format(cost=get_cost(optimizedRoute)))
  x = open('results.txt','a')
  x.write(f"{get_cost(optimizedRoute)}\n")

if __name__ == "__main__":
  main()

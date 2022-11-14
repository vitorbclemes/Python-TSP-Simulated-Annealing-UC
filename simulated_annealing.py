import random
from math import exp,dist

def simulated_annealing(state,base):
  initial_temp = 90
  final_temp = .1
  iterT = 0
  SAMax = 1000

  #define antes da primeira iteraçao o estado atual como o estado inicial
  current_temp = initial_temp
  current_state = state.copy()
  best_state = state.copy()

  x = open(f'{base}_results.txt','w')
  while current_temp > final_temp:
    for i in range(0,SAMax):
      #calcula a diferenca de custo do vizinho e avalia a entrada
      neighbor = get_neighbors(current_state)
      cost_diff = get_cost(neighbor) - get_cost(current_state)

      if cost_diff < 0:
        current_state = neighbor.copy()
        if get_cost(current_state) < get_cost(best_state):
          best_state = current_state.copy()
      else:
        try:
          heuristic = exp(- cost_diff / current_temp)
        except OverflowError:
          heuristic = float('inf')
        if random.uniform(0,1) < heuristic:
          current_state = neighbor.copy()

    #diminui a temperatura
    iterT += 1
    current_temp = reduce_temp(initial_temp,final_temp,iterT,SAMax)

    #escreve resultados
    x.write(f'{current_temp} {get_cost(current_state)}\n')


  return best_state

def reduce_temp(initial_temp,final_temp,iterT,SAmax):
  #calcula A
  new_temp = initial_temp * ( (final_temp/initial_temp)** ((iterT/SAmax)) )
  return new_temp

#Calcula a distancia total da solucao
def get_cost(state):
  cost = 0
  for i in range(0,len(state)-1):
    cost += dist(state[i][1],state[i+1][1])
  return cost

#Perturba a solucao fazendo no mínimo um swap e no máximo cinco, gerando um vizinho
def get_neighbors(state):
  neighbor = state.copy()
  #for i in range(5):
  index_a = random.randint(0,len(state) - 1)
  index_b = random.randint(0,len(state) - 1)
  neighbor[index_a],neighbor[index_b] = neighbor[index_b],neighbor[index_a] #swap

  return neighbor

def main():
  #carrega os dados e salva no array de cidades
  base = '100cities'
  #base = '100cities'
  f= open(f'{base}.txt','r')
  cities = []
  for row in f:
    cities.append([int(row.strip().split()[0]),(int(row.strip().split()[1]),int(row.strip().split()[2]))])

  #gera um estado inicial aleatorio
  initial_state = random.sample(cities,len(cities))

  #aplica o simulated_annealing
  f = open(f'{base}_runs.txt','w')
  for i in range (0,10):
    print(i)
    optimizedRoute = simulated_annealing(initial_state,base)
    print(get_cost(optimizedRoute))
    f.write(f'{get_cost(optimizedRoute)}\n')

if __name__ == "__main__":
  main()

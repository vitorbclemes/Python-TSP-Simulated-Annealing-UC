from math import sqrt
from matplotlib import pyplot as plt
from utils import load_convergence, load_runs
import pandas as pd
import seaborn as sns

base = "100cities"

iters, temps, dists = load_convergence(f'{base}_results.txt')

d = {"temp": temps, "Activation Function": dists, "Iteractions": iters}
df = pd.DataFrame(data=d)

sns.lineplot(data=df, x="Iteractions", y="Activation Function")

plt.savefig(f'Grafico de convergência - {base} ')

plt.clf()

runs = load_runs(f'{base}_runs.txt')

ax = sns.boxplot(x=runs)

ax.set(xlabel="Final Result")

plt.savefig(f'Boxplot - {base}')

# This file can be used to run simulations and generate data
# You need to choose "good" parameters and explain your choices
# I give two examples

from simulations import variable_proba_propagation, variable_burning_duration
from simulations import multiple_simulations
import matplotlib
import matplotlib.pyplot as plt


# Example of usage of variable_proba_propagation:
variable_proba_propagation(1000, 50, 5, list(x/10 for x in range(11)), 10000, False)
# May take 1-2min to complete with these parameters
# list(x/10 for x in range(11)) creates the list [0, 0.1, 0.2, ..., 1.0]
#i=list(x/10 for x in range(11))
#j=[]
#j.append(sum(nb_burnt_trees)/nb_simus)
#plt.plot(i,j)
#plt.show()




# Example of usage of variable_burning_duration:
#variable_burning_duration(1000, 50, list(range(1,12)), 0.2, 10000, False)
# May take 1-2min to complete with these parameters
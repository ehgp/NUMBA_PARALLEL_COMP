#implemented numba, comprehensive lists, and matplotlib graphing 'agg' method which is quicker
from numba import jit
from numba.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('agg')
import random
@jit
def dice(n):
    rolls = [random.randint(1, 6) + random.choices([1,2,3,4,5,6], [0.15, 0.15, 0.15, 0.15, 0.15, 0.25])[0] for i in range(n)]
    fair_rolls = [random.randint(1, 6) + random.choices([1,2,3,4,5,6], [0.15, 0.15, 0.15, 0.15, 0.15, 0.25])[0] - random.choices([1,2,3,4,5,6], [0.15, 0.15, 0.15, 0.15, 0.15, 0.25])[0] for i in range(n)]
    biased_rolls = [random.choices([1,2,3,4,5,6], [0.15, 0.15, 0.15, 0.15, 0.15, 0.25])[0] for i in range(n)]
    fig, axes = plt.subplots(3,1, figsize=(3,3), dpi=120,tight_layout=True)
    return axes[0].title.set_text('two dice rolls'),axes[0].hist(rolls, bins=np.arange(1+1, 12+2)-0.5),axes[1].title.set_text('fair die rolls'),axes[1].hist(fair_rolls, bins=np.arange(1, 6+2)-.5),axes[2].title.set_text('biased die rolls'),axes[2].hist(biased_rolls, bins=np.arange(1, 6+2)-.5),plt.show()

n1 = input("How many times will you roll?: ")
n1 = int(n1)
dice(n1)
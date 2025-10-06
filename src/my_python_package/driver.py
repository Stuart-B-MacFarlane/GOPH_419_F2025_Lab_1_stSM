# Author: Stuart MacFarlane
#Class: GOPH 419 F2025
#Proffesor: Brandon Karchewski

import numpy as np
import matplotlib.pyplot as plt
from functions import (
sqrt,
arcsin,
launch_angle_range,
)

def main ():
    ve_v0 = 2.0
    tol_alpha = 0.04
    alpha = np.arange(1, 1.25, 1.50, 1.75, 2, 2.25, 2.50, 2.75, 3.0)
    y = launch_angle_range(ve_v0,alpha,tol_alpha)
    plt.plot(alpha,y)
    plt.show()
    plt.savefig()

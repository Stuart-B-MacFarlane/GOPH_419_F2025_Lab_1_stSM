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
    tol_alpha = 0.02
    alpha = [0.25,0.30,0.35]
    min_phi = []
    max_phi = []
    i=0
    while (i< len(alpha)):
        print (alpha[i])
        print (len(alpha))
        range_phi = launch_angle_range(ve_v0,alpha[i],tol_alpha)
        min_phi.append (range_phi[0])
        max_phi.append (range_phi[1])
        print("test1")
        i = i+1
    print(min_phi)
    #y = [1,2,3,4,5,6,7,8,9]
    #plt.plot(alpha,min_phi,max_phi)
    #plt.show()

main()

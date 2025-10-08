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
    alpha = [0.10,0.15,0.2,0.25,0.30]
    min_phi = []
    max_phi = []
    i=0
    while (i< len(alpha)):
        print (alpha[i])
        print (len(alpha))
        range_phi = launch_angle_range(ve_v0,alpha[i],tol_alpha)
        min_phi.append (range_phi[0])
        max_phi.append (range_phi[1])
        print("test1","min_phi=",min_phi,"max_phi=",max_phi)
        i = i+1
    #print(min_phi)
    plt.plot(alpha,min_phi,max_phi)
    plt.title ("alpha values for fixed ve/v0 of 2, with alpha tolerance of 0.02")
    plt.show()
    
    




    
    alpha = 0.25
    tol_alpha = 0.04
    ve_v0 = [1.0,1.25,1.5,1.75,2.0]
    i = 0
    min_phi = []
    max_phi = []
    while (i<len(ve_v0)):
        print (ve_v0[i])
        print (len(ve_v0))
        range_phi = launch_angle_range(ve_v0[i],alpha,tol_alpha)
        min_phi.append (range_phi[0])
        max_phi.append (range_phi[1])
        print("test1","min_phi=",min_phi,"max_phi=",max_phi)
        i = i+1
    print (len(ve_v0))
    print (len(min_phi))
    print (len(max_phi))
    plt.plot(ve_v0,min_phi,max_phi)
    plt.show()
main()

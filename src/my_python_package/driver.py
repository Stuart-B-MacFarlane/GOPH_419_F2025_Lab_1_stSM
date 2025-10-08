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
    alpha = [0.01,0.025,0.05,0.075,0.10,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.30]
    min_phi = []
    max_phi = []
    i=0
    while (i< len(alpha)):
        #print (alpha[i])
        #print (len(alpha))
        range_phi = launch_angle_range(ve_v0,alpha[i],tol_alpha)
        min_phi.append (range_phi[0])
        max_phi.append (range_phi[1])
        #print("test1","min_phi=",min_phi,"max_phi=",max_phi)
        i = i+1
    #print(min_phi)
    plt.plot(alpha,min_phi, label="min_phi")
    plt.plot(alpha,max_phi, label ="max_phi")
    plt.title ("alpha values for fixed ve/v0 of 2, with alpha tolerance of 0.02")
    plt.xlabel("aplha")
    plt.ylabel("phi (radians)")
    plt.legend()
    #plt.savefig("test1.png")
    plt.show()
    
    
    




    
    alpha = 0.25
    tol_alpha = 0.04
    ve_v0 = [1.345,1.346,1.347,1.348,1.349,1.35,1.36,1.37,
             1.38,1.39,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,
             1.8,1.85,1.9,1.95,2.0,2.05,2.1,2.11,2.12,2.13,
             2.14,2.15]
    i = 0
    min_phi = []
    max_phi = []
    while (i<len(ve_v0)):
        #print ("ve_v0=",ve_v0[i])
        #print (len(ve_v0))
        range_phi = launch_angle_range(ve_v0[i],alpha,tol_alpha)
        min_phi.append (range_phi[0])
        max_phi.append (range_phi[1])
        #print("test1","min_phi=",min_phi,"max_phi=",max_phi)
        i = i+1
    #print (len(ve_v0))
    #print (len(min_phi))
    #print (len(max_phi))
    plt.plot(ve_v0,min_phi, label="min_phi")
    plt.plot(ve_v0,max_phi, label="max_phi")
    plt.title("Ve/v0 values for constant aplha of 0.25, and tol_alpha of 0.04")
    plt.xlabel("ve/v0")
    plt.ylabel("phi (radians)")
    plt.legend()
    #plt.savefig("test2.png")
    plt.show()
main()

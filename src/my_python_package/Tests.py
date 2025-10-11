# Author: Stuart MacFarlane
#Class: GOPH 419 F2025
#Profesor: Brandon Karchewski

import numpy as np
from functions import (
sqrt,
arcsin,
launch_angle,
launch_angle_range
)

def test_angle(ve_v0,alpha,tol_alpha):
    angle = launch_angle(ve_v0,alpha)
    angle_range = launch_angle_range(ve_v0,alpha,tol_alpha)
    expected_radicand = (1 -((alpha/(1+alpha))*(ve_v0**2)))   
    expected_sin = ((1+alpha)*np.sqrt(expected_radicand))
    expected_angle = np.arcsin(expected_sin)

    lower_alpha = alpha - tol_alpha
    lower_expected_radicand = (1 -((lower_alpha/(1+lower_alpha))*(ve_v0**2)))   
    lower_expected_sin = ((1+lower_alpha)*np.sqrt(lower_expected_radicand))
    lower_expected_angle = np.arcsin(lower_expected_sin)

    upper_alpha = alpha + tol_alpha
    upper_expected_radicand = (1 -((upper_alpha/(1+upper_alpha))*(ve_v0**2)))   
    upper_expected_sin = ((1+upper_alpha)*np.sqrt(upper_expected_radicand))
    upper_expected_angle = np.arcsin(upper_expected_sin)

    expected_angle_range =np.array([lower_expected_angle,upper_expected_angle])
    print ("Launch angle=",angle)
    print ("Expected angle=",expected_angle)
    print ("Launch angle range =",angle_range)
    print ("Expected angle range=",expected_angle_range,"\n")

def test_sqrt(x):
    test_x =sqrt(x)
    expected_x = np.sqrt(x)
    print (" x =",x,"\n sqrt x =",test_x,"\n expected sqrt x =",expected_x,"\n")

def test_arcsin(x):
    test_x =arcsin(x)
    expected_x = np.arcsin(x)
    print (" x =",x,"\n arcsin(x) =",test_x,"\n expected arcsin(x) =",expected_x,"\n")

def main():
    
    x = 0.5 
    test_sqrt(x)
    x = 2 
    test_sqrt(x)
    x = 0.2
    test_sqrt(x)

    x = 0.5 
    test_arcsin(x)
    x = 0.9 
    test_arcsin(x)
    x = 0.2
    test_arcsin(x)
    
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02
    print(" for ve_v0 =",ve_v0,"\n alpha =",alpha,"\n tol_alpha=",tol_alpha,"\n")
    test_angle(ve_v0,alpha,tol_alpha)

    ve_v0 = 3.0
    alpha = 0.50
    tol_alpha = 0.02
    print(" for ve_v0 =",ve_v0,"\n alpha =",alpha,"\n tol_alpha=",tol_alpha,"\n")
    test_angle(ve_v0,alpha,tol_alpha)
    
    ve_v0 = 1.5
    alpha = 0.2
    tol_alpha = 0.05
    print(" for ve_v0 =",ve_v0,"\n alpha =",alpha,"\n tol_alpha=",tol_alpha,"\n")
    test_angle(ve_v0,alpha,tol_alpha)
    
    
main()


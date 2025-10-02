# Author: Stuart MacFarlane
#Class: GOPH 419 F2025
#Proffesor: Brandon Karchewski

def sqrt(x):
    #Calculates the square root of a number
    #Parameters
    #--------
    # x: int or float
    #The number that will be square rooted
    #Returns
    #--------
    #int or float
    n = 0
    k = 0
    k_fact = 1
    k_prod = 1
    k_coef = 1
    
    
    xsqrt = 0
    if (x < 0) or (x > 2.5):
        print( "Radicand is outside of accepted range")
    else:
        if (x <= 0.75):
            a = 0.5
            asqrt = 0.707106781186548
        elif (x <= 1.25):
            a = 1.0
            asqrt = 1
        elif (x <= 1.75):
            a = 1.5
            asqrt = 1.22474487139159 
        else :
            a = 2.0
            asqrt = 1.4142135623731
        print ("a =",a, "and asqrd =",asqrt)
        h = x-a
        print ("h =",h)
        k_term = asqrt
        k_sum = asqrt
        eps_a = 1
    #while (n < 8):
        k=1
        k_fact = k_fact*(k+1)
        if k == 0:
            k_prod =1
        else:
            k_prod = k_prod*(-0.5*((2*k)-1))
        k_coef = 0.5*k_prod / k_fact
        print ("k=",k+1,"k_fact=",k_fact,"k_prod=",k_prod,"k_coef=",k_coef)
         
        
        




        

        
x = 0.25

sqrt(x)

    

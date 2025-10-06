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
        #Test for input in range
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
            #Assaign correct a value, making sure x is within 0.50 of a
        #print ("a =",a, "and asqrd =",asqrt)
        h = x-a
        #print ("h =",h)
        eps_a = 1
        k = 0
    while (eps_a > 5e-9):
        #set epsilon a target for stopping
        if k == 0:
            k_fact =1
            k_prod =1
            k_coef = 1
            k_term = asqrt
            k_sum = k_term
        else:
            if k ==1:
                k_prod = 1
            else:
                k_prod = k_prod*(-0.5*((2*(k-1))-1))
            k_fact = k_fact*(k)
            k_coef = 0.5*k_prod / k_fact
            k_term = ((h**k)/(asqrt**((2*k)-1)))*k_coef
            k_sum = k_sum + k_term
        eps_a = abs(k_term/k_sum)
        
        #print ("k=",k,"k_fact=",k_fact,"k_prod=",k_prod,"k_coef=",k_coef,"k_term=",k_term,"k_sum=",k_sum,"eps_a=",eps_a)
        k= k+1
        
def arcsin(x):
    print("arcsin")
    if x < 0 or x > 1:
        print ("x value outside of allowed range")
    else :
        n = 2
        n_fact = 1
        eps_a = 1
        m=0
        n_term = 0
        n_sum = 0
        while (eps_a > 5e-9):
            n_fact = n_fact*n
            n_2 = 2*n
            n2_fact = n_fact
            
            while not(n_2 == n):
                n2_fact = n2_fact*n_2
                print("n=",n,"n_2=",n_2)
                n_2 = n_2 - 1
            
            
            n_term = ((2*x)**(2*n)) / ((n**2)*((n2_fact)/(n_fact**2)))
            n_sum = n_sum + n_term
            eps_a = abs(n_term/n_sum)
            print (" n_sum=",n_sum,"eps_a=",eps_a)




        

        
#x = float (input("input x value"))
x= 0.5

#sqrt(x)
arcsin(x)
    

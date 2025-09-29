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
    if (x < 0) or (x > 2.5):
        print( "Radicand is outside of accepted range")
    else:
        if (x <= 0.75):
            a = 0.5
            asqrd = 0.707106781186548
        elif (x <= 1.25):
            a = 1.0
            asqrd = 1
        elif (x <= 1.75):
            a = 1.5
            asqrd = 1.22474487139159 
        else :
            a = 2.0
            asqrd = 1.4142135623731
        print ("a =",a, "and asqrd =",asqrd)
            

        
x = 1.75556

sqrt(x)

    

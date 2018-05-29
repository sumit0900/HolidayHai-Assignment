#################################
####function to get all prime 
################################


def getAllPrime(n):
    primeList = []
    for i in range(0,n+1):
        primeList.append(True)
    p = 2
    #### traverse loop upto squareroot of number n.
    while (p * p <= n):
        if (primeList[p] == True):
            demo = p * 2
            ##mark all no. to non prime which are multiple of current number. Current no. will be prime
            for i in range(demo, n+1, p):
                primeList[i] = False
        p += 1
    
    returnList = []
    
    ##Elemets having True in primeList are the prime no.s before number n
    
    for p in range(2, n):
        if primeList[p]:
            returnList.append(p)
            
    return returnList
 

if __name__=='__main__':
    n = int(input())
    print(getAllPrime(n))
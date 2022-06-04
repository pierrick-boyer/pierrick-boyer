""" Prime number if divisible by itself and greater than 2 """
def is_prime(nb):
    prime = True

    if nb < 2:
        prime = False

    for d in range(2, nb):
        if nb % d == 0:
            prime = False

    return prime


""" Prime number G if 2G + 1 and also a prime number """
def is_SG_prime(nb):
    if is_prime(nb) and is_prime(nb*2+1):
        return True
    else:
        return False


    
def get_prime_list(inf, sup):
    prime_list = []
    list_SG = []
    
    if inf < sup:
        
        for nb in range(inf, sup+1):
            
            if is_prime(nb):
                prime_list.append(nb)
            
            if is_SG_prime(nb):
                list_SG.append(nb)
                
    else:
        print('error')
        
    result = f"List of prime is {prime_list}, and list of G prime is {list_SG} in interval {inf, sup}"
    
    return result

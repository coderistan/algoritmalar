from math import sqrt

def find_prime(min_number,max_number):
    for i in range(min_number,max_number):
        if(i%2==0):
            continue
        else:
            find=True
            for k in range(min_number,int(sqrt(i))+1):
                if(i%k==0):
                    find=False
                    break
            if(find):
                yield i

print(sum(find_prime(2,2000000))+2)

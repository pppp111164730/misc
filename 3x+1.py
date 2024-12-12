#Collatz conjecture 
#note think about making this into graph


def threex(x):
    x = int(x)
    while x != 1:
        if (x%2) == 1:
            x = 3*x + 1
            print(x)
        else:
            x = x//2
            print(x)

if __name__ == "__main__":
    threex(11)



"""
Posible idea 
two arrays one with numbers and one with null
run through numbers and assign their result to null
make graph out of the two arrays
"""
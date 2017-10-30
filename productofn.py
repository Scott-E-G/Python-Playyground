x = 1
prod = 1
n = input("Please enter a positive, non zero integer: ")
#while x != n:
#    prod = x * prod
#    x = x + 1
#prod = prod * n
for x in range(1, n+1):
    prod = x * prod
    print (prod)
print('Your total is ' + str(prod))
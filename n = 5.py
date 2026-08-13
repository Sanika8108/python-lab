n = 5

for i in range(1, n + 1):
    print("* " * i)
    
print("-----------------------")
    
n = 5

for i in range(n, 0, -1):
    print("* " * i)
    
print("-------------------------")
    
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
print("------------------------------------------------------------------------------------------")
    
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
    
print("----------------------------")

n = 5

for i in range(n):
    print("* " * n)
print("----------------------------")
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("----------------------------")
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print("----------------------------")
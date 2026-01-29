# rows = 4
# for i in range(1, rows + 1):
#     for j in range (1, i+1):
#         print("* ", end="")
#     print()


# rows = 4
# for i in range(1, rows+1 ):
#     for j in range (1, i+1):
#         print(j, end=" ")
#     print()


# rows = 4
# for i in range(1, rows + 1):
#     for j in range (i, 0, -1):
#         print(j, end=" ")
#     print()


# for i in range(1, 6):
#     print(" * " *i)


# rows = 4
# for i in range(1, rows + 1):
#     for j in range (i):
#         print(i, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# for i in range (1 , 5):
#     for j in range (i):
#         print("*", end=" ")
#     print()    

# for i in range(1,5):
#     for j in range (5 - i, 0, -1):
#         print(j, end=" ")
#     print()    

# for i in range(1, 5):
#     for j in range (1, 1 + i):
#         print("*", end=" ")
#     print()
# rows = 4
# for i in range(1, rows + 1):
#     if i == 1:
#         print("  *  ")
#     else:
#         print(" "* (rows - i ) + "* "*i)


# for i in range(1,5):
#     spaces = 4 - i - (i == 1)
#     stars = 2 * i - 1
#     print(" " * spaces + "* " * stars)        


# for i in range(1, 5):
#     spaces = 4 - i 
#     stars = i - 1
#     print(" " * spaces + "* " * stars)


# rows = 4
# for i in range(rows):
#     for k in range (i):
#         print (" ", end=" ")
#     for j in range (rows - i):
#         print("*", end=" ")
#     print()
# 
    
# rows = 4    
# for i in range(rows):
#     print(" " * i + "*" * (rows - i))


# for i in range(1, 7):
#     spaces = 4 - i - (i == 1)
#     stars = i 
#     print(" " * spaces + "* " * stars)


# for i in range(1,5):
#     for j in range(1,i + 1):
#         print(" *", end="")
#     print()    

# for i in range(1,5):
#     spaces = 4 - i - (i == 1)
#     stars= i
#     print(" " * spaces + "* " * stars)    


# for i in range(1,5):
#     spaces = 4 - i - (i == 1)
#     stars = 2 * i - 1
#     print(" " * spaces + "* " * stars)        


# for i in range(1,5):
#     print("*" * i)
# for i in range(4-1, 0, -1):
#     print("*" * i)

for i in range(1,5):
    for j in range(1,i + 1):
        print(j , end="" )
    print()    
for i in range(4-1, 0, -1):
    for j in range(1 , i + 1):
        print(j , end="")
    print()    
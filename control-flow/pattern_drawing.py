square_length = int(input("Enter the size of the pattern:"))
size = 0
while size < square_length:
    
    for i in range(square_length):
        print("*", end="")
    print()
    size += 1
    

def add(a):  # recursive function, if no limits then ends due to python built in limit so the program doesn't crash
    a += 1
    print(a)
    if a < 10:  # ends due to if statement
        add(a)
add(1)
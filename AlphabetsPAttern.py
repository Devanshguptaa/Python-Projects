def print_A():
    for row in range(7):
        for col in range(7):
            if (col == 0 and row != 0) or (col == 6 and row != 0) or (row == 0 and col > 0 and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()



def print_B():
    for row in range(7):
        for col in range(7):
            if (col == 0 or (col == 6 and row != 0 and row != 3 and row != 6) or (row == 0 or row == 3 or row == 6) and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_C():
    for row in range(7):
        for col in range(7):
            if (col == 0 and (row != 0 and row != 6)) or (row == 0 or row == 6) and (col > 0 and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_D():
    for row in range(7):
        for col in range(7):
            if (col == 0 or (col == 6 and row != 0 and row != 6) or (row == 0 or row == 6) and col > 0 and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_E():
    for row in range(7):
        for col in range(7):
            if (col == 0 or row == 0 or row == 3 or row == 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_F():
    for row in range(7):
        for col in range(7):
            if (col == 0 or row == 0 or row == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_G():
    for row in range(7):
        for col in range(7):
            if (col == 0 and (row != 0 and row != 6)) or (col == 6 and (row != 1 and row != 2 and row != 5)) or (row == 0 or row == 6) and (col > 0 and col < 6) or (row == 3 and col > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_H():
    for row in range(7):
        for col in range(7):
            if (col == 0 or col == 6 or row == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_I():
    for row in range(7):
        for col in range(7):
            if (row == 0 or row == 6 or col == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_J():
    for row in range(7):
        for col in range(7):
            if (row == 0 or col == 3 or (row == 6 and col > 0 and col < 3)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_K():
    for row in range(7):
        for col in range(7):
            if (col == 0 or (row == col and col > 2) or (row + col == 6 and col > 2)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_L():
    for row in range(7):
        for col in range(7):
            if (col == 0 or row == 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_M():
    for row in range(7):
        for col in range(7):
            if (col == 0 or col == 6 or (row == col and col > 0 and col < 4) or (row + col == 6 and col > 2 and col < 6)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_N():
    for row in range(7):
        for col in range(7):
            if (col == 0 or col == 6 or row == col):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_O():
    for row in range(7):
        for col in range(7):
            if (col == 0 and (row != 0 and row != 6)) or (col == 6 and (row != 0 and row != 6)) or (row == 0 or row == 6) and (col > 0 and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_P():
    for row in range(7):
        for col in range(7):
            if (col == 0 or (row == 0 or row == 3) and col < 6) or (col == 6 and (row == 1 or row == 2)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_Q():
    for row in range(7):
        for col in range(7):
            if (col == 0 and (row != 0 and row != 6)) or (col == 6 and (row != 0 and row != 6)) or (row == 0 or row == 6) and (col > 0 and col < 6) or (row == 4 and col == 5):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_R():
    for row in range(7):
        for col in range(7):
            if (col == 0 or (row == 0 or row == 3) and col < 6) or (col == 6 and (row == 1 or row == 2)) or (row - col == 3 and col > 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_S():
    for row in range(7):
        for col in range(7):
            if (row == 0 or row == 3 or row == 6) or (col == 0 and row < 3) or (col == 6 and row > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_T():
    for row in range(7):
        for col in range(7):
            if (row == 0 or col == 3):
              
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_U():
    for row in range(7):
        for col in range(7):
            if (col == 0 and row != 6) or (col == 6 and row != 6) or (row == 6 and (col > 0 and col < 6)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_V():
    for row in range(7):
        for col in range(7):
            if (col == row or col + row == 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_W():
    for row in range(7):
        for col in range(7):
            if (col == 0 or col == 6 or (row == 6 and (col > 0 and col < 6)) or (row == col and col > 2) or (row + col == 6 and col > 2)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_X():
    for row in range(7):
        for col in range(7):
            if (col == row or col + row == 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_Y():
    for row in range(7):
        for col in range(7):
            if ((row < 4 and col == row) or (col + row == 6 and col < 4)) or (row >= 4 and col == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_Z():
    for row in range(7):
        for col in range(7):
            if (row == 0 or row == 6 or row + col == 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_alphabet(alphabet):
    if alphabet == 'A':
        print_A()
    elif alphabet == 'B':
        print_B()
    elif alphabet == 'C':
        print_C()
    elif alphabet == 'D':
        print_D()
    elif alphabet == 'E':
        print_E()
    elif alphabet == 'F':
        print_F()
    elif alphabet == 'G':
        print_G()
    elif alphabet == 'H':
        print_H()
    elif alphabet == 'I':
        print_I()
    elif alphabet == 'J':
        print_J()
    elif alphabet == 'K':
        print_K()
    elif alphabet == 'L':
        print_L()
    elif alphabet == 'M':
        print_M()
    elif alphabet == 'N':
        print_N()
    elif alphabet == 'O':
        print_O()
    elif alphabet == 'P':
        print_P()
    elif alphabet == 'Q':
        print_Q()
    elif alphabet == 'R':
        print_R()
    elif alphabet == 'S':
        print_S()
    elif alphabet == 'T':
        print_T()
    elif alphabet == 'U':
        print_U()
    elif alphabet == 'V':
        print_V()
    elif alphabet == 'W':
        print_W()
    elif alphabet == 'X':
        print_X()
    elif alphabet == 'Y':
        print_Y()
    elif alphabet == 'Z':
        print_Z()

alphabet_choice = input("Enter an alphabet (A-Z): ")
print()

print_alphabet(alphabet_choice.upper())

-------------------------------------------------------------------------shift+Enter----------------------------------------------------------------------

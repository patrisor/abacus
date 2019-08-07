# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    abacus.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/07/23 13:16:09 by patrisor          #+#    #+#              #
#    Updated: 2019/08/02 15:56:46 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
ABACUS
'''
# Logic to slide any part of the abacus
def slide(l, inp):
    if inp == "d":
        if l[0] == 0:
            return False
        l.pop(0)
        l.append(1)
    if inp == "a":
        if l[len(l) - 1] == 0:
            return False
        l.pop(len(l) - 1)
        l.insert(0, 1)
    return True

# Logic to slide any part of the abacus
def update_abacus(a, r, c):
    l = a[r + c]
    while True:
        print_abacus(a)
        inp = input("Slide the Abacus: [a or d] \n")
        die(inp)
        if inp != "a" and inp != "d":
            print("Invalid Input. Try Again")
            continue
        slide(l, inp)
    return True

''' TODO: Update Abacus to look like this
====================================================
||  .                  .  .  .  .  .  .  .  .  .  ||
||-( )----------------( )( )( )( )( )( )( )( )( )-||
||  "                  "  "  "  "  "  "  "  "  "  ||
||  .  .                  .  .  .  .  .  .  .  .  ||
||-( )( )----------------( )( )( )( )( )( )( )( )-||
||  "  "                  "  "  "  "  "  "  "  "  ||
||  .  .  .                  .  .  .  .  .  .  .  ||
||-( )( )( )----------------( )( )( )( )( )( )( )-||
||  "  "  "                  "  "  "  "  "  "  "  ||
||  .  .  .  .                  .  .  .  .  .  .  ||
||-( )( )( )( )----------------( )( )( )( )( )( )-||
||  "  "  "  "                  "  "  "  "  "  "  ||
||  .  .  .  .  .                  .  .  .  .  .  ||
||-( )( )( )( )( )----------------( )( )( )( )( )-||
||  "  "  "  "  "                  "  "  "  "  "  ||
||  .  .  .  .  .  .                  .  .  .  .  ||
||-( )( )( )( )( )( )----------------( )( )( )( )-||
||  "  "  "  "  "  "                  "  "  "  "  ||
||  .  .  .  .  .  .  .                  .  .  .  ||
||-( )( )( )( )( )( )( )----------------( )( )( )-||
||  "  "  "  "  "  "  "                  "  "  "  ||
||  .  .  .  .  .  .  .  .                  .  .  ||
||-( )( )( )( )( )( )( )( )----------------( )( )-||
||  "  "  "  "  "  "  "  "                  "  "  ||
||  .  .  .  .  .  .  .  .  .                  .  ||
||-( )( )( )( )( )( )( )( )( )----------------( )-||
||  "  "  "  "  "  "  "  "  "                  "  ||
||  .  .  .  .  .  .  .  .  .  .                  ||
||-( )( )( )( )( )( )( )( )( )( )-----------------||
||  "  "  "  "  "  "  "  "  "  "                  ||
====================================================
'''
def print_abacus(a):
    for r in range(0, len(a), 2):
        print(str(int(r / 2)) + " || " + ' '.join(str(b) for b in a[r]) + " | " + ' '.join(str(c) for c in a[r + 1]))

'''
USER_INPUTS
'''
# Processes input at any point during the program and kills it if it gets "q" byte.
def die(i):
    if i == "q":
        print("Goodbye!")
        exit(-1)

# Helper function to check the numbers in two other functions
def check_num(inp, n1, n2):
    if inp.isalpha() or int(inp) > n2 or int(inp) < n1:
        print("Invalid Input. Try Again")
        return False
    return True

# Chooses the Row
def choose_row():
    while True:
        inp = input("Which row would you like to play with? [0 - 6]\n")
        die(inp)
        if not check_num(inp, 0, 6):
            continue
        return int(inp)

# Chooses the Upper or Lower Beads
def upper_or_lower():
    while True:
        inp = input("Upper or Lower beads? [0 or 1] \n")
        die(inp)
        if not check_num(inp, 0, 1):
            continue
        return int(inp)

'''
MAIN_PROGRAM 
'''
if __name__ == "__main__":
    abacus = (([(([1] * 5) + ([0] * 3))] + [[0, 1]]) * 7)
    while True:
        print_abacus(abacus)
        row = choose_row() 
        u_or_l = upper_or_lower()
        update_abacus(abacus, row, u_or_l)

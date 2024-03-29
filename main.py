import os
'''
ABACUS
'''
def print_abacus(abacus):
    x = ("=" * 83) + "\n"
    for row in range(len(abacus)):
        for i in range(3): # Construct Row of Abacus from left to right
            x += '||'
            for col in abacus[row]: # At each drawing, it scans over the list once again from left to right
                if i == 0: # BUILDS the tops portion of the string
                    x += ("      " if col == 0 else "  .-. ")
                if i == 1: 
                    x += ("------" if col == 0 else "-(   )")
                if i == 2:
                    x += ("      " if col == 0 else "  '-' ")
            if row == len(abacus):
                x += " || "
                break
            x += (" ||\n" if i == 0 or i == 2 else "-||\t" + str(row) + "\n")
    x += ("=" * 83)
    print(x)

# Logic to slide any part of the abacus
def slide(l, inp):
    os.system("afplay sounds/click_sound.wav")
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

def calculate_abacus(abacus):
  ret = 0
  units = 1
  for row in range(len(abacus)):
    for col in range(len(abacus[row]) - 1, -1, -1):
      if abacus[row][col] == 0:
        break
      if abacus[row][col] == 1:
        ret = ret + units
    units = units * 10
  return(ret)

'''
USER INPUT
'''
def die(x):
  if x == "q":
    print("Goodbye!")
    exit(-1)

def update_abacus(abacus):
  while True:
      inp = input("Slide the List using [a, d]. Click 'f' when finished.\n")
      die(inp)
      if not slide(abacus[row], inp):
        print("Already gone far enough this way! Try the other way")
        continue
      if inp == 'f':
        break
      if ((inp != 'a' and inp != 'd' and inp != 'f') or (not inp.isalpha())):
        print("Invalid Input. Try Again.")
        continue
      print_abacus(abacus)
      print("NUMBER: " + '{:,}'.format(int(calculate_abacus(abacus))) + "\n")

def choose_row():
  while True:
    inp = input("Choose Row:\n")
    die(inp)
    if inp.isalpha() or int(inp) > 9 or int(inp) < 0:
      print("Invalid input. Try again.")
      continue
    return int(inp)

def title():
  print("         888")
  print("         888")
  print("         888")
  print(" 8888b.  88888b.   8888b.   .d8888b 888  888 .d8888b")
  print("    '88b 888 '88b     '88b d88P'    888  888 88K")
  print(".d888888 888  888 .d888888 888      888  888 'Y8888b.")
  print("888  888 888 d88P 888  888 Y88b.    Y88b 888      X88")
  print("'Y888888 88888P'  'Y888888  'Y8888P  'Y88888  88888P'\n")

def intro():
  title()
  while True:
    inp = input("Welcome. Enter a number to get the visual representation of it, else enter [i] for an interactive display:\n")
    die(inp)
    if ((not inp.isalpha() and int(inp) < 0) or (inp.isalpha() and inp != 'i')):
      print("Invalid input. Try again.")
      continue
    return inp

def process_input(abacus, ret):
  units = [int(d) for d in str(ret)]
  units.reverse()
  if len(units) > 10:
    print("Number Too Large.")
    exit(-1)
  ''' Remove Trailing Zeros
  while units[-1] == 0:
    units.pop[-1] '''
  for j in range(len(units) - 1, - 1, - 1):
    for i in range(units[j]):
      slide(abacus[j], 'd')

'''
MAIN FUNCTION
'''
if __name__ == "__main__":
  abacus = [([1] * 10) + ([0] * 3) for _ in range(10)]
  ret = intro()
  if not ret.isalpha():
    process_input(abacus, ret)
    print_abacus(abacus)
    exit(0)
  print_abacus(abacus)
  while True:
    row = choose_row()
    update_abacus(abacus)
  exit(0)

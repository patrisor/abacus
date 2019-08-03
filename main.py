'''
ABACUS
'''
# TODO: Update
def print_abacus(abacus):
  units = 1
  print('\n' + ('-' * 31))
  for l in range(len(abacus)):
    print(str(l) + ' |-' + ('-'.join(str(e) for e in abacus[l])) + '-| ' + '{:,}'.format(units) + 's')
    units *= 10
  print('-' * 31)

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
      print("NUMBER: " + '{:,}'.format(int(calculate_abacus(abacus))))

def choose_row():
  while True:
    inp = input("Choose Row:\n")
    die(inp)
    if inp.isalpha() or int(inp) > 9 or int(inp) < 0:
      print("Invalid input. Try again.")
      continue
    return int(inp)

def intro():
  while True:
    inp = input("Welcome to my Abacus. Enter a number to get the visual representation of it, else enter [i] for an interactive display:\n")
    die(inp)
    if ((not inp.isalpha() and int(inp) < 0) or (inp.isalpha() and inp != 'i')):
      print("Invalid input. Try again.")
      continue
    return inp

# TODO: Fix Bugs
def process_input(abacus, ret):
  units = [int(d) for d in str(ret)]
  if len(units) > 10:
    print("Number Too Large.")
    exit(-1)
  ''' Remove Trailing Zeros
  while units[-1] == 0:
    units.pop[-1] '''
  '''
  for i in range(len(abacus)):
    if i == len(units):
      break
      '''
  # Soft copy l[::-1]; Hard copy l.reverse()
  for j in range(len(units) - 1, - 1, - 1):
    for i in range(units[j]):
      print(units[j])
      slide(abacus[j], 'd')
  print(units)

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

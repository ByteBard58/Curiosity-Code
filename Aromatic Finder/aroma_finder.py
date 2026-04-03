"""
Aromatic finder

A fun little terminal-based Python program that determines whether 
a compound is *Aromatic* or *Aliphatic* based on its pi electron count and charge state 
— using Hückel's Rule.

"""

def smart_div(x,y) -> str:
  if x%y == 0:
    return "integer"
  if x%y != 0:
    return "float"

def huckel(pi_es:int,charged:bool) -> str:
    '''
    Independent function for actual calculation
    '''
    n:str = smart_div(pi_es-2,4)
    if n == "integer" and charged:
      return "aromatic"
    elif n == "integer" and not charged:
      return "unconfirmed"
    elif n == "float":
      return "aliphatic"

def main() -> None:
  '''
  The CLI code
  '''
  print("Welcome to Aromatic Finder")
  print("Just input the total number of pi electorns in the " \
  "compound and the charge state of the compound, this program will do the rest :)")
  print("Info: Input 000 to exit")
  while True:
    try:
      pi_es:str = input("Please provide the total number of pi " \
      "electrons in the molecule (input 000 to exit): ")
      if pi_es == "000":
        print("Exitting....")
        break
      pi_es:int = int(pi_es)
    except ValueError:
      print("Please provide a number, not anything else")
      continue
    while True:
      ion :str= input("Please provide the charge " \
      "state of the compound (input 'i' if charged, _ if neutral): ")
      if ion not in ["i","I","_"]:
        print("Please provide the state in the following way without space:"
        " 'i' or 'I' if the compound is charged, _(underscore) if the compound is neutral")
        continue
      else:
        break
    result = huckel(pi_es=pi_es,charged=True if ion in ["i","I"] else False)
    if result in ["aliphatic","aromatic"]:
      print(f"Calculated Type: {result}")
    elif result == "unconfirmed":
      print("According to the calculation, the compound should be Aromatic." \
      " BUT, this program can not determine whether the compound shows resonance or not.")
      print("So, this program is unable to completly find out " \
      "whether the compound is aromatic or aliphatic.")
    else:
      print("Something went wrong")

main()
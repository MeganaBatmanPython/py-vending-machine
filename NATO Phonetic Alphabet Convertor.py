NATO={'A':'Alfa',
      'B':'Bravo',
      'C':'Charlie',
      'D':'Delta',
      'E':'Echo',
      'F':'Foxtrot',
      'G':'Golf',
      'H':'Hotel',
      'I':'India',
      'J':'Juliett',
      'K':'Kilo',
      'L':'Lima',
      'M':'Mike',
      'N':'November',
      'O':'Oscar',
      'P':'Papa',
      'Q':'Quebec',
      'R':'Romeo',
      'S':'Sierra',
      'T':'Tango',
      'U':'Uniform',
      'V':'Victor',
      'W':'Whiskey',
      'X':'X-ray',
      'Y':'Yankee',
      'Z':'Zulu',
      ' ':' '}
name=input("What is your name?")
name=name.upper()
alpha=[]
for item in name:
    converted_name=NATO[item]
    alpha.append(converted_name)
print(alpha)

print("This is your name in the NATO phonetic alphabet.")
import random
from random import choice

bosh = '123456'
characters = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
symbols = '!<>^&(),/|*'
yes = '123'
def main():
    print("Password generator")
    i = True
    while i:
        user = input("Enter 'Y' to generate or 'N' to exit: ")
        if user.upper() == "Y":
            i = False
            generate()
        elif user.upper() == 'N':
            i = False
        else:
            print("Not 'Y' or 'N'")
            continue

def generate():
    set1_5 = []
    set2_5 = []
    set3_5 = []
    set0 = []
    for x in yes:
        for x in bosh:
            randletternum = random.randint(0,25)
            randletter = characters[randletternum]
            set1_5.append(randletter)
            set1_6 = ' '.join(set1_5)
            set1 = set1_6.replace(' ', '')
            set1 = (''.join(choice((str.upper, str.lower))(c) for c in set1))
        for x in bosh:
            randnumnum = random.randint(0,9)
            randnum = numbers[randnumnum]
            set2_5.append(randnum)
            set2_6 = ' '.join(set2_5)
            set2 = set2_6.replace(' ', '')
        for x in bosh:
            randsymnum = random.randint(0,9)
            randsym = symbols[randsymnum]
            set3_5.append(randsym)
            set3_6 = ' '.join(set3_5)
            set3 = set3_6.replace(' ', '')
        set6 = set2 + set1 + set3
    for i in yes: 
        set0.append(''.join(random.sample(set6, 5)))
    set0.insert(1, '-')
    set0.insert(3, '-')
    set0 = (''.join(choice((str.upper, str.lower))(c) for c in set0))
    print(set0)

main()
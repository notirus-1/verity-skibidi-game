import sys
# set correct list
def verity_check(list1, list2):
    return list1 == list2
verities = ['verity', 'verity', 'verity', 'falsity', 'obesity', 'cruelty']
guesses = []
guess_index = 0
# take input
while True:
    print('come on guess!!!')
    if verity_check(verities, guesses):
        print('you won!!')
        sys.exit()    
    else:
        length = len(guesses)
        normal = length + 1
        verityguess = input().lower()
        if guess_index < len(verities) and verityguess == verities[guess_index]:
            print(f'you got {normal} correct!!')
            guesses.append(verityguess)
            guess_index += 1
            continue
        else:
            print('you got it all wrong!!!')

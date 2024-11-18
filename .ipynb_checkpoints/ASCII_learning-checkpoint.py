import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def flashcard_0b(let):
    print(let)
    answer = input("Translate to 0b")
    correct_answer = bin(ord(let))[2:].zfill(8)
    if(answer == correct_answer):
        print("True")
    else:
        print("False, it's " + correct_answer)

def flashcard_0d(let):
    print(let)
    answer = input("Translate to 0d")
    correct_answer = str(ord(let))
    if(answer == correct_answer):
        print("True")
    else:
        print("False, it's " + correct_answer)

def flashcard_0x(let):
    print(let)
    answer = input("Translate to 0x")
    correct_answer = str(hex(ord(let))[2:])
    if(answer == correct_answer):
        print("True")
    else:
        print("False, it's " + correct_answer)

def flashcards_deck_0d():
    while(True):
        letter = random.choice(letters)
        flashcard_0d(letter)
        cont = input("Continue? [y/n]").strip()
        if cont.lower() in ['n', 'no']:
            break

def flashcards_deck_0x():
    while(True):
        letter = random.choice(letters)
        flashcard_0x(letter)
        cont = input("Continue? [y/n]").strip()
        if cont.lower() in ['n', 'no']:
            break

def flashcards_deck_0b():
    while(True):
        letter = random.choice(letters)
        flashcard_0b(letter)
        cont = input("Continue? [y/n]").strip()
        if cont.lower() in ['n', 'no']:
            break
            
def ASCII_learning():
    print("Hello Anon! This application will make your brain automatically read ASCII codes as letters which will make you able to understand the OMNISSIAH words. Be dutiful and learn well.")
    while(True):
        ans = input("MENU: \nFlashcards:\n1 Learn 0d\n2 Learn 0b\n3 Learn 0x\n\nType in the number of activity")
        if ans.lower() == 'exit':
            break
        if ans == '1':
            flashcards_deck_0d()
        elif ans == '2':
            flashcards_deck_0b()
        elif ans == '3':
            flashcards_deck_0x()
        else:
            print("Wrong answer\nIf you want to leave, type 'exit'")

ASCII_learning()
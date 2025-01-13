import random

list_pileface = ['pile', 'face']
list_ouinon = ['oui', 'non']
points = 0
winstreak = 0


while True:
    print("Voulez-vous jouer ?")
    reponse = input("oui ou non ?")
    if reponse not in list_ouinon:
        print("OUI ou NON")
    elif reponse == "non":
        break
    else :
        flip = input("Pile ou Face ?").strip().lower()

        if flip in list_pileface:
            
            generated_word = (random.choice(list_pileface))
            print(f"La pièce est tombée sur : {generated_word}")

            if generated_word == flip:
                print("Bravo ! +1 Points !")
                points += 1
                winstreak += 1

            if generated_word != flip:
                print("Dommage :(")     
                winstreak = 0

            print(f"Votre score est de : {points}")
            print(f"Votre Winstreak est de : {winstreak}")

        else :
            print("NON")

print("Bye!")
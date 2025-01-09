# Jeu pile ou face
# To do :
# - GUI + Animation de coinflip
import random

list = ['pile', 'face']
points = 0
winstreak = 0

while True:
    print("Voulez-vous jouer ?")
    reponse = input("oui ou non ?")

    if reponse == "non":
        break
    
    flip = input("Pile ou Face ?")
    generated_word = (random.choice(list))
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

print("Bye!")
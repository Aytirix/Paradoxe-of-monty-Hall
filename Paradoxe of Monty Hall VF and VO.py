import random
#Problème de monty hall
print("\n\n\n\n\n")
print("English = 1")
print("Français = 0")
langage = 0
langage = int(input("--> "))
if langage == 0:
    print("\n\n\n\n\n")
    print("Bienvenue dans le paradoxe de Monty Hall")
    print("Situation initiale:")
    print("1. Vous êtes sur un plateau télévisé, le commentateur vous demdande de choisir une de ces 3 portes:")
    print("╔═════╦═════╦═════╗")
    print("║     ║     ║     ║")
    print("╠  1  ╠  2  ╠  3  ║") 
    print("║     ║     ║     ║")
    print("╚═════╩═════╩═════╝")
    print("2. Le commentateur va vous montrez une porte qui n'est pas la bonne")
    print("3.Il vous laisse encore une chance et vous demande si vous voulez changez de porte ou non")
    print("4.Pensez-vous avoir plus de chance de ganger en changeant de porte au deuxième tour ?")
    print("\n")
    print("à la fin du teste, vous aurez les résultas en pourcentage du taux de victoire de si vous changez de porte ou non")
    nombre_de_tours = int(input("Combien de tours de jeu voulez-vous ? "))
elif langage == 1:
    print("Welcome to the Monty Hall Paradox")
    print("Welcome to the Monty Hall paradox")
    print("Initial situation:")
    print("1. You are on a TV set, the commentator asks you to choose one of these 3 doors:")
    print("╔═════╦═════╦═════╗")
    print("║     ║     ║     ║")
    print("╠  1  ╠  2  ╠  3  ║") 
    print("║     ║     ║     ║")
    print("╚═════╩═════╩═════╝")
    print("2. the commentator will show you a door that is not the right one")
    print("3.he gives you one more chance and asks you if you want to change the door or not")
    print("4.do you think you have a better chance of winning by changing doors in the second round?")
    print("\n")
    print("at the end of the test, you will have the results in percentage of the win rate of whether you change the door or not")
    nombre_de_tours = int(input("How many turns do you want to play? "))
else:
    print("Vous avez entrez un nombre autre que 0 ou 1")
    print("You have entered a number other than 0 or 1")
    exit()
compteur_avec_changement_de_porte = 0
compteur_sans_changer_de_porte = 0
for boucle in range(0,nombre_de_tours):
    #On initialise les variables
    gain = ["perdu", "gagné","perdu "]
    #attribuer les gains a chaque porte aléatoirement et le supprimer de la liste
    dict = {1:"",2:"",3:""}
    for i in range(1,4):
        dict[i] = random.choice(gain)
        gain.remove(dict[i])
    porte_choisie = random.choice(list(dict.keys()))
    #si la porte choisie est la bonne, on supprime une porte perdu et pas celle qu'il y a dans porte_choisie
    if dict[porte_choisie] == "gagné":
        for b in range(1,4):
            if dict[b] == "perdu":
                del dict[b]
                compteur_sans_changer_de_porte = compteur_sans_changer_de_porte+1
    elif dict[porte_choisie] == "perdu":
        for b in range(1,4):
            if dict[b] == "perdu ":
                del dict[b]
                compteur_avec_changement_de_porte = compteur_avec_changement_de_porte+1
    elif dict[porte_choisie] == "perdu ":
        for b in range(1,4):
            if dict[b] == "perdu":
                del dict[b]
                compteur_avec_changement_de_porte = compteur_avec_changement_de_porte+1
    #calculer en pourcentage le ratio de gain/perte si on change de porte ou non

pourcentage_avec_changement_de_porte = (compteur_avec_changement_de_porte/nombre_de_tours)*100
pourcentage_sans_changer_de_porte = (compteur_sans_changer_de_porte/nombre_de_tours)*100
if langage == 0 :
    print("\n-----------------------")
    print("-----  RÉSULTATS  -----")
    print("-----------------------\n")
    print("Si vous changez votre porte au deuxième tour, vous avez " + str(round(pourcentage_avec_changement_de_porte,5)) + " % " + "de chances de gagner.") 
    print("Si vous ne changez pas de porte au deuxième tour, vous avez " + str(round(pourcentage_sans_changer_de_porte,5)) + " % " + "de chances de perdre.")
    print("On peut en conclure qu'on a plus de chance de gagner si on change de porte au deuxième tour.")
    print("Ce test à été réalisé " + str(nombre_de_tours) + " fois.")
    print("pour avoir un résultat cohérent, il faut que le nombre de tours soit élevé !\n")
elif langage == 1:
    print("\n-----------------------")
    print("-----  RESULTS  -----")
    print("----------------------\n")
    print("If you change your door in the second round, you have " + str(round(pourcentage_avec_changement_de_porte,5)) + " % " + "chances to win.")
    print("If you don't change doors in the second round, you have " + str(round(pourcentage_sans_changer_de_porte,5)) + " % " + "chances of losing.")
    print("We can conclude that we have a better chance of winning if we change doors in the second round.")
    print("This test has been performed " + str(nombre_de_tours) + " times.")
    print("to have a coherent result, the number of turns must be high !")
import os
import pickle
os.chdir('C:/Users/user/Documents/Python/Pendu')

#chargement des mots à jouer
with open ('Mots_a_8_caracteres.txt','r') as fichier :
    liste_mots = fichier.read()
liste_mots = liste_mots.split(",\n")

#tirage du mot au hasard
from random import choice
mot = choice(liste_mots)

#Proposition du RAZ de la liste des joueurs
print('Bienvenue dans le jeu "Pendu"')
with open ('scores','rb') as fichier :
    mon_depickler = pickle.Unpickler(fichier)
    liste_joueurs = mon_depickler.load()
if liste_joueurs =={} :
    print("Vous êtes le premier joueur !")
    joueur_actuel = input("Saisissez votre prenom : ")
    liste_joueurs[joueur_actuel] = [0,0]
    
else :
    test = input ("Si vous souhaitez effacer tous les joueurs participants, tapez 'Y', sinon 'N' : ")
    if test == 'Y' :
        liste_joueurs ={}
        with open ('scores','wb') as fichier :
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(liste_joueurs)
        joueur_actuel = input("Saisissez votre prenom : ")
        liste_joueurs[joueur_actuel] = [0,0]
    else :
        #identification du joueur
        test = False
        print ("Joueurs paticipants :")    
        for cle in liste_joueurs.keys() :
            print (cle)
        joueur_actuel = input("Saisissez votre prenom : ")
        for cle in liste_joueurs.keys() :
            if joueur_actuel == cle :
                test = True
                print ("Vous avez déjà participé. Votre dernier score est {0} pour {1} jeux".format(liste_joueurs[cle][1],liste_joueurs[cle][0]))
        if test == False :
            liste_joueurs[joueur_actuel] = [0,0]
            print("Vous êtes un nouveau participant. Votre score est 0")
mot_screen = '........'
print ('Le mot à deviner : ', mot_screen)

#lancement des essais
essai = 1
while essai < 9 :
    if essai < 4 :
        lettre = input("Essai {}. Tapez une lettre du mot en majuscule : ".format(essai))
        i = 0
        while i < 8 :
            if mot[i] == lettre :
                mot_screen = mot_screen[0:i]+lettre+mot_screen[i+1:8]
            i+=1
        print ('Le resultat :',mot_screen)
        if mot_screen == mot :
                liste_joueurs[joueur_actuel][1] = (8-(essai-1)) + liste_joueurs[joueur_actuel][1]
                liste_joueurs[joueur_actuel][0] += 1
                print ('Felicitations ! Votre nouveau score est {0} pour {1} jeux'.format(liste_joueurs[joueur_actuel][1],liste_joueurs[joueur_actuel][0]))
                essai = 9
    else :
        choix_jeu = input ("Si vous voulez soumettre le mot, tapez 'Y', sinon 'N' : ")
        if choix_jeu == 'Y' :
            mot_screen = input('Tapez votre mot en majuscule ; ')
            if mot_screen == mot :
                liste_joueurs[joueur_actuel][1] = (8-(essai-1)) + liste_joueurs[joueur_actuel][1]
                liste_joueurs[joueur_actuel][0] += 1
                print ('Felicitations ! Votre nouveau score est {0} pour {1} jeux'.format(liste_joueurs[joueur_actuel][1],liste_joueurs[joueur_actuel][0]))
                essai = 9
            else :
                print ('Dommage ! Le bon mot est ', mot)
                liste_joueurs[joueur_actuel][0] += 1       
                print ('Votre score reste {0} pour {1} jeux'.format(liste_joueurs[joueur_actuel][1],liste_joueurs[joueur_actuel][0]))
                essai = 9
        else :
            lettre = input('Essai {}. Tapez une lettre du mot en majuscule : '.format(essai))
            i = 0
            while i < 8 :
                if mot[i] == lettre :
                    mot_screen = mot_screen[0:i]+lettre+mot_screen[i+1:8]
                i+=1
            print('Le resultat :',mot_screen)
            if mot_screen == mot :
                liste_joueurs[joueur_actuel][1] = (8-(essai-1)) + liste_joueurs[joueur_actuel][1]
                liste_joueurs[joueur_actuel][0] += 1
                print ('Felicitations ! Votre nouveau score est {0} pour {1} jeux'.format(liste_joueurs[joueur_actuel][1],liste_joueurs[joueur_actuel][0]))
                essai = 9
    essai += 1
if essai == 9 :
    print ('Vous etes pendu-e. Le bon mot est ', mot)
    liste_joueurs[joueur_actuel][0] += 1
    print ('Votre score reste {0} pour {1} jeu(x)'.format(liste_joueurs[joueur_actuel][1],liste_joueurs[joueur_actuel][0]))
with open ('scores','wb') as fichier :
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(liste_joueurs)

#os.system('pause')
    
    


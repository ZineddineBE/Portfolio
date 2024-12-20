'''
ProjetPython–Puissance4

Nom: Zineddine BEOUCHE

Fonctionnalités demandées implémentées:
    - Initialisation d'une grille de jeu de nr lignes et nc colonnes, et qui ne contient aucun disque,
    - Fonctions nr(g) et nc(g), 
    - Afﬁchage d'une grille avec des caractères,
    - Savoir si une colonne c est un coup valide pour une grille g, 
    - Demander au joueur p de saisir une colonne valide de g,
    - Déterminer quelle est la ligne r où tombe le disque joué à la colonne c dans la grille g,
    - Modiﬁer la grille g avec le disque que le joueur p a joué en colonne c,
    - La fonction play() qui fait jouer les 2 joueurs,
    - Le prédicat is_align (g, lc, p) qui vérifie si 4 disques de même couleurs sont alignés,
    - Le prédicat is_win(g,r,c,p) qui indique si la case (r,c) provoque la victoire du joueur p,
    - La fonction ia_aleat (g) qui renvoie aléatoirement une colonne c,
    - La fonction ia_win(g, joueur) qui analyse la victoire,
    - La fonction unmove(g, c,ligne) qui annule un coup.
    
print("\033[1m") mettre en gras du texte (à mettre au début du texte)
print("\033[0m") fin du texte en gras (à mettre à la fin du texte)
time.sleep(0.75) pour bien analyser ce que l'IA fait quand elle joue
'''

from render_connect4 import*
import time 
    

#Initialisation de la grille de jeu en fonction de ce que l'utilisateur saisie comme nombre de ligne et de colonne
#Retourne la liste de la grille de jeu

def initialisationGrille(nr, nc):
    nr = int(input("Entrez un nombre de ligne pour le plateau de jeu: "))
    nc = int(input("Entrez un nombre de colonne pour le plateau de jeu: "))
    g=[]
    for i in range(nr):
        g=g+[[0 for j in range(nc)]]
    return g


#Retourne le nombre de lignes du plateau de jeu

def nr(g):
    return len(g)
    print('Le nombre de ligne du plateau est de : ', len(g))


#Retourne le nombre de colonnes du plateau de jeu

def nc(g):
    return len(g[0])
    print('Le nombre de colonne du plateau est de : ', len(g[0]))


#Affichage de la grille sous forme d'une chaine de caractères
#'O' pour le joueur 1 (disque rouge)
#'X' pour le joueur 2 (disque jaune)
#Retourne la chaine de caractère grille qui contient l'affichage du plateau de jeu dans la console
    
def grille_avec_caracteres(g):
    grille = ''
    for i in range(nr(g)):
        for j in range(nc(g)):
            if g[i][j]==1:
                grille=grille+'O  '
            elif g[i][j]==2:
                grille=grille+'X  '
            else:
                grille=grille+'-  '
        grille=grille+'\n'
    grille=grille+'=  '*nc(g)
    grille=grille+'\n'
    for k in range(nc(g)):   
        grille=grille+str(k)+'  '
    print("\n---------------------------\n")
    return grille


#Vérifie si une colonne est valide ou non
#Retourne True si la colonne est valide et False sinon

def colonne_est_valide(c,g):
    for i in range(nr(g)):
        if c<0 or c>=nc(g) or g[i][c]!=0:
            return False
        else:
            return True
        

#Demande à l'utilisateur de saisir une colonne valide, lui redemande s'il n'a pas saisie une colonne valide
#Retourne la colonne valide

def saisie_colonne_valide(g):
    colonne=int(input("Choisissez une colonne : "))
    while colonne_est_valide(colonne,g)!=True:
        print("Colonne invalide !")
        colonne=int(input("Choisissez une colonne : "))
    print("Colonne valide !")
    return colonne


#Trouve à qu'elle ligne le disque va tomber
#Retourne la ligne qui correspond à l'endroit où le disque va tomber

def quelle_ligne(c,g):
    r=0
    for i in range(nr(g)): 
        if g[i][c]==0:
            r=i
    return r


#Met à jour la grille avec le disque au bon endroit

def update_grille(r, c, g, p):
    if p==1:
        g[r][c]=1
    else:
        g[r][c]=2
    print(grille_avec_caracteres(g))
    draw_connect4(g)   


#Met à jour la grille pour le test dans ia_win

def show_grille(r, c, g, p):
    if p==1:
        g[r][c]=1
    else:
        g[r][c]=2


#Vérifie si 4 disques sont alignés ou non
#Renvoie True si la 4 disques sont alignés et False sinon

def is_align(g, lc, p):
    cpt=0
    for i in range(len(lc)):
        if  lc[i][1] >=0 and lc[i][1]<nc(g):
            if  lc[i][0] >=0 and lc[i][0]<nr(g):
                if g[lc[i][0]][lc[i][1]]!=p:
                    cpt=0
                else:
                    cpt=cpt+1
                    if cpt==4:
                        return True
    return False   


#Vérifie si un coup est gagnant ou non
#Renvoie True si un coup est gagnant et False sinon

def is_win(g, r, c, p):
    lh=[(r, c-3), (r, c-2), (r, c-1), (r, c), (r, c+1), (r, c+2), (r, c+3)] #horizontal
    lv=[(r-3, c), (r-2, c), (r-1, c), (r, c), (r+1, c), (r+2, c), (r+3, c)] #verticale
    ld1=[(r-3, c+3), (r-2, c+2), (r-1, c+1), (r, c), (r+1, c-1), (r+2, c-2), (r+3, c-3)] #diagonale gauche
    ld2=[(r-3, c-3), (r-2, c-2), (r-1, c-1), (r, c), (r+1, c+1), (r+2, c+2), (r+3, c+3)] #diagonale droite
    if is_align(g, lh, p) or is_align(g, lv, p) or is_align(g, ld1, p) or is_align(g, ld2, p):
        return True
    else:
        return False
   
   
#Renvoie une colonne col aléatoire
    
def ia_aleat(g):
    col=randint(0,nc(g)-1)
    while colonne_est_valide(col, g)!=True:
        col=randint(0,nc(g)-1)
    return col
             

#Fonction qui fait jouer un humain en lui demandant de saisir une colonne valide
#Retourne la variable verif qui indique si un coup est gagnant ou non

def jeu_humain(g, joueur):
    colonne=saisie_colonne_valide(g)
    ligne=quelle_ligne(colonne,g)
    update_grille(ligne, colonne, g, joueur)
    verif=is_win(g, ligne, colonne, joueur)
    return verif


#Fonction qui analyse la victoire d'un coup lorsqu'une IA joue,
#s'il n'y a pas de coup gagnant ia_aleat(g) joue un coup aléatoirement
#Retourne True si c'est un coup gagnant et False sinon 

def ia_win(g, joueur):
    colonnes_valides=all_colonnes_valides(g)
    for col in colonnes_valides:
        ligne=quelle_ligne(col, g)
        show_grille(ligne, col, g, joueur)
        verif=is_win(g, ligne, col, joueur)
        if verif == True:
            print(grille_avec_caracteres(g))
            draw_connect4(g)
            time.sleep(0.75)
            return verif
        else:
            unmove(g, col, ligne)     
    colonne=ia_aleat(g)
    ligne=quelle_ligne(colonne,g)
    update_grille(ligne, colonne, g, joueur)
    time.sleep(0.75)
    return False


#Retourne la liste de toutes les colonnes valides

def all_colonnes_valides(g):
    l=[]
    for c in range(nc(g)):
        if colonne_est_valide(c,g):
            l.append(c)
    return l
            

#Fonction qui annule un coup
#Retourne la grille sans le coup qui a été annulé
    
def unmove(g, c,ligne):
    g[ligne][c]=0
    return g
    

#Fonction qui demande à l'utilisateur s'il veut rejouer une partie ou non 

def replay():
    print("\033[1m")
    rejouer=input("Voulez-vous rejouer une partie ? (o/n)")
    print("\033[0m")
    if rejouer=='o':
        play()
    else:
        print("\033[1m","Au revoir et merci d'avoir jouer !","\033[0m")
        exit(0)
    

#Jeu à 2 joueurs (Humain et IA)

def play():
    g=initialisationGrille(nr, nc)
    draw_connect4(g)
    joueur1=input("Le joueur 1 est-il un humain ? (o/n)")
    joueur2=input("Le joueur 2 est-il un humain ? (o/n)")
    print(grille_avec_caracteres(g))
    verif=False 
    cpt_coup=0
    while cpt_coup!=nc(g)*nr(g):
        if joueur1=='o' and joueur2=='o': #Joueur contre Joueur
            joueur=1
            print("\nAu tour du joueur",joueur,"!")
            verif=jeu_humain(g, joueur)
            cpt_coup=cpt_coup+1
            if cpt_coup==nc(g)*nr(g):
                print("\033[1m","\nAucun joueur n'a gagné la partie...","\033[0m")
                replay()
            elif verif!=True:
                joueur=2
                print("\nAu tour du joueur",joueur,"!")
                verif=jeu_humain(g, joueur)
                cpt_coup=cpt_coup+1
        elif joueur1=='n' and joueur2=='n':#IA contre IA
            joueur=1
            verif=ia_win(g, joueur)
            cpt_coup=cpt_coup+1
            if cpt_coup==nc(g)*nr(g):
                print("\033[1m","\nAucun joueur n'a gagné la partie...","\033[0m")
                replay()
            elif verif!=True:
                joueur=2
                verif=ia_win(g, joueur)
                cpt_coup=cpt_coup+1
        elif joueur1=='o' and joueur2=='n':#Joueur contre IA
            joueur=1
            print("\nAu tour du joueur",joueur,"!")
            verif=jeu_humain(g, joueur)
            cpt_coup=cpt_coup+1
            if cpt_coup==nc(g)*nr(g):
                print("\033[1m","\nAucun joueur n'a gagné la partie...","\033[0m")
                replay()
            elif verif!=True:
                joueur=2
                verif=ia_win(g, joueur)
                cpt_coup=cpt_coup+1
        elif joueur1=='n' and joueur2=='o':#IA contre Joueur
            joueur=1
            verif=ia_win(g, joueur)
            cpt_coup=cpt_coup+1
            if cpt_coup==nc(g)*nr(g):
                print("\033[1m","\nAucun joueur n'a gagné la partie...","\033[0m")
                replay()
            elif verif!=True:
                joueur=2
                print("\nAu tour du joueur",joueur,"!")
                verif=jeu_humain(g, joueur)
                cpt_coup=cpt_coup+1
        if verif==True or verif==True and cpt_coup==nc(g)*nr(g):
            print("\033[1m")
            print("\nLe joueur",joueur,"gagne la partie. Bravo !")
            print("\033[0m")
            replay()
    print("\033[1m","\nAucun joueur n'a gagné la partie...","\033[0m")
    replay()           


play()
wait_quit()
        

    
        

    
        
    





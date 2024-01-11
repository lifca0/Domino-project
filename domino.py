import random as rd

def listDomino():   #créer la liste de domino sans répétition
    y=[]
    for n in range (7):
        x=[(n,k)for k in range (n,7)] #avoir les dominos sans répétition.
        y+=x #créer une seule liste avec tous les dominos
    return y
            
def distrib ():     #faire la distribution des dominos entre les joueurs
    joueur=[[],[],[],[]] #On va créer 1 seul liste avec les dominos de tous les joueurs
    domino = listDomino ()
    for i in range (len(joueur)):
        for j in range (7): #chaques joueurs a 7 dominos dans sa main
            x=rd.randint(0,len(domino)-1)
            joueur[i].append(domino[x]) #le joueur numéro i obtient le domino x
            del domino[x] #supprimer le domino tiré de la liste de dominos initiale  
    return joueur



#Dans cette partie , on code pour l'instant que l'interaction entre un joueur et le plateau, chaque cas specifique n'ont pas encore ete traité , on code pour l'instant que le cas le plus generale. 
#création de liste pour des tests


def dominoplaceable (joueur): #Cette partie permet de savoir quel domino que l'on peut placer sur le plateau 
    place=[]
    placeD=[] #Liste des dominos que l'on peut placer à droite
    placeG=[] #Liste des dominos que l'on peut placer à gauche
    if plateau==[]:
        return (joueur,placeG,placeD)
    else: 
        for k in range(len(joueur)):
            for i in range(2):
                if joueur[k][i] == plateau[0][0]:
                    placeG.append(joueur[k]) #liste de domio qu'on peut placer a gauche
                elif joueur[k][i] == plateau[len(plateau)-1][1]:
                    placeD.append(joueur[k]) #liste de domio qu'on peut placer a droite
        #parfois on peut placer un domino des 2 côtés, cette partie permet de supprimer les doublons et de les regrouper dans une seul liste appelé "place".
        if placeG != [] or placeD != [] :
            for k in placeG:
                if k not in place: #si le domino est dans la liste de ceux placeable a gauche mais pas dans la liste "place" on le rajoute à la liste
                    place.append(k)
            for k in placeD: 
                if k not in place: #pareil que la boucle du dessus mais pour ceux qu'on peut placer à droite.
                    place.append(k)
            return (place,placeG,placeD)
        else : #Si aucun dominos n'est placeable (ni a gauche ni a droite) le joueur dis "boudé"
            return ("BOUDE",placeG,placeD)


def inverse (domino): #permet d'inverser le domino si il est dans le mauvais sens
    return (domino[1],domino[0]) # prend en argument un domino (n,p) et renvoie le domino (p,n)


# permet de placer à gauche ou à droite le domino choisie 
def placement (joueur): #si c'est le joueur qui joue
    if plateau == []:#plateau vide
        plateau.append(place[int(a)-1])
        del joueur[joueur.index(place[int(a)-1])] #permet de supprimer le domino choisis de la main du joueur
        return plateau
    else:
        l=len(plateau)-1
        b=0
        if place[int(a)-1] in placeG and place[int(a)-1] in placeD: #vérifie si on peut placer le domino des 2 côtés
            b=int(input("Entrer 1 pour placer à gauche et 2 pour placer à droite ")) #choisir ou placer son domino 
            if b==1 : #vérifie si le joeur veut jouer a gauche 
                if place[int(a)-1][1]== plateau[0][0]: #vérifie si le domino est dans le bon sens 
                    plateau.insert(0,place[int(a)-1]) #place à gauche si il est dans le bon sens
                else:
                    plateau.insert(0,inverse(place[int(a)-1])) #place à gauche si il est dans le mauvais sens
            elif b==2: #vérifie si le joeur veut jouer a droite
                if place[int(a)-1][0]== plateau[l][1]: #vérifie si le domino est dans le bon sens 
                    plateau.append(place[int(a)-1]) #place à droite si il est dans le bon sens
                else:
                    plateau.append(inverse(place[int(a)-1])) #place à droite si il est dans le mauvais sens   
        elif place[int(a)-1] in placeG and not place[int(a)-1] in placeD: #vérifie si on peu placer uniquement a gauche
            if place[int(a)-1][1]== plateau[0][0]: #vérifie si le domino est dans le bon sens
                plateau.insert(0,place[int(a)-1]) #place à gauche si il est dans le bon sens
            else:
                plateau.insert(0,inverse(place[int(a)-1])) #place à gauche si il est dans le mauvais sens
        elif place[int(a)-1] in placeD and not place[int(a)-1] in placeG: #vérifie si on peu placer uniquement a droite
            if place[int(a)-1][0]== plateau[l][1]:
                plateau.append(place[int(a)-1])
            else:
                plateau.append(inverse(place[int(a)-1])) #place à droite
        del joueur[joueur.index(place[int(a)-1])] #permet de supprimer le domino choisis de la main du joueur
        return plateau
    
#PARTIE IA
def ia_base(joueur): #fonctionne pareil que placement mais de manière aléatoire
    domino=rd.randint(0,len(place)-1)
    if plateau == []:#plateau vide
        plateau.append(place[domino])
        del joueur[joueur.index(place[domino])] #permet de supprimer le domino choisis de la main du joueur
        return plateau
    if place[domino] in placeG and place[domino] in placeD:
        b=rd.randint(0,1)
        if b==0 : #vérifie si le joeur veut jouer a gauche 
            if place[domino][1]== plateau[0][0]: #vérifie si le domino est dans le bon sens 
                plateau.insert(0,place[domino]) #place à gauche si il est dans le bon sens
            else:
                plateau.insert(0,inverse(place[domino])) #place à gauche si il est dans le mauvais sens
        elif b==1: 
            if place[domino][0]== plateau[len(plateau)-1][1]: #vérifie si le domino est dans le bon sens 
                plateau.append(place[domino]) #place à droite si il est dans le bon sens
            else:
                plateau.append(inverse(place[domino]))
    elif place[domino] in placeG and not place[domino] in placeD: #vérifie si on peu placer uniquement a gauche
        if place[domino][1]== plateau[0][0]: #vérifie si le domino est dans le bon sens
            plateau.insert(0,place[domino]) #place à gauche si il est dans le bon sens
        else:
            plateau.insert(0,inverse(place[domino])) #place à gauche si il est dans le mauvais sens
    elif place[domino] in placeD and not place[domino] in placeG: #vérifie si on peu placer uniquement a droite
        if place[domino][0]== plateau[len(plateau)-1][1]:
            plateau.append(place[domino])
        else:
            plateau.append(inverse(place[domino])) #place à droite
    del joueur[joueur.index(place[domino])] #permet de supprimer le domino choisis de la main du joueur
    return plateau

def comptedomino (): 
    #permet de compter le nombre de dominos placer avec un certains nombre de points (très utile pour une IA avancée)
    compte=[] 
    for k in range (7):
        x=0
        for i in range(len(plateau)):#pour avoir le domino numero i
            if k == plateau[i][0] or k == plateau [i][1]:
                x+=1
        compte.append(x)
    return compte

def comptepoints (joueur): #Il peut arriver que la partie soit bloqué donc on compte les nombre de points par joueur
    x=70#le plus grand nombre de points qu'un joueur peut avoir avec 7 dominos est 69 donc on initialise a 70
    k=0
    for i in range(len(joueur)):#pour avoir le joueur numero i
        pointsjoueur=0 #on initialise a 0
        for domino in joueur[i]:
            pointsjoueur+=domino[0]+domino[1] #on coompte par rapport aux points sur les dominos
        if x>pointsjoueur: #on cherche celui qui a le moins de points pour déterminer le gagnant
            x=pointsjoueur 
            k=i+1 #le numéro du joueur avec le moins de points
    return x,k #le programme renvoie le nombre de points du gagnant ainsi que son numéro 
  

      
def gagnant ():
    if [] in joueur: #test si un joueur n'a plus de dominos
        return 1
    elif dominoplaceable(joueur[0])[0] == "BOUDE" and  dominoplaceable(joueur[1])[0] == "BOUDE" and dominoplaceable(joueur[2])[0] == "BOUDE" and dominoplaceable(joueur[3])[0] == "BOUDE":
        #test si tout le monde est boude
        return 2
    else:#si il n'y a pas de gagnants
        return 0 



#Partie interaction avec l'utilisateur 
joueur = distrib () #permet de créer la liste de domino de tous les joueurs
plateau=[] #le plateau de jeu est vide au début donc on crée une liste vide


nbj=input("Entrer le nombre de joueurs dans la partie: ") #nombre de joueurs

x=0  #permet de savoir quel joueur joue (joueur n°x)
for k in range(len(joueur)):
    if (6,6) in joueur[k]: #le joueur avec le double 6 commence
        x=k
            
while gagnant() == 0 :  #test si il y a un gagnant.
    place,placeG,placeD = dominoplaceable(joueur[x])
    
    if x <= int(nbj)-1 : #si c'est un vraie joueur
        print("\nplateau: ", plateau) #Affichage du plateau 
        print("\njoueur", x+1 ,"tes dominos: ", joueur[x]) #Affiche des dominos du joueur qui doit jouer 
        print("dominos placeable: ", place) #affiche la liste des dominos qu'il peut placer     
        if place != "BOUDE" : #regarde si le joueur n'est pas boudé
            a=input("Entrer le numero du domino à placer ") #le joueur choisis quel domino il veut jouer parmis la liste de dominos placeable. 
            while int(a)>len(place): #empêche le joueur de choisir un domino qui n'est pas dans la liste par erreur.
                if len(place) !=1:
                    print ("\nvous devez choisir un domino compris ente 1 et ", len(place))
                    a=input("Entrer le numero du domino à placer ")
                else :
                    print("vous ne pouvez placer qu'un seul domino, appuyer sur 1:")
                    a=input("")
            placement (joueur[x]) #effectue la commande placement pour modifier le plateau 
        else : #affiche "joueur suivant" si le joueur est boudé.
            print ( "\nJOUEUR SUIVANT") #\n permet de sauter une ligne
    else: #si c'est l'IA qui doit jouer
        print("\nplateau: ", plateau) #Affichage du plateau 
        print("\nbot n°", x+1 ,"tes dominos: ", joueur[x]) #Affiche des dominos du joueur qui doit jouer 
        print("dominos placeable: ", place) #affiche la liste des dominos qu'il peut placer 
        if place != "BOUDE" : #regarde si l'IA n'est pas boudé
            ia_base(joueur[x]) #effectue la commande pour que l'IA joue et que ça modifie le plateau
        else : #affiche "joueur suivant" si l'IA est boudé.
            print ( "\nJOUEUR SUIVANT") #\n permet de sauter une ligne
    if [] in joueur: #test si un joueur n'a plus de dominos pour désigner un gagnant
        ()
    else:
        x=(x+1)%4 #permet de passer au joueur suivant en modulo 4
        
#si il y a un gagnant la séquence précédente s'arrete et test si:
if gagnant() == 1: #si un joueur n'a plus de dominos
    x=joueur.index([])
    if x<= int(nbj):
        print ("\nBravo,joueur",x+1,"a gagné car il n'à plus de dominos.")
    else:
        print ("Pas de chance, c'est le bot n°", x+1, " qui a gagné")
else:  #si le jeu est bloqué
    points,gagnant=comptepoints(joueur)
    if gagnant<= int(nbj):
        print ('le jeu est bloqué, bravo au joueur', gagnant, ' qui gagne avec' , points,  'points.')
    else:
        print ("le jeu est bloqué, c'est le bot n°", gagnant, ' qui gagne avec' , points,  'points.')
 




        
        
"""

IA & Datascience - Classification Challenge
Hélène Peignard
TD I

"""
import math
import random


def distance(x,y):
    # methode de chebyshev pour mesurer une distance
    dist=max(abs(float(x[0])-float(y[0])),abs(float(x[1])-float(y[1])),abs(float(x[2])-float(y[2])),abs(float(x[3])-float(y[3])))
    return dist

def KVoisins(entree,apprentissage,k):
    listeF=[]
    for ent in entree: # pour chaque valeurs dans le tableau d'entrée
        temp=[]
        temp2=[]
        liste_cat=[]
        nbCat=[]
        # on récupère les catégories avec leur nom
        # et un autre tableau à 0 qui représente le
        # nombre de fois que cette catégorie est la plus proche
        for a in apprentissage:
            if a[len(a)-1] not in liste_cat:
                liste_cat.append(a[len(a)-1])
                nbCat.append(0)
        # on calcul les distance entre l'entrée et les valeurs de l'apprentissage
        for ap in apprentissage:
            temp.append([distance(ent,ap),ap])
        temp.sort() # on tri le tableau final 
        temp2=temp[:k] # on ne garde que les K valeurs (paramètre de la fonction)
        for e in temp2: # pour chaque valeurs de catégories restantes, on va aller 
            #remplir dans les tableaux des catégories en ajoutant 1 à la 
            # catégorie la plus proche à chaque fois
            l=len(e)-1
            m=len(e[l])-1
            nomCat=e[l][m] 
            num=liste_cat.index(nomCat) # on récupère l'indice qui correspond au nom pour le tableau avec la quantité
            nbCat[num]+=1
        idx=nbCat.index(max(nbCat)) # on ne garde que la catégorie qui a le nombre le plus élévés
        dataInfos=liste_cat[idx]
        listeF.append([ent,dataInfos]) # on enregistre les données de l'entrée et la catégorie 
    return listeF

def Apprentissage(fichier):
    # même méthode de lecture que pour le fichier finalTest.csv
    data=open(fichier)
    dataset=data.read()
    data.close()
    final=[]
    dataset=dataset.split('\n')
    for d in dataset:
        da=d.split(';')
        temp=[]
        for row in da:
            temp.append(row)
        final.append(temp)
    final.pop() # le dernier elément est vide, il faut donc l'enlever
    return final

def main():
    data=open("finalTest.csv") # on récupère les données
    # on les sépare afin d'avoir chaque valeur indépendante
    # au lieu de conserver un seul string à chaque fois
    dataset=data.read()
    data.close()
    dataCoord=[]
    dataset=dataset.split('\n')
    for d in dataset:
        da=d.split(';')
        temp=[]
        for row in da:
            temp.append(row)
        dataCoord.append(temp)
    dataCoord.pop() # le dernier elément est vide, il faut donc l'enlever
    entree=dataCoord
    # on utilise data.csv comme apprentissage
    fichierAp='data.csv'
    apprentissage=Apprentissage(fichierAp)

    # on récupère une liste des catégories
    liste_cat=[]
    for a in apprentissage:
        if a[len(a)-1] not in liste_cat:
            liste_cat.append(a[len(a)-1])
    k=6
    d_out=KVoisins(entree,apprentissage,k)
    # creation du fichier de sortie avec les prédictions de catégorie
    sortie=open('outputExample_Peignard.txt','w')
    for i in d_out:
        sortie.write(str(i[len(i)-1])+'\n')
    sortie.close()
    print('Fin de la prédiction, fichier .txt créé')


main() #exécute le code 
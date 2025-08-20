import time
#Définition d'une arête
nbsommets = 0
nbaretes = 0
class Arete :
    def __init__(self, initial,final,cout):
        self.sommet_initial=initial   # sommet initial de l'arête
        self.sommet_final=final       # sommet final de l'arête
        self.sommet_cout=cout         # cout de l'arête


#Définition d'un graphe

class Graphe:
    def __init__(self,ns,aretes):
        self.nombre_sommet=ns        # nombre de sommets du graphe
        self.liste_aretes=aretes     # liste des arêtes du graphe


        
#Ecrire une fonction qui permet de construire une arête à partir d'informations saisies au clavier
def saisie_arete():
    si=int(input("Sommet initial: "))
    sf=int(input("Sommet final: "))
    cout=float(input("Cout: "))
    a =Arete(si,sf,cout)
    return a
    
#En déduire une fonction qui permet de construire un graphe à partir d'informations saisies au clavier
def saisie_graphe():
    global nbsommets, nbaretes
    listearetes=[]
    nbsommets=int(input("Nombre de sommets: "))
    nbaretes=int(input("Nombre d'aretes: "))
    for i in range(0, nbaretes):
        arete =[]
        print("Saisissez l'arête numero "+str(i+1)+':')
        time.sleep(0.5)
        a=saisie_arete()
        arete.append(a.sommet_initial)
        arete.append(a.sommet_final)
        arete.append(a.sommet_cout)
        listearetes.append(arete)
        g = Graphe (nbsommets,listearetes)
    return g

#Ecrire une fonction qui prend en entrée un graphe et qui renvoie sa matrice d'adjacence
def adjacence(g):
    mat = [[float(0) for i in range(g.nombre_sommet)]for i in range(g.nombre_sommet)]
    for i in range(len(g.liste_aretes)):
        mat[g.liste_aretes[i][0]-1][g.liste_aretes[i][1]-1] = g.liste_aretes[i][2]
        mat[g.liste_aretes[i][1]-1][g.liste_aretes[i][0]-1] = g.liste_aretes[i][2]
    return mat


# g = saisie_graphe()
# print(g.liste_aretes)
# print (adjacence(g))
# m = adjacence(g)
# print(m)

#Ecrire une fonction qui prend en entrée une matrice d'adjacence et qui l'affiche sous sa forme matricielle (affichage ligne par ligne).
def affichermatrice(adjacence):
    for ligne in adjacence:
        for c in ligne:
            print(c, end=" ")
        print()
        
# affichermatrice(m)
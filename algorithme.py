import graph as gr


g = gr.saisie_graphe()

m = gr.adjacence(g)

gr.affichermatrice(m)

def DetDeg(n, g, m):
   degre = 0
   for i in range (0, gr.nbsommets):
           if not(m[n][i]==0):
               degre+=1
   return degre
           

LC = ['White', 'Black', 'Blue', 'Yellow', 'Red', 'Green', 'Violet', 'Purple']
LSommet = []

for i in range (0, gr.nbsommets) : 
    Larrete =[]
    degreSommet = DetDeg(i, g, m)
    Larrete.append(int(i))
    Larrete.append(degreSommet)
    LSommet.append(Larrete)

LSommet.sort(key=lambda degre: degre[1], reverse=True)
print(LSommet) 

C = 0
SommetColo = 0

while SommetColo < len(LSommet):
    for i in range (len(LSommet)):
        if len(LSommet[i])== 2:
            Possible = True
            for j in range(i):
                if len(LSommet[j]) == 3 and LSommet[j][2] == LC[C] and m[LSommet[i][0]][LSommet[j][0]] == 1:
                    Possible = False
                    break
            if Possible:
                LSommet[i].append(LC[C])
                SommetColo += 1
    C += 1
    


print('Nombre de couleurs utilisées : ', C)
print('Liste Finale : ', LSommet)         
    
print("Sommets ayant la même couleur :")
for i in range(C):
    s = "couleur " + str(i) + " : "
    for e in LSommet:
        if e[2] == LC[i]:
            s += str(e[0]+1) + " "
    print(s)










   

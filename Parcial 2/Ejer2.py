from grafo import Grafo
from random import randint


grafo = Grafo(dirigido=False)


personajesStwrs = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C 3PO", "Princess Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2 D2", "BB 8"]

for i in personajesStwrs:
    grafo.insert_vertice(i)

#a
j=0


for i in personajesStwrs:
    posicion  = grafo.search_vertice(i)
    punto = grafo.get_element_by_index(posicion )
    if punto[1].size() < 4:
        k = 0
        while j == 0:
            if k >= len(personajesStwrs):
                j=1
            else:
                place = personajesStwrs[k]
                posicionb = grafo.search_vertice(place)
                puntob = grafo.get_element_by_index(posicionb)
                checker = grafo.is_adyacent(punto[0],puntob[0])
                if puntob[1].size() < 3 and punto[0] != puntob[0] and checker == False: 
                    value = randint(1, 20)
                    grafo.insert_arist(punto[0], puntob[0], value)
                    if punto[1].size() == 3:
                        j=1
                k += 1
        j=0

grafo.barrido()

i=0



tree_min = grafo.kruskal()

valor_maximo = 0
nodo_maximo = list
for tree in tree_min:
    print("Arbol Minimo")
    for nodo in tree.split(";"):
        value = nodo.split("-")
        print(nodo)
        if value[0]=="Yoda" or value[1]=="Yoda":
            i = 1
        if int(value[2])>valor_maximo:
            nodo_maximo = value
    if i ==1:
        print("Yoda existe en el arbol minimo")
        print(f"Esta es la arista de valor maximo {nodo_maximo[0]} y {nodo_maximo[1]} comparten {nodo_maximo[2]} episodios")

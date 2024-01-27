import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo():
    G = nx.Graph()

    # Agregar nodos
    G.add_nodes_from([1, 2, 3, 4])

    # Agregar enlaces
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

    return G

def dibujar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
    plt.show()

def desconectar_enlace(G, nodo_a, nodo_b):
    if G.has_edge(nodo_a, nodo_b):
        print(f"Desconectando enlace entre {nodo_a} y {nodo_b}")
        G.remove_edge(nodo_a, nodo_b)
    else:
        print(f"No hay un enlace entre {nodo_a} y {nodo_b}")

def main():
    grafo = crear_grafo()
    dibujar_grafo(grafo)

    # Desconectar un enlace
    nodo_desconexion_a = int(input("Ingrese el primer nodo a desconectar: "))
    nodo_desconexion_b = int(input("Ingrese el segundo nodo a desconectar: "))

    desconectar_enlace(grafo, nodo_desconexion_a, nodo_desconexion_b)

    dibujar_grafo(grafo)

if __name__ == "__main__":
    main()


import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class DisjointSet:    # Classe para representar um conjunto disjunto

    def __init__(self, n):
        # cria conjuntos disjuntos n (um para cada vértice)
        self.pai = {i: i for i in range(1, n + 1)}

    def Find(self, k):  # Encontra a raiz do conjunto ao qual o elemento k pertence
        # se `k` for raiz
        if self.pai[k] == k:
            return k

        # recursão até encontrar a raiz
        return self.Find(self.pai[k])

    def Union(self, a, b):  # Realiza união de dois subconjuntos
        # encontra a raiz dos conjuntos aos quais os elementos x e y pertencem
        x = self.Find(a)
        y = self.Find(b)

        self.pai[x] = y

# Função para construir a MST usando o algoritmo de Kruskal
def Kruskal(edges, n):
    MST = []  # armazena as arestas presentes no MST
    index = 0

    # Inicializa a classe DisjointSet e cria um conjunto disjunto para cada elemento
    ds = DisjointSet(n)

    # classifica as arestas aumentando o peso
    edges.sort(key=lambda x: x[2])

    # MST contém n-1 bordas
    while len(MST) != n - 1:

        # considera a próxima aresta com peso mínimo do gráfo
        (orig, dest, peso) = edges[index]
        index += 1 

        # encontra a raiz dos conjuntos para os quais dois
        # vértices da aresta pertencem
        x = ds.Find(orig)
        y = ds.Find(dest)

        # se ambos os vertices tiverem pais diferentes, eles pertencem a
        # diferentes componentes conectados e podem ser incluídos no MST
        if x != y:
            MST.append((orig, dest, peso))
            ds.Union(x, y)

    return MST


# Parte principal

def test(nodes, lines):

        # Criar grafo
        grafo = {}
        for line in lines:
            if line.startswith('*'):
                continue
            orig, dest, peso = line.split()
            if orig not in grafo:
                grafo[orig] = {}
            if dest not in grafo:
                grafo[dest] = {}
            grafo[orig][dest] = peso
            grafo[dest][orig] = peso

        # Converter grafo em uma uma lista de vertices
        # (u, v, w) triples representam: vértice de partida `u` -> vértice de chegada `v` com peso `w`
        arestas = []
        for orig, neighbors in grafo.items():
            for dest, peso in neighbors.items():
                arestas.append((int(orig), int(dest), int(peso)))
        # Kruskal
        mst = Kruskal(arestas, int(nodes))

        # Output
        sumKm = 0
        for edge in mst:
            print(f'Pedro se deslocou da loja {edge[0]} até a loja {edge[1]} e percorreu {edge[2]}km.')
            sumKm += int(edge[2])
        print('-------- FIM DO PERCURSO --------')
        print(f'Pedro percorreu {sumKm}km.')
        return mst

def CriarGrafo(grafo):
    df = {'origem': [], 'destino': [], 'peso': []}

    #transforma a lista de tuplas mst em dicionário com chaves from (vértice de partida), to(vértice de destino) e peso
    for i in range(len(grafo)):
        df['origem'].append(grafo[i][0])
        df['destino'].append(grafo[i][1])
        df['peso'].append(grafo[i][2])
        
    # constroi o grafo
    Grafo = nx.from_pandas_edgelist(df, 'origem', 'destino')
    nx.draw(Grafo, with_labels=True, node_size=0.6, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=10)
    plt.grid(True)
    return plt.gcf()


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

layout = [[sg.Text('Escolha um arquivo com a base de dados ou escreva manualmente')],
          [sg.Text('Choose a file: ',  enable_events=True), sg.FileBrowse(key='browse',)],
          [sg.Button('Adicionar base de dados', key='ADDBASE', enable_events=True)],
          [sg.Text('Digite o número de vértices'), sg.Input(key='-VER-'), sg.Button('Adicionar número de vértices', key='add', enable_events=True)],
          [sg.Text('Digite a primeira vértice, a segunda vértice e o peso da aresta'), sg.Input(key='-ARE-'), sg.Button('Adicionar aresta', key='OK', enable_events=True)],
          [sg.Button('Mostrar grafo', key='-OK-', enable_events=True)], 
          [sg.Canvas(size=(1000, 1000), key='-CANVAS-')],
          ]
sg.theme('DarkTeal')
print = sg.Print
window = sg.Window('Kruskal Algoritmo - Visualização', layout, location=(0,0), size=(800,600), keep_on_top=True, resizable = True).Finalize()


lines=[]
fim = False
while True:
    event, values = window.read()
    if event == 'ADDBASE':
            # Abrir a base de dados
            path = values['browse']
            with open(path) as f:
                lines = f.readlines()

            # guardar numero de vertices
            _,nodes = lines[0].split()
    
    elif event == 'OK':
        
        lines.append(str(values['-ARE-']))
                
    elif event == '-OK-':

        mst = test(nodes, lines)

        draw_figure(window['-CANVAS-'].TKCanvas, CriarGrafo(mst)) 

    elif event == 'add':

        nodes = values['-VER-']    

    elif event == sg.WIN_CLOSED:
        break

window.close()
# Algoritmo-de-Kruskal-Projeto
Um projeto de faculdade realizado para a cadeira de Algoritmos e Estrutura de Dados

Universidade Federal de Pernambuco 
Centro de Informática - CIn 

Disciplina: Algoritmos e estruturas de dados
Docente: Sérgio Queiroz 
Discente: 
Ana Júlia de Oliveira Fernandes
Bruno Miguel Moreira Albuquerque


## Relatório do projeto: Grupo #4.3

Recife, 18 de abril de 2023

## Implementação
### Algoritmo utilizado:
 Algoritmo de Kruskal - Árvore geradora mínima
### Desenvolvimento: 
Primeiramente foi escolhida uma base de dados para realizar o projeto. Após isso, foi iniciado o desenvolvimento do algoritmo de Kruskal. Feita a parte principal, que era resolver o problema mst, partimos para a visualização do grafo gerado a partir do algoritmo utilizando as bibliotecas networkx e matplotlib. Para finalizar, foi desenvolvido uma interface gráfica com pysimplegui que permite a visualização do projeto construído.
### Bibliotecas utilizadas: 
 Foram usados networkx, matplotlib para criar o grafo mst e PySimpleGUI para criar a interface gráfica

## Conclusão
- Na interface pode ser usada para ver o caminho de menor custo da base de dados de jazz utilizado no projeto, assim como pode ser adicionado uma base de dados da escolha do usuário ou adicionar o grafo manualmente. 
- Instruções para usar a base de dados de jazz:
  Clicar em adicionar base de dados percurso de Pedro;

  Clicar em gerar caminho de menor custo.
- Instruções para usar outra base de dados:
  Clicar em browse;
  Escolher a base;
Clicar em adicionar base de dados;

Clicar em gerar caminho de menor custo.

- Instruções para usar manualmente:

  Digitar o número de vértices;

  Clicar em adicionar número de vértices;

  Digitar a vértice 1, a vértice 2 e o peso da aresta, apenas separadas com espaço. exemplo: <1 4 3> vértice 1 = 1, vértice 2 = 4 e peso = 3;

  Após digitada uma aresta, clicar em adicionar aresta, apagar a aresta que está na caixa e digitar a próxima.

  Depois de todas as arestas digitas, clicar em gerar caminho de menor custo.

OBS: A interface apenas aceita números para vértices dentro do intervalo do número de vértices. Exemplo: se foi adicionado 5 números de vértices, apenas pode ser adicionado como vértices números de 1 a 5. O peso é livre para qualquer número.


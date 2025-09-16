class Graph_adj_matrix:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_matrix=[[0]* vertices for _ in range(vertices)]

    #undirected graph
    def add_edge(self,source,destination,weight):
        self.adj_matrix[source][destination]=weight #change weight/True depending on normal or weighted graphs
        #self.adj_matrix[destination][source]=True #comment this line for directed graph
graph_adj_matrix=Graph_adj_matrix(4)
graph_adj_matrix.add_edge(0,1,20)
graph_adj_matrix.add_edge(0,2,10)
graph_adj_matrix.add_edge(2,3,30)
graph_adj_matrix.add_edge(3,1,40)

#print(graph_adj_matrix.adj_matrix)
for i in graph_adj_matrix.adj_matrix:
    print(i)



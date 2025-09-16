from collections import deque

class Graph_adj_list:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list={i:[] for i in range(vertices)}

    def add_edge(self,source,destinantion):
        self.adj_list[source].append(destinantion)
        self.adj_list[destinantion].append(source)

    #BFS

    def BFS(self,starting):
        visited=[False]*self.vertices
        queue=deque()

        visited[starting]=True
        queue.append(starting)

        while queue:
            top=queue.popleft()
            print(top,end=" ")

            for i in self.adj_list[starting]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
    
    #DFS

    def DFS(self,starting):
        visited=[False]*self.vertices

        stack=[starting]

        while stack:
            top=stack.pop()
            print(top)

            for i in self.adj_list[top]:
                if(not visited[i]):
                    visited[i]=True
                    stack.append(i)


graph_adj_list=Graph_adj_list(5)
graph_adj_list.add_edge(0,1)
graph_adj_list.add_edge(0,2)
graph_adj_list.add_edge(1,3)
graph_adj_list.add_edge(2,3)
graph_adj_list.add_edge(3,4)
graph_adj_list.add_edge(2,4)
#print(graph_adj_list.adj_list)
print("BFS")
graph_adj_list.BFS(0)
print()
print("DFS")
graph_adj_list.DFS(0)



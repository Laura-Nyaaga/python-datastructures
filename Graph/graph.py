# # bar graph
# import matplotlib.pyplot as plt
# x = ['Tomatoes', 'Kales', 'Onions', 'cabbages', 'Carrots']
# y = [12,34,20,23,10]
# plt.bar(x,y, color='blue')
# plt.xlabel('Groceries')
# plt.ylabel('Quantity')
# plt.title('A Bar Graph Representing the Groceries In A Farm against Quantity')

# plt.show()

# undirected graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.print_graph()
print("gggggggggggggggggggggggggggggggg")
# # Histogram
# import matplotlib.pyplot as plt
# ages=[18,22,19,18,21,24,23,22,18,19,21,19,19,27,28,19,24,23]
# plt.hist(ages,bins=range(min(ages),max(ages)+1),color='blue')
# plt.xlabel('Ages')
# plt.ylabel('Frequency')
# plt.title('Frequency of Ages of Students')
# plt.show()

# directed graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(3, 0, 4)
g.add_edge(2, 1, 1)
g.print_graph()

# adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def __str__(self):
        return str(self.graph)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

print("Graph is adjancecy list:")
print(g)

# adjancency Matrix
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.graph])

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("Graph as an adjacency matrix:")
print(g)

#Acyclic Graph
class Graph:
    def __init__(self, size):
     self.adj_matrix = [[0] * size for _ in range(size)]
     self.size = size
     self.vertex_data = [''] * size
    def add_edge(self, u, v):
     if 0 <= u < self.size and 0 <= v < self.size:
      self.adj_matrix[u][v] = 1
    def add_vertex_data(self, vertex, data):
     if 0 <= vertex < self.size:
      self.vertex_data[vertex] = data
    def print_graph(self):
     print("Adjacency Matrix:")
     for row in self.adj_matrix:
      print(' '.join(map(str, row)))
     print("\nVertex Data:")
     for vertex, data in enumerate(self.vertex_data):
      print(f"Vertex {vertex}: {data}")
# Creating an acyclic graph with 4 vertices
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

#cyclic graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
         if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = 1
          self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
         if 0 <= vertex < self.size:
          self.vertex_data[vertex] = data
    def print_graph(self):
         print("Adjacency Matrix:")
         for row in self.adj_matrix:
            print(' '.join(map(str, row)))
         print("\nVertex Data:")
         for vertex, data in enumerate(self.vertex_data):
          print(f"Vertex {vertex}: {data}")
# Creating a cyclic graph with 4 vertices
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.print_graph()
\




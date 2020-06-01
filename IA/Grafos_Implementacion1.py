class Graph:
    def __init__(self):
        self.graph = {}

    def __get_iterator(self, obj):
        try:
            iterator = iter(obj)
        except TypeError:
            iterator = (obj, )
        return iterator
    def add_vertex(self, vertex):
        for i in self.__get_iterator(vertex):
            self.graph[i] = set()

    def del_vertex(self, vertex):
        vertex = set(self.__get_iterator(vertex))
        for i in vertex:
            if i in self.graph:
                self.graph.pop(i)
        for i in self.graph.iterkey():
            self.graph[i] -= vertex
    def is_vertex(self, vertex):
        if vertex in self.graph:
            return True
        return False
    def add_edge(self, src, dest, undirected=True):
        for s in self.__get_iterator(src):
            if s not in self.graph:
                self.graph[s] = set()
            for d in self.__get_iterator(dest):
                if s == d:
                    continue
                if d not in self.graph:
                    self.graph[d] = set()
                self.graph[s].add(d)
                if undirected:
                    self.graph[d].add(s)
    def delete_edge(self, src, dest):
        dest = set(self.__get_iterator(dest))
        src = set(self.__get_iterator(src))
        for i in src:
            if i in self.graph:
                self.graph[i] -= dest
    
    def get_edge(self, vertex):
        return self.graph[vertex]
    
    def walk(self, source, topdown=False):
        v = set()
        l = [source]
        if topdown:
            print("DFS:")
        else:
            print("BFS:")
        v.add(source)
        while l:
            node = l.pop()
            print(node,)
            for i in self.graph[node]:
                if i not in v:
                    v.add(i)
                    if topdown:
                        l.append(i)
                    else:
                        l.insert(0,i)
        print()
    def __str__(self):
        s = "Vertex -> Edges\n"
        for k, v in self.graph.items():
                s += "%-6s -> %s\n" %(k,v)
        return s

graph = Graph()
graph.add_edge(1, (2, 3))
graph.add_edge(2, (4, 5))
graph.add_edge(3, (6, 7))
print(graph)

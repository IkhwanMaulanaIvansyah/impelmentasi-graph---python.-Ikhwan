import os
os.system('cls' if os.name == 'nt' else 'clear')
class Graph:
    def __init__(self, graphku=None):
        if graphku is None:
            graphku = {}
        self.graphku = graphku

    def getvertex(self):
        return list(self.graphku.keys())
   
    def getedge(self):
        edges = []
        for v in self.graphku:
            for e in self.graphku[v]:
                if {e, v} not in edges:
                    edges.append({e, v})
        return edges
   
    def addvertex(self, v):
        if v not in self.graphku:
            self.graphku[v] = []
         
    def addedge(self, e):
        (v1, v2) = e
        if v1 in self.graphku:
            self.graphku[v1].append(v2)
        else:
            self.graphku[v1] = [v2]
        if v2 in self.graphku:
            self.graphku[v2].append(v1)
        else:
            self.graphku[v2] = [v1]

graph1 = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"],
}

g = Graph(graph1)
print("awal : ", g.getvertex())
print("awal : ", g.getedge())
g.addvertex ("f")
print("tambah :", g.getvertex())
g.addedge ({"f","a"})
print("tambah :", g.getedge())
g.addedge ({"f","g"})
print("tambah ke-2", g.getvertex())
print("tambah ke-2", g.getedge())

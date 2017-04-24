class Vertice:
    def _init_(self):
        self.color="white"
        self.dist = 6
        self.name = 0
        self.pred = None
        
        
class Graph:
    def _init_(self):
    	self.nodes = dict()
    		
    def initialize_nodes(self,n):
        for i in range(1,n+1):
            self.nodes[Vertice()] = []
    	#print(self.nodes)

    def create_edges(self,u,v):
    	for key,value in self.nodes.items():
    		if(key.name == u):
    			value.append(v)
    		elif(key.name == v):
    			value.append(u)

    def nomear(self):
    	i=1
    	for key, value in self.nodes.items():
    		key.name = i
    		i=i+1

    def bfs(self,vert):
    	
    	vert[0][0].color = 'gray'
    	vert[0][0].pred = None
    	neighbors=[]
    	for n in vert[0][1]:
    		neighbors.append(n)

    	print(n)


if _name_ == "_main_":
 	g = Graph()
 	g.initialize_nodes(8)
 	g.nomear()
 	g.create_edges(1,4)
 	g.create_edges(1,5)
 	g.create_edges(3,6)

 	g.bfs(g.nodes.items())

 	"""for k,v in g.nodes.items():
 		print(k.name)
 		print(v)"""
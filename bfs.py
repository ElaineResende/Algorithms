import sys 
class Vertice:
    def __init__(self):
        self.color="white"
        self.dist = 0
        self.name = 0
        self.pred = None
        
        
class Graph:
    def __init__(self):
    	self.nodes = dict()
    		
    def initialize_nodes(self,n):
        for i in range(1,n+1):
            self.nodes[Vertice()] = []
    	#print(self.nodes)

   	"""def nodes_kjksld(self):
   		i=0
   		for key, value in self.nodes.items():
			key.name = 8
			i=i+1"""

    def create_edges(self,u,v):
    	#print("u-v: ", u, v)
    	for key,value in self.nodes.items():
    		#print("keyname:", key.name)
    		if(key.name == u):
    			value.append(v)
    		elif(key.name == v):
    			value.append(u)
    		#print(key, value)		

    def nomear(self):
    	i=1
    	for key, value in self.nodes.items():
			key.name = i
			i=i+1

    def bfs(self,vert,i):
    	
    	vert[i][0].color = 'gray'
    	vert[i][0].pred = None
    	#print("name: ", vert[i][0].name)
    	queue=[]
    	queue.append(vert[i])
    	#print("queue: ", queue)
    	while(len(queue)>0):
    		u = queue.pop()
    		neighbors = u[1]
    		#print("neighbors: ",neighbors)
    		for n in neighbors:
    			
    			#print("vizinho n",self.nodes.items()[n-1][0])
    			if(self.nodes.items()[n-1][0].color == 'white'):
    				#print("n", n)
    				self.nodes.items()[n-1][0].color = 'gray'
    				self.nodes.items()[n-1][0].dist = u[0].dist+6
    				self.nodes.items()[n-1][0].pred = u[0].name
    				queue.append(self.nodes.items()[n-1])  
    			#print(n)
    		u[0].color = 'black'
    		#queue.pop()
    	"""print(queue)

    	for n in vert[0][1]:
    		print("...",n)
    		queue.append(self.nodes.items()[n])
    	print("len: ", len(queue))"""
    	


if __name__ == "__main__":
 	
 	

 	q = int(input())
 	i=0
 	ans=[]
 	#print("q: ",q)
 	while i < q:
 		g = Graph()
 		nodes,edges = raw_input().split(" ")
 		#print(nodes, edges)
 		g.initialize_nodes(int(nodes))
 		g.nomear()
 		#print("len:", len(g.nodes))
 		for e in range(1,int(edges)+1):
 			#print(e)
 			e1,e2=raw_input().split(" ")
 			g.create_edges(int(e1),int(e2))
 		i=i+1
 		starting_node = input()-1

 		g.bfs(g.nodes.items(),starting_node)

	 	for k,v in g.nodes.items():
	 		if(len(v) == 0 or k.color == 'white'):
	 			k.dist = -1

	 	res=[]
	 	for k,v in g.nodes.items():
	 		if(k.dist!=0):
	 			res.append(k.dist)
	 	
	 	ans.append(res)
	 	#print(ans)

 	for x in ans:
 		sys.stdout.write(" ".join(str(i) for i in x) + "\n")


 	"""g.create_edges(1,4)
 	g.create_edges(1,2)
 	g.create_edges(3,4)
 	g.create_edges(2,3)
 	g.create_edges(4,2)
 	g.create_edges(5,6)
 	g.create_edges(6,7)"""

 	

 	
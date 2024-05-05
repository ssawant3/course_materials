# #DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
# class Dijkstra:


#     def Dijkstra_alg(self, n, e, mat, s):
#         graph=[]
#         for i in range(n):
#             graph.append([-1]*(n))
        
#         for i in range(e):
#             u = mat[i][0]
#             v = mat[i][1]
#             w = mat[i][2]
#             graph[u-1][v-1]=w
#             graph[v-1][u-1]=w
        
#         output=[]
#         for i in range(n):
#             output.append([float("inf"),0,False])
        
#         def find_shortest_value_vertex(output):
#             minimum=float("inf")
#             vertex= None
#             for i in range(len(output)):
#                 if(output[i][0]<minimum and output[i][2]==False):
#                     minimum=output[i][0]
#                     vertex=i
#             return vertex
#         output[s-1][0]=0
#         output[s-1][1]=1

#         for i in range(n):
#             curr=find_shortest_value_vertex(output)
#             output[curr][2]=True
#             for j in range(n):
#                 if(graph[curr][j]!=-1 and output[j][2]==False and output[curr][0]!=float("inf") 
#                    and output[curr][0]+graph[curr][j]<output[j][0]):
#                     output[j][0]=output[curr][0]+graph[curr][j]
#                     output[j][1]=output[curr][1]
#                 elif(graph[curr][j]!=-1 and  output[curr][0]+graph[curr][j]==output[j][0]):
#                     output[j][1]=0
     
#         for i in range(len(output)):
#             output[i]=output[i][:2]
#         return output
#         return 0
#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class Dijkstra:


    def Dijkstra_alg(self, n, e, mat, s):
        
        def shortValV(opt):
            min=float("inf")
            vtx= None
            for i in range(len(opt)):
                if(opt[i][0]<min and opt[i][2]==False):
                    min=opt[i][0]
                    vtx=i
            return vtx

        G=[]
        for i in range(n):
            G.append([-1]*(n))
        
        for i in range(e):
            u = mat[i][0]
            v = mat[i][1]
            w = mat[i][2]
            G[u-1][v-1]=w
            G[v-1][u-1]=w
        
        opt=[]
        for i in range(n):
            opt.append([float("inf"),0,False])
        
        opt[s-1][0]=0
        opt[s-1][1]=1

        for i in range(n):
            current=shortValV(opt)
            opt[current][2]=True
            for j in range(n):
                if(G[current][j]!=-1 and opt[j][2]==False and opt[current][0]!=float("inf") 
                   and opt[current][0]+G[current][j]<opt[j][0]):
                    opt[j][0]=opt[current][0]+G[current][j]
                    opt[j][1]=opt[current][1]
                elif(G[current][j]!=-1 and  opt[current][0]+G[current][j]==opt[j][0]):
                    opt[j][1]=0
     
        for i in range(len(opt)):
            opt[i]=opt[i][:2]
        return opt



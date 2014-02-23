'''
Created on Jan 29, 2011

@author: Robin Willis
'''

import rhinoscriptsyntax as rs
from System.Drawing import Color

class MinimalSpanningTree:
    
    def __init__(self, points, curves):
        
        #input
        self.points = points
        self.triangles = curves
        self.pointCount = len(points)
        self.triangleCount = len(curves)
        #output
        self.nodes = {}
        self.branches = []
        
        #print "New instance of the MinimalSpanningTree class created."
        #print ">>", self.pointCount, "points. >>",self.triangleCount," triangles."
        
        
    def buildTree(self):
        
        #pydev doesnt like rs.filter.*
        pointFilter = 1
        curveFilter = 4
             
        lines={}
        
        #convert triangles to lines
        for i in range(len(self.triangles)):
            #remove duplicate geometry (no operation for this so we use the command prompt)
            if rs.IsCurveClosed(self.triangles[i]):
                rs.ExplodeCurves(self.triangles[i], True)
                rs.Command("_SelDup")
                rs.Command("_delete")
        
        
        rs.Command("_SelCrv")
        curves=rs.GetObjects(None,curveFilter,True,True)

        #Guid to Curve End Points
        for j in range(len(curves)):
            curveSP = rs.CurveStartPoint(curves[j])
            curveEP = rs.CurveEndPoint(curves[j])
            lines[j] = [curveSP,curveEP]
        
        #Guid to Point Coordinates
        nodes = {}
        for i in range(len(self.points)):
            nodes[i] = rs.PointCoordinates(self.points[i])
            
        nodeDict ={}
        
        #build nodeDict
        #adding all these lines is really not necessary and left over from an old way I was trying to calculate things
        #at the end of the day all the calculations are done with just the points blah
        #erri take it back - we do need the end start set but not the branch set
        #we use the endpoints of each line to find out which nodes are connected by a line
        #not the best naming of variables going on here either
        for i in range(len(nodes)):
            branchSet = []
            endStartSet = []
            for j in range(len(lines)):

                if lines[j][0] == nodes[i] or lines[j][1] == nodes[i]:
                    #lineObj=rs.AddLine(lines[j][0],lines[j][1])
                    #branchSet.append(lineObj)
                    endStart =  [lines[j][0],lines[j][1]]
                    endStartSet.append(endStart)

            #nodeDict Structure
            nodeDict[i]=[nodes[i],branchSet, endStartSet]

        #create empty dict for processed nodes and get first node to start calculation
        testNodes={}
        path=[]
        testNodes[0] = nodeDict[0]
        
        
        
        #clean up input curves
        
        pathLayer = rs.AddLayer("MINIMAL SPANNING TREE", Color.CornflowerBlue)
        rs.CurrentLayer(pathLayer)
        
        #calculate the tree
        
        self.genPath(nodeDict,testNodes,path, 0)
        

    def genPath(self,nodeDict,testNodes,path,cycle):
        print "START PAth - CYCLE ",cycle
        
        queryNodes = self.getConnectedNodes(testNodes, nodeDict)
              
        #for j in range(len(queryNodes)):
            #rs.AddCircle(queryNodes[j][0],3)
    
        closestNieghbor = self.getClosestNode(testNodes,queryNodes)
        #rs.AddCircle(closestNieghbor[0][0],10)
        #rs.AddCircle(closestNieghbor[1][0],5)

        branch = rs.AddLine(closestNieghbor[0][0], closestNieghbor[1][0])
        path.append(branch)
        
        testNodes[len(testNodes)] = closestNieghbor[1]
        cycle = cycle + 1
        if (cycle < len(nodeDict)-1):
            self.genPath(nodeDict,testNodes,path,cycle)
        else:
            self.nodes = testNodes
            self.branches = path
    
    def getClosestNode(self,testNodes,queryNodes):
        
        neighbors = {}
        #there must be a better way to do this
        bestDistance = 10000000000000000
        for i in range(len(testNodes)):
            for j in range(len(queryNodes)):
                distance = rs.Distance(testNodes[i][0], queryNodes[j][0])
                if(distance<bestDistance):
                    bestDistance = distance
                    neighbors[0] = testNodes[i]
                    neighbors[1] = queryNodes[j]

        return neighbors
        
    
    def getConnectedNodes(self, nodes, nodeDict):
        connectedNodes = []
        for i in range(len(nodeDict)):
                
            if(self.isNodeChecked(nodeDict[i],nodes) == False):
                for k in range(len (nodes)):
                    for j in range(len(nodeDict[i][2])):
                        for l in range(len(nodes[k][2])):
                            if(nodeDict[i][2][j] == nodes[k][2][l]):
                                connectedNodes.append(nodeDict[i])
        return connectedNodes
    
    def isNodeChecked(self, node, nodes):
        checked = False
        for i in range(len(nodes)):
            if (node[0] == nodes[i][0]):
                checked = True
        return checked


#for testing
#pts = rs.GetObjects("get points", rs.filter.point)
#tri = rs.GetObjects("get triangles",rs.filter.curve)

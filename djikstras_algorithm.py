# Dijkstra's Alogrithm


# Node Format: Node = "label": [ [nbrLabel, workingValue], orderID, finalValue, [nbrs], visited]
# workingValues: [0]
# orderID: [1]
# finalValue: [2]
# nbrs: [3]
# visited: [4]

# Example Node: NodeA = "C": [ [["A", 7], ["B", 8]], 3, 7, [["A", 5], ["B", 3], ["E", 3]], True]







class Tree:
   
   def __init__(self, nodes):
   
      self.nodes = {
         "A": [ [], None, None, [["B", 5], ["C", 7], ["D", 8]], False],
         "B": [ [], None, None, [["A", 5], ["C", 3], ["E", 4], ["G", 16]], False],
         "C": [ [], None, None, [["A", 7], ["B", 3], ["E", 3]], False],
         "D": [ [], None, None, [["A", 8], ["E", 6]], False],
         "E": [ [], None, None, [["B", 4], ["C", 3], ["F", 3], ["G", 8]], False],
         "F": [ [], None, None, [["D", 6], ["E", 3], ["G", 8]], False],
         "G": [ [], None, None, [["B", 16], ["E", 10], ["F", 8]], False],
      }
      
      

   def return_node(self, label):
      
      if label not in self.nodes:
         raise ValueError(f"Node '{label}' was not found")
      
      return self.nodes[label]
         




class Node:
   
   def __init__(self, label, nbrs): # nbrs means neighbours
      
      self.label = label
      self.workingValues = []
      self.orderID = None
      self.finalValue = None
      self.nbrs = nbrs
      
      
      


   
def shortest_path(startNode, endNode):
   

   
   try:
      startNode = Tree.return_node(startNode) # Tests start node is valid and assigns it
      endNode = Tree.return_node(endNode) # Test that the end node is valid and assigns it
      
   except ValueError as error:
      print(f"Error: {error}")
      
   
   startNode[1] = 1 # [1] is the OrderID, 1 because its the first node; start node
   startNode[2] = 0 # [2] is the finalValue, 0 because it has no weight (its the start)
   startNode[4] = True # [4] is the visited flag, visited = True

   
   
   timesVisitedEndNode = 0
   visitedNodes = []
   focusNode = startNode
   firstPass = True
   orderID = 0
   
   while timesVisitedEndNode < len(Tree.return_node(endNode)[3]): # Finds the degree of the end node
         
      orderID += 1
      
      if not firstPass:
         
         # Adds nodes which have been visited to a visitedNodes list
               for node in Tree.nodes:
                  if node[4] and not node[2]: # If the node has been visited and doesnt have a finalValue
                     visitedNodes.append(node)
                      
                      
                      
               # Find smallest working value
               smallestWorkingValue_graph = next(iter(visitedNodes.values()))[0][1] # First working value of the first visited node
               for visitedNode in visitedNodes:
                  
                  smallestWorkingValue_node =                    # Looks up the smallest workingValue in each node
                  if smallestWorkingValue_node < smallestWorkingValue_graph: # Finds smallest workingValue of a node
                     smallestWorkingValue_graph = smallestWorkingValue_node
                     focusNode = visitedNode
           
      else:
         continue

      
      focusNode[2] = orderID
      focusNode[3] = min(focusNode[1]) # Assigns finalValue to focusNode
      
      
      
      # Visits the nbrs of the focusNode and changes the nbrs of the focusNode to visited
      for nbr in focusNode[4]: # the neighbours of the focusNode
         
         lookupWeight = dict(nbr[4]) # finds weight of the connection from nbr to focusNode 
         workingValue = focusNode[3] + lookupWeight(focusNode) # finalValue of focusNode + weight from nbr to focusNode

         nbr[5] = True # visited = True
         
         nbr[1].append(workingValue, focusNode[0]) # appends a new working value (doesnt erase previous working values, added to list)
                  
      
      timesVisitedEndNode = 0
      for nbr in endNode:
         
         if nbr[3] is not None: # If the endNode's nbr has visited it
            timesVisitedEndNode += 1
            
            
      firstPass = False
      
# if focusNode finalVal - weight = nbr finalVal, correct path

   focusNode = endNode
   
   while True:
      
      if focusNode[0] == startNode[0]: # If you have reached the beginning
         break
      
      
      # [5, "A"], [3, "C"], [4, "E"], [16, "G"]
      
      for workingValues in focusNode[1]:
         
         for workingValue, label in workingValues:
            weight = dict(focusNode[4])[workingValue]
            
            if focusNode[3] - 
      
   
   
      shortestPath = 
   
   



startNode = "A" # Replace with user input
endNode = "G" # Replace with user input


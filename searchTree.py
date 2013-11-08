import time 
from math import log
# Node: {parent, num_times_visited, (player_1_reward,player_2_reward)}

Class SearchTree:
    self.searchTree = ({'parent':none, 'num_vist': 0, 'reward':(0.0,0.0)},'childs':[]) # root node

# Defines heuristic for choosing the best child
    def pickChild(self,currNode,player):
        
        kids = self.generateChildren(currNode)
        
        max = -100.0
        favorite = none
        for c in kids:
            if c['num_vist'] == 0:
                max = 10000  # want to set very high so will explore children before expanding other children
                favorite = c
            else if max < c['num_visit']/c['reward'][player] + 2*cp*sqrt(2*log1p(currNode['num_vist'])/c['num_visit']):
                max =  c['num_visit']/c['reward'][player] + 2*cp*sqrt(2*log1p(currNode['num_vist'])/c['num_visit']
                favorite = c
        return favorite

# Generates all the possible children of the node
    def generateChildren(self,node):
        acts = getActions(node);  # TODO:: getActions() needs to be defined by the game state
        states = []
        for a in acts:
            states.append(getState(node,a))  # getState() should return Node dictionaries
        return states


# Propogate Value up through tree
    def backup(self):
        pass

# Add a child to the current search tree
    def addChild(self, child_node):
        pass

# Run a simulation through the node
    def runSimuation(self,node):
        pass

# Main algorithm for search tree
    def findBestMove(self,player):
        
        while(time_up == false):
            # Find a leaf node to simulate from
            simNode = self.getSimulationNode()
            # Run simulations from leaf node
            bestNode = self.runSimulation(simNode)
            # Add best child to tree
            simNode['kids'].append(bestNode)
            # Return best move
            if(



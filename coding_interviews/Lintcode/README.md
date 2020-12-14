# Lintcode Ladder 

## GS
[591. Connecting Graph III](https://www.lintcode.com/problem/connecting-graph-iii/description?_from=ladder&&fromId=171)
- Union-find

__Union-find template__

```python
# initialization
def __init__(self, num_nodes):
    self.num_nodes = num_nodes
    self.father = {}

    for i in range(1, num_nodes+1):
        self.father[i] = i

# find the father for the node
def find(self, node):
   
    path = []
    x = node
    while(self.father[x] != x):
        path.append(x)
        x = self.father[x]
    
    for p in path:
        self.father[p] = x
    
    return self.father[x]

# union two nodes
def connect(self, node1, node2):
    father1 = self.find(node1)
    father2 = self.find(node2)

    if father1 != father2:
        self.father[father1] = father2

```
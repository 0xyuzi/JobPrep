from collections import defaultdict
def trans_string(str1, str2):
    """
    str1: the source string
    str2: the target string

    return: minimum number of operations to transform str1 to str2
    """
    
    # first check if two string are the same
    if str1 == str2:
        return 0
    
    # check if the str2 have full set of the eng chars (26)
    if len(set(str2))==26:
        return -1
    
    # build the undirected graph (V,E) as (source_char, target_char), if source_char has more than 1 diff target char, return -1 
    graph = {}

    indgree = defaultdict(int)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] not in graph :
                graph[str1[i]] = str2[i]
                indgree[str2[i]] += 1 
            else:
                if graph[str1[i]] != str2[i]:
                    return -1 
        

    
    
    print(graph, indgree)
    res = 0

  
    
    num_nodes = is_cycle(graph, indgree)
    if num_nodes != 0:
        print(num_nodes)
        res += 1+ num_nodes
        
    
    res += len(graph) 
        

    print(res, graph, indgree)

    return res 


def is_cycle(graph, indegree):
    """
    detect if have cycle and delete the nodes in cycle if node's indegree less than 2
    return: number of nodes in the cycle, if not cycle, return 0

    """

    # detect if have cycle and return the cycle endpoint
    end_node, num_nodes = cycle_detected(graph)
    print(f" is_cycle: end_node {end_node}, num_nodes {num_nodes}")
    # remove nodes in the cycle if which has less than 2 indegrees
    if end_node:
        remove_nodes(end_node, graph, indegree)
        print(f"remove nodes of the cycle start from {end_node}")
        return num_nodes
    else:
        return 0


def cycle_detected(graph):
    print("cycle_detected function")
    for v in graph:
        print(f"vertex {v}")
        end_node = dfs(v, graph[v], graph)
        print(f"end_node: {end_node}")
        if end_node == v:
            print(f"end_node sames as vertice")
            num_nodes = count_nodes(end_node, graph)
            print(f"num_nodes {num_nodes}")
            return end_node, num_nodes
    # if not found cycle 
    return None, None


def dfs(v, node,graph):
    print(node)    
    if v == node:
        return node 

    if node in graph:
        node = dfs(v, graph[node], graph)
        return node 
    else:
        return None 

    

def count_nodes(node, graph):
    
    v = graph[node]
    
    count = 1
    
    while (v != node):
        count += 1 
        v = graph[v]
    
    return count 
    
def remove_nodes(end_node, graph, indegree):
    print("remove_nodes")
    visited = set()
    visited.add(end_node)
    indegree[end_node] -=  1
    node = graph[end_node] 
    
    
    while node != end_node:
        indegree[node] -=  1
        if indegree[node] == 0:
            print(f"graph and indegree of node {node} since its indegree is 0")
            visited.add(node)
            node = graph[node]
           
        else:
            node = graph[node]

    for v in visited:
        print(f"remove {v} from the graph")
        del graph[v]




if __name__ == "__main__":
    # abcd -> bcaa
    str1 = "abcd"
    str2 = "bcaa"

    print(trans_string(str1, str2))




  




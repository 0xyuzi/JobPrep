class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """

    def topologicalSortNumber(self, n, p):
        # Write your code here

        def dfs(visited, visited_count, graph, indegree, memo):
            if visited_count == len(graph):
                return 1

            if visited in memo:
                return memo[visited]

            ret = 0
            for n in graph:
                if indegree[n] == 0 and visited & (1<<n) == 0:

                    visited |= 1<<n
                    visited_count += 1

                    for sub in graph[n]:
                        indegree[sub] -= 1

                    ret += dfs(visited, visited_count, graph, indegree, memo)

                    for sub in graph[n]:
                        indegree[sub] += 1
                    
                    visited_count -= 1    
                    visited &= ~(1<<n)
            
            memo[visited] = ret
            return ret

        graph = {i: set() for i in range(n)}
        indegree = {i: 0 for i in range(n)}
        visited = 0

        for take, take_first in p:
            # take_first -> take (indegree++)
            # take is depends on take_first
            graph[take_first].add(take)
            indegree[take] += 1

        return dfs(visited, 0, graph, indegree, {})
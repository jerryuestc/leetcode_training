# leetcode_training

## DFS algorithm

### DFS三要素

1 已VISIT点的集合
2 确定相邻点的方式

伪代码

n = number of nodes in the graph
g = adjacency list representing the graph
visited = [false, false, ...]

function dfs(at)
    if visited[at]: return
    visited[at] = true
    neighbors = graph[at]
    for next in neighbors:
        dfs(next)

startnode = 0
dfs(start_node)
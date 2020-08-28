"""

对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，
使得图中任意一对顶点u和v，若边(u,v)∈E(G)，则u在线性序列中出现在v之前。
通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列，简称拓扑序列。
简单的说，由某个集合上的一个偏序得到该集合上的一个全序，这个操作称之为拓扑排序。
在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，
称为该图的一个拓扑排序（英语：Topological sorting）：
每个顶点出现且只出现一次；
若A在序列中排在B的前面，则在图中不存在从B到A的路径。

"""


def toposort(graph):
    in_degrees = dict((u,0) for u in graph) # 初始化所有顶点入度为0
    vertex_num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1  # 计算每个顶点的入度
            q = [u for u in in_degrees if in_degrees[u] == 0] # 筛选入度为0的顶点
            seq = []
    while q:
        u = q.pop()  # 默认从最后一个删除
        seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1  # 移除其所有指向
            if in_degrees[v] == 0:
                q.append(v)   # 再次筛选入度为0的顶点
        if len(seq) == vertex_num:  # 如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
            return seq
        else:
            print("there's a circle.")


G = {
 'a': 'bce',
 'b': 'd',
 'c': 'd',
 'd': '',
 'e': 'cd'
}
print(toposort(G))
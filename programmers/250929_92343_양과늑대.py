"""
Date 25.09.29
양과 늑대
URL
https://school.programmers.co.kr/learn/courses/30/lessons/92343
"""


def search_paths(cur_node, nodes, sheep_cnt, wolf_cnt, counting_log, graph, info):

    nodes.remove(cur_node)

    for child in graph[cur_node]:
        nodes.append(child)

    if info[cur_node] == 0:  # sheep
        sheep_cnt += 1
    else:  # wolf
        wolf_cnt += 1

    counting_log.append(sheep_cnt)

    possible_visit = []
    for node in nodes:
        if info[node] == 0 or sheep_cnt > wolf_cnt + 1:
            possible_visit.append(node)

    for next_node in possible_visit:
        search_paths(next_node, nodes[:], sheep_cnt, wolf_cnt, counting_log, graph, info)


def solution(info, edges):

    # graph의 i번째 원소는 i-th node에 연결된 node의 목록을 원소로 갖는 list
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    print(graph)
    cur_node = 0
    nodes = [0]
    counting_log = []
    search_paths(cur_node, nodes, 0, 0, counting_log, graph, info)

    return max(counting_log)


info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
print(solution(info, edges))

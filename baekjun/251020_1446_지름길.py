"""
Date: 2025.10.20
지름길 (그래프, 다익스트라 or 데이크스트라)

"""

if __name__ == "__main__":
    with open("./coding_test/baekjun/input.txt", "r") as f:
        num_routes, len_highway = map(int, f.readline().split(" "))
        graph = [tuple(int(item) for item in row.split(" ")) for row in f.readlines()]

    # print(num_routes, len_highway)
    print(graph)

    nodes = set()

    for start_pos, end_pos, len_route in graph:
        nodes.update([start_pos, end_pos])

    nodes = sorted(nodes)
    least_dist = [min(nodes)] + [float("inf")] * (len(nodes) - 1)
    print(nodes)
    print(least_dist)

    cur_node = 0
    visited = [0] * len(nodes)
    visited[0] = 1

    while True:

        for start_node, end_node, len_route in graph:
            if cur_node > start_node:
                continue
            if least_dist[cur_node] + len_route < least_dist[nodes.index(start_node)]:
                least_dist[nodes.index(start_node)] = least_dist[cur_node] + len_route
        visited[cur_node] = 1
        for node in visited:
            if not node:
                cur_node = 
                break
        not_visited_node_indices = [idx for idx, visit_flag in enumerate(visited) if not visit_flag]
        for not_visited_node_idx in not_visited_node_indices:
             = min(nodes)

    #     for idx, route in enumerate(graph):
    #         start_node, end_node, len_route = route
    #         if cur_node > start_node:
    #             continue
    #         if (least_dist[cur_node] + len_route) < least_dist[idx]:
    #             least_dist[idx] = least_dist[cur_node] + len_route

    #     visited[cur_node] = 1
    #     cur_node = idx for idx in range(len(num_routes)) if visited[idx] == 0 and

    #     start_node, end_node, len_route = graph[idx]

    #     if cur_node > start_node:
    #         idx += 1
    #         continue

    #     if

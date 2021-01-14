INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node(distance, visited):
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(n, m, information, start):
    # 모든 노드의 연결 정보를 그래프화 하기
    graph = [[] for _ in range(n + 1)]
    for data in information:
        # data[0] -> data[1]로 가는 비용이 data[2]
        graph[data[0]].append((data[1], data[2]))
    # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
    visited = [False] * (n + 1)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)

    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node(distance, visited)
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    return distance[1:]

n, m = 6, 11
start = 1
information = [
    [1, 2, 2],
    [1, 3, 5], # 노드 1 -> 노드 3으로 가는 비용이 5
    [1, 4, 1],
    [2, 3, 3],
    [2, 4, 2],
    [3, 2, 3],
    [3, 6, 5],
    [4, 3, 3],
    [4, 5, 1],
    [5, 3, 1],
    [5, 6, 2]
]

# 다익스트라 알고리즘 수행
print(dijkstra(n, m, information, start))
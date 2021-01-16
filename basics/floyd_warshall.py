INF = int(1e9)
def floyd_warshall(n, m, connections):
    distance = [["INFINITY"] * n for _ in range(n)]

    # 2차원 리스트로 그래프를 만들고 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # 자기 자신에게 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    # 각 노드의 연결 정보 업데이트
    for data in connections:
        # data[0] -> data[1]로 가는 비용은 data[2]
        graph[data[0]][data[1]] = data[2]

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과를 저장
    for a in range(n):
        for b in range(n):
            if graph[a + 1][b + 1] != INF:
                distance[a][b] = graph[a + 1][b + 1]
    return distance

n = 4 # 노드 개수
m = 7 # 간선 개수
connections = [
    [1, 2, 4],
    [1, 4, 6],
    [2, 1, 3],
    [2, 3, 7],
    [3, 1, 5],
    [3, 4, 4],
    [4, 3, 2]
]
print(floyd_warshall(n, m, connections))
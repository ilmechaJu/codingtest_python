#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    DFS(깊이 우선 탐색)은 그래프나 트리를 탐색하는 알고리즘 중 하나로,
#    루트 노드(혹은 다른 임의의 노드)에서 시작하여 마지막 노드까지 깊이를 우선하여 탐색하는 알고리즘입니다.
#    재귀함수 혹은 스택을 사용하여 구현할 수 있습니다.

# 2. 예시 입력 / 출력:
#    입력: graph = {1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, start_node = 1
#    출력: [1, 2, 4, 5, 3]

# 3. 알고리즘의 시간 복잡도:
#    O(V + E) (V: 정점의 개수, E: 간선의 개수)

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 경로 찾기
#    - 사이클 탐지
#    - 그래프 연결 성분 찾기

# 5. DFS 상세 과정:
#    - 시작 노드(1)를 스택에 넣고, 방문 처리를 한다.
#    - 노드 1에서 방문하지 않은 인접 노드(2와 3) 중 하나(2)를 선택하여 스택에 넣고 방문 처리한다.
#    - 노드 2에서 방문하지 않은 인접 노드(4와 5) 중 하나(4)를 선택하여 스택에 넣고 방문 처리한다.
#    - 노드 4에서 더 이상 방문하지 않은 인접 노드가 없으므로, 스택에서 노드 4를 꺼내고, 이전 노드(2)로 돌아간다.
#    - 노드 2에서 아직 방문하지 않은 노드(5)를 스택에 넣고 방문 처리한다.
#    - 노드 5에서 더 이상 방문하지 않은 인접 노드가 없으므로, 스택에서 노드 5를 꺼내고, 이전 노드(2)로 돌아간다.
#    - 노드 2에서 더 이상 방문하지 않은 인접 노드가 없으므로, 스택에서 노드 2를 꺼내고, 이전 노드(1)로 돌아간다.
#    - 노드 1에서 아직 방문하지 않은 노드(3)를 스택에 넣고 방문 처리한다.
#    - 노드 3에서 더 이상 방문하지 않은 인접 노드가 없으므로, 스택에서 노드 3을 꺼낸다.
#    - 위 과정을 더 이상 수행할 수 없을 때까지 반복한다.

def dfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            print(str(node)+" ") #방문 노드를 출력하기 위한 코드
            visited[node] = 1
            stack.extend(reversed(graph[node]))  # reversed를 사용하여 깊이 우선 탐색을 유지
    return visited

# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# DFS 알고리즘 실행
result = dfs(graph, 1)
# 출력: 1 2 4 5 3

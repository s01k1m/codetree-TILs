def solution(tickets):
    answer = []
    l = len(tickets)
    
    stack = ["ICN"]  # always start from Incheon
    route = ["ICN"]  # initialize route with starting point
    visited = [0] * l

    tickets.sort(key=lambda x: (x[0], x[1]))  # sort tickets to use lexicographically smallest route

    def dfs(route):
        if len(route) == l + 1:  # if the route includes all tickets + start point
            answer.append(route[:])
            return

        last = route[-1]
        for idx, (start_air, end_air) in enumerate(tickets):
            if not visited[idx] and start_air == last:
                visited[idx] = 1
                route.append(end_air)
                
                dfs(route)
                
                route.pop()
                visited[idx] = 0
    
    dfs(route)
    
    answer.sort()
    return answer[0]



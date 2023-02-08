class Solution:
    def numBusesToDestination(self, routes: List[List[int]], s: int, t: int) -> int:
        if s == t: return 0
        routes = [set(bus) for bus in routes]
        bus_graph = defaultdict(set)
        for i,bus in enumerate(routes):
            for stop in bus:
                for j in range(i+1,len(routes)):
                    if stop in routes[j]:
                        bus_graph[i].add(j)
                        bus_graph[j].add(i)

        seen, target= set(),set()
        for idx,bus in enumerate(routes):
            if s in bus:
                seen.add(idx)
            if t in bus:
                target.add(idx)

        queue = deque(list(seen))
        num_bus = 0
        while queue:
            num_bus += 1
            n = len(queue)
            for _ in range(n):
                bus_stop = queue.popleft()
                if bus_stop in target:
                    return num_bus
                for nei in bus_graph[bus_stop]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
                        

        return -1

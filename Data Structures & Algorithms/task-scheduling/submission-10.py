class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_map = defaultdict(list)
        max_heap, cooldown_arr = [], []
        time = 0

        for task in tasks:
            tasks_map[task] = tasks_map.get(task, 0) - 1

        for count in tasks_map.values():
            heapq.heappush(max_heap, count)

        while max_heap or cooldown_arr:
            if not max_heap:
                time_add = cooldown_arr[0][1] - time
                count = cooldown_arr.pop(0)[0]

                heapq.heappush(max_heap, count)
                time += time_add
            else:
                if cooldown_arr and cooldown_arr[0][1] == time:
                    heapq.heappush(max_heap, cooldown_arr.pop(0)[0])

            task = heapq.heappop(max_heap)
            task += 1
            time += 1

            if task < 0:
                cooldown_arr.append([task, time + n])

        return time
        
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_map = defaultdict(list)
        max_heap, cooldown_arr = [], []
        res, time = 0, 0

        for task in tasks:
            tasks_map[task] = tasks_map.get(task, 0) - 1

        for char, count in tasks_map.items():
            heapq.heappush(max_heap, [count, char])

        while max_heap or cooldown_arr:
            if not max_heap:
                res += (n + 1) - time
                time = 0

                while cooldown_arr:
                    heapq.heappush(max_heap, cooldown_arr.pop(0))

            if max_heap:
                if time == n + 1 and cooldown_arr:
                    time -= 1
                    heapq.heappush(max_heap, cooldown_arr.pop(0))
                else:
                    curr_task = heapq.heappop(max_heap)
                    COUNT = 0

                    curr_task[COUNT] += 1

                    if curr_task[COUNT] < 0:
                        cooldown_arr.append(curr_task)

                    time += 1
                    res += 1

        return res
        
        
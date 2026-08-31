class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [None] + stones

        self.build_max_heap(stones)

        while len(stones) > 2:
            stone_1 = self.remove_root(stones)
            self.max_heapify(stones, len(stones), 1)
            stone_2 = self.remove_root(stones)
            stones.append(abs(stone_1 - stone_2))
            self.build_max_heap(stones)

        return stones[1]

    def remove_root(self, arr):
        root_node = arr[1]

        arr[1] = arr[len(arr) - 1]
        arr.pop()
        self.max_heapify(arr, len(arr), 1)

        return root_node

    def max_heapify(self, arr: List[int], arr_size: int, node_index: int):
        l = node_index * 2
        r = node_index * 2 + 1

        largest = node_index

        if l < arr_size and arr[l] > arr[largest]:
            largest = l

        if r < arr_size and arr[r] > arr[largest]:
            largest = r

        if largest != node_index:
            arr[node_index], arr[largest] = arr[largest], arr[node_index]
            self.max_heapify(arr, arr_size, largest)

    def build_max_heap(self, arr: List[int]):
        arr_size = len(arr)

        for i in range(arr_size // 2, 0, -1):
            self.max_heapify(arr, arr_size, i)




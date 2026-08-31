class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = [None] + nums, k
        self.build_min_heap(self.heap)

        while len(self.heap) - 1 > self.k:
            self.heap.pop(1)
            self.min_heapify(self.heap, len(self.heap) - 1, 1)

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.build_min_heap(self.heap)
        
        if len(self.heap) - 1 > self.k:
            self.heap.pop(1)
            self.build_min_heap(self.heap)

        return self.heap[1] 

    def min_heapify(self, arr: List[int], arr_size: int, node_index: int):
        l = node_index * 2
        r = node_index * 2 + 1

        smallest = node_index

        if l < arr_size and arr[l] < arr[node_index]:
            smallest = l

        if r < arr_size and arr[r] < arr[smallest]:
            smallest = r

        if smallest != node_index:
            arr[smallest], arr[node_index] = arr[node_index], arr[smallest]
            self.min_heapify(arr, arr_size, smallest)

    def build_min_heap(self, arr: List[int]):
        arr_size = len(arr)

        for i in range(arr_size // 2, 0, -1):
            self.min_heapify(arr, arr_size, i)

    


        

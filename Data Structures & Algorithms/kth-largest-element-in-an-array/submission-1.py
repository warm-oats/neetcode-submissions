class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [None] + nums
        res = 0

        self.build_max_heap(nums)

        while k > 0:
            res = self.heap_pop(nums)
            k -= 1

        return res
            
    def heap_pop(self, arr):
        popped = arr[1]

        arr[1] = arr[len(arr) - 1]
        arr.pop()
        self.max_heapify(arr, len(arr), 1)

        return popped
        
    def max_heapify(self, arr, arr_size, node_index):
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

    def build_max_heap(self, arr):
        arr_size = len(arr)

        for i in range(arr_size // 2, 0, -1):
            self.max_heapify(arr, arr_size, i)
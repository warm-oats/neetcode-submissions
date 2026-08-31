class Solution:
    def kClosest(self, points, k):
        max_heap = [None]
        res = []

        for x, y in points:
            dist = -((x ** 2) + (y ** 2))
            max_heap.append([dist, x, y])

        self.build_max_heap(max_heap)

        while k > 0:
            dist, x, y = max_heap[1]
            res.append([x,y])

            max_heap[1] = max_heap[len(max_heap) - 1]
            max_heap.pop()
            self.max_heapify(max_heap, len(max_heap), 1)
            
            k -= 1

        return res
        
    def max_heapify(self, arr, arr_size: int, node_index):
        l = node_index * 2
        r = node_index * 2 + 1

        largest = node_index

        DIST = 0

        if l < arr_size and arr[l][DIST] > arr[largest][DIST]:
            largest = l

        if r < arr_size and arr[r][DIST] > arr[largest][DIST]:
            largest = r

        if largest != node_index:
            arr[largest], arr[node_index] = arr[node_index], arr[largest]
            self.max_heapify(arr, arr_size, largest)

    def build_max_heap(self, arr):
        arr_size = len(arr)

        for i in range(arr_size // 2, 0, -1):
            self.max_heapify(arr, arr_size, i)
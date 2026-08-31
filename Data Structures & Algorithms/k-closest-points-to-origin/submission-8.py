class Solution:
    def kClosest(self, points, k):
        min_heap = [None]
        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist, x, y])

        self.build_min_heap(min_heap)

        while k > 0:
            dist, x, y = min_heap[1]
            res.append([x,y])

            min_heap[1] = min_heap[len(min_heap) - 1]
            min_heap.pop()
            self.min_heapify(min_heap, len(min_heap), 1)
            
            k -= 1

        return res
        
    def min_heapify(self, arr, arr_size: int, node_index):
        l = node_index * 2
        r = node_index * 2 + 1

        smallest = node_index

        DIST = 0

        if l < arr_size and arr[l][DIST] < arr[node_index][DIST]:
            smallest = l

        if r < arr_size and arr[r][DIST] < arr[smallest][DIST]:
            smallest = r

        if smallest != node_index:
            arr[smallest], arr[node_index] = arr[node_index], arr[smallest]
            self.min_heapify(arr, arr_size, smallest)

    def build_min_heap(self, arr):
        arr_size = len(arr)

        for i in range(arr_size // 2, 0, -1):
            self.min_heapify(arr, arr_size, i)
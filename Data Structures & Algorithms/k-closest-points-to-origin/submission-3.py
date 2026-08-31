class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [None] + points
        res = []

        self.build_min_heap(points)

        while len(points) > 1 and k > 0:
            res.append(points.pop(1))

            if len(points) > 1:
                self.min_heapify(points, len(points), 1)

            k -= 1

        return res
        
    def min_heapify(self, arr: List[List[int]], arr_size: int, node_index: int):
        l = node_index * 2
        r = node_index * 2 + 1

        smallest = node_index
        smallest_dist = math.sqrt(arr[smallest][0]**2 + arr[smallest][1]**2)

        if l < arr_size:
            l_dist = math.sqrt(arr[l][0]**2 + arr[l][1]**2)
            if l_dist < smallest_dist:
                smallest = l
                smallest_dist = l_dist

        if r < arr_size:
            r_dist = math.sqrt(arr[r][0]**2 + arr[r][1]**2)
            if r_dist < smallest_dist:
                smallest = r

        if smallest != node_index:
            arr[smallest], arr[node_index] = arr[node_index], arr[smallest]
            self.min_heapify(arr, arr_size, smallest)

    def build_min_heap(self, arr: List[List[int]]):
        arr_size = len(arr)

        for i in range(arr_size // 2, 0, -1):
            self.min_heapify(arr, arr_size, i)
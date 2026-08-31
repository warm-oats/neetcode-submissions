class TimeMap:

    def __init__(self):
        self.time_map_hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map_hashmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        current_key_arr = self.time_map_hashmap[key]

        if not current_key_arr:
            return ""
        
        l, r = 0, len(current_key_arr) - 1

        res = ""

        while r >= l:
            mid = (r + l) // 2
            mid_value = current_key_arr[mid][0]
            mid_timestamp = current_key_arr[mid][1]

            if mid_timestamp > timestamp:
                r = mid - 1
            elif mid_timestamp <= timestamp:
                res = mid_value

                l = mid + 1
            else:
                return 
        
        return res
                


            

        


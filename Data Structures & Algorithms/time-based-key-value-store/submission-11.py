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

        current_val_pair = ["", current_key_arr[l][1]]

        while r >= l:
            mid = (r + l) // 2
            mid_value = current_key_arr[mid][0]
            mid_timestamp = current_key_arr[mid][1]

            if timestamp == mid_timestamp:
                return mid_value
            elif mid_timestamp > timestamp:
                r = mid - 1
            elif mid_timestamp < timestamp and timestamp <= current_key_arr[r][1]:
                max_timestamp = max(mid_timestamp, current_val_pair[1])
                new_val = mid_value if max_timestamp == mid_timestamp else current_val_pair[0]

                current_val_pair = [new_val, max_timestamp]

                l = mid + 1
            else:
                return current_key_arr[r][0]
        
        return current_val_pair[0]
                


            

        


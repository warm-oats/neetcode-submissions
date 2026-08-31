class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ''

        VALUE = 0
        TIMESTAMP = 1
        current_list = self.time_map[key]
        start_index = 0
        end_index = len(current_list) - 1
        res = ''

        while end_index >= start_index:
            middle_index = math.floor((start_index + end_index) / 2)

            if current_list[middle_index][TIMESTAMP] == timestamp:
                return current_list[middle_index][VALUE]

            if current_list[middle_index][TIMESTAMP] > timestamp:
                end_index = middle_index - 1
            elif current_list[middle_index][TIMESTAMP] < timestamp:
                if res == '' or res[TIMESTAMP] < current_list[middle_index][TIMESTAMP]:
                    res = current_list[middle_index]
                start_index = middle_index + 1

        return res[VALUE] if res else ''


            

        

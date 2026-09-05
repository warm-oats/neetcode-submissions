class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars_arr = list(zip(position, speed))
        cars_arr.sort(reverse=True)

        pos_i = 0
        speed_i = 1

        cur_fleet_time = (target - cars_arr[0][pos_i]) / cars_arr[0][speed_i]

        for car in cars_arr:
            car_time = (target - car[pos_i]) / car[speed_i]

            if car_time > cur_fleet_time:
                fleets += 1
                cur_fleet_time = car_time

        return fleets + 1

            

            









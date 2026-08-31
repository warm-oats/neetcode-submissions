class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        # Merge speed and position array and sort in ascending order
        cars_arr = list(zip(position, speed))
        POSITION_INDEX = 0
        SPEED_INDEX = 1

        cars_arr.sort(reverse=True)

        current_fleet_time = (target - cars_arr[0][POSITION_INDEX]) / cars_arr[0][SPEED_INDEX]

        for car in cars_arr:
            car_time = (target - car[POSITION_INDEX]) / car[SPEED_INDEX]

            if car_time > current_fleet_time:
                fleets += 1
                current_fleet_time = car_time
        
        return fleets + 1





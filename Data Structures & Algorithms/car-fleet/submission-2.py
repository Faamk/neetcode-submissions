class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = 0
        cars_in_order = sorted((v,k) for k,v in enumerate(position))
        last_arrival = 0
        for pos, i in reversed(cars_in_order):
            my_speed = speed[i]
            my_arrival = (target - pos) / my_speed
            if my_arrival > last_arrival:
                car_fleets +=1
                last_arrival = my_arrival

    
        return car_fleets

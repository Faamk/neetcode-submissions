class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times_arrival = [None] * len(speed)
        cars_in_order = sorted((v,k) for k,v in enumerate(position))
        last_arrival = 0
        print(cars_in_order)
        for pos, i in reversed(cars_in_order):
            my_speed = speed[i]
            my_arrival = (target - pos) / my_speed
            my_arrival = my_arrival if my_arrival > last_arrival else last_arrival
            times_arrival[i] = my_arrival
            last_arrival = my_arrival
    
        return len(set(times_arrival))

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = len(position)

        sorted_pair = sorted(zip(position, speed))

        for idx, (pos, spd) in enumerate(sorted_pair):
            if idx == len(position) - 1:
                return fleet_count

            car_ahead = sorted_pair[idx + 1]
            # 자기 앞 차량보다 빠르고, 도착 전에 따라잡는다면
            if (
                spd > car_ahead[1]
                and (target - pos) / spd >= (target - car_ahead[0]) / car_ahead[1]
            ):
                fleet_count -= 1

        return fleet_count
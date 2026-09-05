class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0

        sorted_pair = sorted(zip(position, speed), reverse=True)

        times = [(target - pos) / spd for pos, spd in sorted_pair]

        branch_time = 0

        for time in times:
            if branch_time < time:
                fleet_count += 1
                branch_time = time

        return fleet_count
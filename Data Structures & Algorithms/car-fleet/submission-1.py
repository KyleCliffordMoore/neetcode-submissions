class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = []

        for pos, vel in cars:
            time = (target - pos) / vel

            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)
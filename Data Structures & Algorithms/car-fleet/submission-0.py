class Solution:
    
    def doesCatchup(self, target: int, posLeft: int, speedLeft: int, posRight: int, speedRight: int) -> bool:

        # Get times of both cars ~ d/v
        timeRight = (target - posRight) / speedRight
        timeLeft  = (target - posLeft)  / speedLeft

        # print(f"Time L:{timeLeft}, Time R:{timeRight}")

        return timeRight >= timeLeft 

    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Assuming more than one vehicle

        # Sort Car Positions
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])        
        pairs.sort(key=lambda pos: pos[0])
        # print(pairs)

        ans = [pairs[-1]]
        pairs.reverse()
        # print(pairs)
        for [pos, spd] in pairs:
            if not self.doesCatchup(target, pos, spd, ans[-1][0], ans[-1][1]):
                print(f"Appending [{pos}, {spd}] b/c greater than [{ans[-1][0]}, {ans[-1][1]}]")
                ans.append([pos, spd])

        return len(ans)
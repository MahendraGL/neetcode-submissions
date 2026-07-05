class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        PosS = []
        stack = []

        for i in range(len(position)):
            PosS.append((position[i], speed[i]))
        
        arr = sorted(PosS)[::-1]

        for i in range(len(position)):
            time = (target - arr[i][0]) / arr[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time) 
        return len(stack)

           

        
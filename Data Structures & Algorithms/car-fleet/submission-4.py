class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sim = [(p, s) for p, s in zip(position, speed)]
        sim.sort(reverse=True)
        stack = []
        for car in sim:
            p, s = car
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
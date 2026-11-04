class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        def can_transport_people(i,j):
            return people[i]+people[j] <= limit

        left = 0
        right = len(people)-1
        boats = 0

        while left <= right:
            if can_transport_people(left, right):
                left += 1

            right -= 1
            boats += 1

        return boats

    # MAIN TAKEWAYS
    # remember to check the corner cases like list empty or with one element
    # sorting is not bad, it can actually help solving the problem
    # becarful in the if conditin having only what's useful
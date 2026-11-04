class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = people.sort()

        def can_transport_people(i,j):
            return people[i]+people[j] <= limit

        left = 0
        right = len(people)-1
        boats = 0

        while left <= right:
            if can_transport_people(left, right):
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1

        return boats
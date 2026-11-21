class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Step 1: If the target is the starting combination, no rotation is needed
        if target == "0000":
            return 0

        # Step 2: Initialize visited with all forbidden combinations
        visit = set(deadends)

        # Step 3: If the starting combination is a deadend, we cannot move
        if "0000" in visit:
            return -1

        # Step 4: Initialize two search frontiers
        # begin: States currently explored from the starting combination
        # end: States currently explored from the target combination
        begin = {"0000"}
        end = {target}

        # Step 5: Track the number of rotations from both directions
        steps = 0

        # Step 6: Continue while both search frontiers have reachable states
        while begin and end:

            # Step 6.1: Always expand the smaller frontier
            # This reduces the number of combinations explored
            if len(begin) > len(end):
                begin, end = end, begin

            # Step 6.2: Move to the next BFS level
            steps += 1

            # Step 6.3: Store all newly discovered combinations
            temp = set()

            # Step 6.4: Explore every combination in the current frontier
            for lock in begin:

                # Step 6.5: Try rotating each of the 4 wheels
                for i in range(4):

                    # Step 6.6: Try both rotation directions (-1 and +1)
                    for j in [-1, 1]:

                        # Step 6.7: Calculate the new digit
                        # Modulo 10 handles circular rotation:
                        # 9 + 1 -> 0
                        # 0 - 1 -> 9
                        digit = str((int(lock[i]) + j) % 10)

                        # Step 6.8: Build the next lock combination
                        # Example: lock = "0000", i = 0, j = 1
                        # nextLock = "1000"
                        nextLock = lock[:i] + digit + lock[i+1:]

                        # Step 6.9: Check whether the two search frontiers meet
                        # If nextLock is already reachable from the opposite side,
                        # we have found a path connecting start and target
                        if nextLock in end:
                            return steps

                        # Step 6.10: Skip deadends and previously visited states
                        if nextLock in visit:
                            continue

                        # Step 6.11: Mark the combination as visited
                        visit.add(nextLock)

                        # Step 6.12: Add it to the next BFS frontier
                        temp.add(nextLock)

            # Step 6.13: Move to the next BFS level
            begin = temp

        # Step 7: Return -1 if no path connects the starting state and target
        return -1
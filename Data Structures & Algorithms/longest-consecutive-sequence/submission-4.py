class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # go through the list and every time i see an element i add it to a set
        # if the previous element is not in the set that number is the start of sequence
        # increase the sequence length and take the max between the current sequnece length and the max seq
        # if it's not the start of the sequence go back and increase the seq length until i find the start of sequence

        max_seq = 0 
        unique_elements = set(nums)

        for  n in unique_elements:
            current_seq = 1

            while n-1 in unique_elements:
                n = n-1
                current_seq+=1

            max_seq = max(max_seq, current_seq)

        return max_seq

        # MAIN TAKEAWAY
        # go through a dry run to spot the errors
        # If i can avoid some operations inside the loops try to take them out (see unique elements)
        # 


        
#By reading the question, it is clear that sorting takes O(n log n) time while hashing can solve our challenge by taking O(n) time. 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Initialize a hashmap/ creates an empty dictionary to store each number in nums
        map_ = {} 
        #Set length as 0, this will keep track of the count of longest sequence
        length = 0 

        for i in nums:
            map_[i] = 1 #pre-fills the dictionary to match the len(nums) with each arbitrary element 1

        #Iterates over each key
        for i in map_.keys(): 
            if i-1 in map_.keys(): continue #check if the previous number exist in the dictionary
            #Keeps track of current sequence length
            current = 1 

            while i+1 in map_.keys(): #check if the next number exists in the dictionary
                #increase both index and length by 1 if the number exists
                i += 1 
                current +=1 

            #Update the length
            length = max(current, length)

        return length

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
 
        freq = [[] for i in range(len(nums) + 1)]   # create a list of lists. the same size of the input  array + 1.
        count = defaultdict()

        # count the nº of occurrences of each number, and register it in the dict
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)    #the number n happens c number of times

        # Extract the k more frequent (from the end to the beginning)
        result = []
        for i in range(len(freq) - 1, 0, -1):   #run it in descendent order, -1 as the decrementer. starts from the highest index (max freq) and decreases to 0.
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result




           

           
        count = defaultdict()
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, count in count.items():  #key, value
            freq[count].append(n)
        
        result = []
        for i in range(len(freq) - 1 , 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result





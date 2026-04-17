class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)

        buckets = {}
        for key in freqs:
            freq = freqs[key]
            if freq in buckets:
                buckets[freq].append(key)
            else:
                buckets[freq] = [key]
        
        freqList = list(buckets.keys())
        freqList.sort()

        print(buckets)
        toReturn = []
        for i in freqList:
            bucket = buckets[i]
            bucket.sort(reverse=True)
            
            for num in bucket:
                toReturn += [num] * i

        
        return toReturn
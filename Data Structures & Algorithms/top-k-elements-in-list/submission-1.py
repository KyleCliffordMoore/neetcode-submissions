class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = Counter(nums)

        def bucketSort(freqs):
            
            buckets = [[] for i in range(len(nums) + 1)]
            for key in freqs:
                freq = freqs[key]

                buckets[freq].append(key)

            return buckets
        
        buckets = bucketSort(freqs)

        print(buckets)
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            while k > 0 and len(bucket) > 0:
                k -= 1
                ans.append(bucket.pop())

        return ans
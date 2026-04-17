class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Init bucket & counts
        counts = Counter(nums)
        buckets = []
        for i in range(len(nums) + 1): # 0 will never be used oh well
            buckets.append([])

        # Place counts inside buckets
        for key in counts:
            occurances = counts.get(key)
            buckets[occurances].append(key)
        # print("finished buckets:", buckets)

        # Get k values going from right to left
        answer = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) != 0:
                for j in buckets[i]:
                    answer.append(j)
                    k -= 1
                    if k <= 0:
                        return answer

        return answer

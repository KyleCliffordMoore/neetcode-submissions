class Solution:

    mylist = deque([])

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            self.mylist.append(len(string))
            ans += string
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        while self.mylist:
            idx = self.mylist.popleft()
            ans.append(s[:idx])
            s = s[idx:]
        return ans
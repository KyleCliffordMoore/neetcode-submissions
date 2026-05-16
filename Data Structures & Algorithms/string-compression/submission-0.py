class Solution:
    def compress(self, chars: List[str]) -> int:        
        write = 0
        read = 0

        while read < len(chars):
            curr = chars[read]
            count = 0

            while read < len(chars) and chars[read] == curr:
                read += 1
                count += 1

            chars[write] = curr
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
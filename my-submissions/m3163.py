class Solution:
    def compressedString(self, word: str) -> str:
        output = []
        prev_char, cnt = None, 0
        for c in word :
            if cnt == 9 :
                output.append(str(cnt) + prev_char)
                prev_char, cnt = None, 0

            if c == prev_char :
                cnt += 1
                continue

            if prev_char :
                output.append(str(cnt) + prev_char)

            prev_char = c
            cnt = 1

        output.append(str(cnt) + prev_char)
        return ''.join(output)

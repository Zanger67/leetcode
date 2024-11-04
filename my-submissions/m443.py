class Solution:
    def compress(self, chars: List[str]) -> int:
        output_len = 0
        prev, cnt = None, 0
        output_len = 0

        # + [None] allows for the last round of characters
        #          to have a turn to be added
        for c in chars + [None] :
            if prev == c :
                cnt += 1
                continue

            if prev :
                chars[output_len] = prev
                output_len += 1

                reps_str = str(cnt)
                if cnt > 1 :
                    for x in reps_str :
                        chars[output_len] = x
                        output_len += 1
            prev = c
            cnt = 1

        return output_len

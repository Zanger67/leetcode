class Solution:
    def bestClosingTime(self, customers: str) -> int:
            y_cnt = customers.count("Y")
            n_cnt = 0
            output = 0
            output_pen = y_cnt
            for i, c in enumerate(customers, 1) :
                if c == 'N' :
                    n_cnt += 1
                else :
                    y_cnt -= 1
                
                if y_cnt + n_cnt < output_pen :
                    output, output_pen = i, y_cnt + n_cnt
            
            return output
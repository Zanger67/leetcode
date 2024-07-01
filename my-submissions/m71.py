class Solution:
    def simplifyPath(self, path: str) -> str:
        output = deque()

        temp = path.replace('//', '/')

        while '//' in temp :
            temp = temp.replace('//', '/')
        temp = temp.split('/')

        for folder in temp :
            if folder == '.' :
                continue
            if folder == '..' :
                if len(output) > 0 :
                    output.pop()
                continue
            output.append(folder)
        
        while len(output) > 0 and output[0] == '' :
            output.popleft()
        while len(output) > 0 and output[-1] == '' :
            output.pop()

        return '/' + '/'.join(output)
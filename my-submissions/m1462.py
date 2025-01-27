        prereqs = defaultdict(set)

        for a, b in prerequisites :
            prereqs[b].add(a)

        output = []

        for i, (a, b) in enumerate(queries) :
            to_visit = [b]
            visited = set()

            while to_visit :
                x = to_visit.pop()
                if x in visited :
                    continue
                visited.add(x)

                if x == a :
                    output.append(True)
                    break

                for y in prereqs[x] :
                    if y not in visited :
                        to_visit.append(y)

            if len(output) <= i :
                output.append(False)

        return output
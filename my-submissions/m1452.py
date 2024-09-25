class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(x) for x in favoriteCompanies]
        
        return [i for i, x in enumerate(favoriteCompanies) 
                  if all(x == y 
                         or not x.issubset(y) 
                         for y in favoriteCompanies)]

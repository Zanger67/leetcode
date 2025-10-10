class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(k, len(energy)) :
            energy[i] = max(energy[i], energy[i - k] + energy[i])
        return max(energy[-k:])
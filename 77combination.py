from typing import List


class Solution:

    def __init__(self):
        self.sub_set_list = []
        self.k = None
        self.n = None

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.n = n
        for action in range(1, n + 1):
            subset = []
            self.search_subset(subset, action)
        return self.sub_set_list

    def search_subset(self, subset, action):
        new_subset = subset.copy()
        new_subset.append(action)
        if len(new_subset) == self.k:
            self.sub_set_list.append(new_subset)
            return
        if action == self.n:
            return
        for new_action in range(action + 1, self.n + 1):
            self.search_subset(new_subset, new_action)


if __name__ == "__main__":
    solu = Solution()
    n, k = 4, 2
    print(solu.combine(n, k))

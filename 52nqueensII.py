from typing import Tuple, List
import numpy as np

"""
本问题中，需要用到回溯算法，利用深度优先搜索解决问题。
在构建模型的时候，需要意识到queen是一行一行放置的，这样不会出现重复结果，不需记录已经visit的点。
逐行放置queen可以大大减少动作空间，降低时间消耗
"""


class Solution:

    def __init__(self):
        self._n = None
        self._visited = set()
        self._success = 0

    def is_visited(self, location):
        return location in self._visited

    def totalNQueens(self, n: int) -> int:
        self._n = n
        for i in range(n):
            choice = (0, i)
            path = []
            adj = np.zeros((n, n))
            self.find_avail_poz(adj, path, choice)
        return self._success

    def find_avail_poz(self, adj: np.ndarray, path: List[Tuple[int, int]], choice: Tuple[int, int]):
        new_path = path.copy()
        new_path.append(choice)
        if len(new_path) == self._n:
            self._success += 1
            return
        new_adj, new_choices = self._get_adjacency(adj, choice)
        if not new_choices:
            return
        for new_choice in new_choices:
            self.find_avail_poz(new_adj, new_path, new_choice)

    def _get_adjacency(self, prev_adj: np.ndarray, new_choice: tuple):
        # 放入老棋盘，棋盘上0表示可放置的位置
        # 输入放置位置，返回新棋盘，和新的可放置位置
        adj = prev_adj.copy()
        m, n = new_choice
        adj[m, :] = 1
        adj[:, n] = 1
        m_temp, n_temp = m, n
        while m_temp < self._n and n_temp < self._n:
            adj[m_temp, n_temp] = 1
            m_temp += 1
            n_temp += 1
        m_temp, n_temp = m, n
        while m_temp >= 0 and n_temp >= 0:
            adj[m_temp, n_temp] = 1
            m_temp -= 1
            n_temp -= 1
        m_temp, n_temp = m, n
        while m_temp < self._n and n_temp >= 0:
            adj[m_temp, n_temp] = 1
            m_temp += 1
            n_temp -= 1
        m_temp, n_temp = m, n
        while m_temp >= 0 and n_temp < self._n:
            adj[m_temp, n_temp] = 1
            m_temp -= 1
            n_temp += 1
        next_row = new_choice[0] + 1
        poz_tuple = [(next_row, col) for col in np.where(adj[next_row, :] == 0)[0]]
        return adj, poz_tuple


if __name__ == "__main__":
    import time
    solu = Solution()
    prev_adj = np.zeros((5, 5))
    start = time.time()
    result = solu.totalNQueens(9)
    dur = time.time() - start
    print(result)
    print(dur)


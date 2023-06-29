from collections import defaultdict, deque


class Solution:
    def max_probability(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
        start: int,
        end: int,
    ) -> float:
        succ_prob_node = [0] * n
        succ_prob_node[start] = 1

        node_paths = defaultdict(list)

        for i, [node, another_node] in enumerate(edges):
            node_paths[node].append((another_node, i))
            node_paths[another_node].append((node, i))

        paths = deque()
        paths.append(start)

        while paths:
            node = paths.popleft()

            for next_node, succ_prob_i in node_paths[node]:
                if next_node == node:
                    continue
                new_v = succ_prob_node[node] * succ_prob[succ_prob_i]
                if new_v > succ_prob_node[next_node]:
                    succ_prob_node[next_node] = new_v
                    paths.append(next_node)

        return succ_prob_node[end]

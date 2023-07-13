class Solution:
    def eventual_safe_nodes(self, graph: list[list[int]]) -> list[int]:
        node_statuses = {
            "NOT_VISITED": 0,
            "VISITED": 1,
            "SAFE": 3
        }
        status = [node_statuses["NOT_VISITED"]] * (len(graph))
        res = []

        def is_safe_node(node: int):
            if status[node] == node_statuses["VISITED"]:
                return False
            if status[node] == node_statuses["SAFE"]:
                return True
            status[node] = node_statuses["VISITED"]

            for outgoing_node in graph[node]:
                if not is_safe_node(outgoing_node):
                    return False
            status[node] = node_statuses["SAFE"]
            return True

        for i in range(len(graph)):
            if is_safe_node(i):
                res.append(i)
        return res

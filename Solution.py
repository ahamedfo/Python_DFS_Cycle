from collections import deque


class Solution:
    def __init__(self, graph):
        self.graph = graph

    def root_finder(self, explored):
        for node in explored:
            if explored[node] == False:
                return node

    def find_cycle(self):
        #print("Implement me!")
        self.graph
        #stack_size = 0
        stack = deque()
        explored = {}
        node_to_neighbor = {}
        lists = []
        for node in self.graph:
            explored[node] = False
        while False in list(explored.values()):
            if len(stack) <= 1:
                root = self.root_finder(explored)
                stack.append(root)
                #stack_size += 1
                node_to_neighbor[root] = root
            for node in list(stack):
                k = []
                k.append(node)
                stack.pop()
                #stack_size -= 1
                if not explored[node]:
                    explored[node] = True
                for neighbor in self.graph.get(node):
                            k.append(neighbor)
                            if not explored[neighbor]:
                                stack.append(neighbor)
                                #stack_size += 1
                                if neighbor not in node_to_neighbor.keys():
                                    node_to_neighbor[neighbor] = node
                            elif explored[neighbor] and node_to_neighbor[node] != neighbor and len(stack) > 2:
                                lists.append(neighbor)
                                i = node #1
                                while i != node_to_neighbor[i]:
                                    lists.append(i)
                                    i = node_to_neighbor[i]
                                lists.append(i)
                                if len(lists) == 3:
                                    a = lists[0]
                                    lists[0] = lists[1]
                                    lists[1] = a
                                if len(lists) != len(set(lists)):
                                    return []
                                return lists
                explored[node] = True
        return []
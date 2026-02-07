class DisJointSet:
    def __init__(self, n):

        self.parents = list(range(n)) #[0,1,2,3]
        self.n_of_verties = [1] * n
        self.levels = [0] * n

    def find(self, x: int) -> int:
        """
        :param x: vertie we are going to find root for
        :return: the root of the x
        """

        try:
            if x != self.parents[x]:

                self.parents[x] = self.find(self.parents[x])

            return self.parents[x]

        except IndexError as e:
            print(f'{e} has happened')
            return None

    def union(self, v_1, v_2):

        root_1 = self.find(v_1)
        root_2 = self.find(v_2)

        if root_1 != root_2:

            if self.levels[root_1] > self.levels[root_2]:#маємо додати другий до першого

                self.parents[root_2] = root_1

                self.n_of_verties[root_1] += self.n_of_verties[root_2]

            elif self.levels[root_1] < self.levels[root_2]:

                self.parents[root_1] = root_2

                self.n_of_verties[root_2] += self.n_of_verties[root_1]

            else:

                self.levels[root_1] += 1

                self.parents[root_2] = root_1

                self.n_of_verties[root_1] += self.n_of_verties[root_2]

            return True

        return False


def kruskal(n, G, show_weight=False):
    """
    Finds minimum spanning tree

    """

    edges = list(G.edges(data=True))

    edges = sorted(edges, key=lambda x: x[2]['weight'])#[v_1, v_2, weight_dict]

    graph = DisJointSet(n)

    mst = []


    total_weight = 0
    for v_1, v_2, weight_dict in edges:

        if graph.union(v_1, v_2):

            mst.append((v_1,v_2))

            total_weight += weight_dict['weight']

        if len(mst) == n - 1:
            break

    if show_weight:

        return mst, total_weight

    return mst

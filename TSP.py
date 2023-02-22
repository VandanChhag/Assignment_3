from sys import maxsize
import numpy as np


class Solver:
    def __solver(self, graph, city_num, s):
        vertex = []
        for i in range(city_num):
            if i != s:
                vertex.append(i)

        min_cost = maxsize
        min_path = []
        while True:
            path = []
            current_cost = 0
            k = s
            for i in range(len(vertex)):
                current_cost += graph[k][vertex[i]]
                k = vertex[i]
                path.append(k + 1)
            current_cost += graph[k][s]
            if min_cost > current_cost:
                min_cost = current_cost
                path.append(s + 1)
                path.insert(0, s + 1)
                min_path = path

            if not self.__next_perm(vertex):
                break
        return min_cost, min_path

    def __next_perm(self, l):
        n = len(l)
        i = n - 2

        while i >= 0 and l[i] > l[i + 1]:
            i -= 1

        if i == -1:
            return False

        j = i + 1
        while j < n and l[j] > l[i]:
            j += 1

        j -= 1

        l[i], l[j] = l[j], l[i]
        left = i + 1
        right = n - 1

        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return True

    def __dist(self):
        city_num = int(input("Enter number of cities "))
        city_dist = np.zeros((city_num, city_num))

        for i in range(city_num):
            for j in range(city_num):
                dist = 0
                if i < j:
                    dist = int(input(f"Enter Distance b/w {i + 1} and {j + 1} "))
                elif i > j:
                    dist = city_dist[j][i]
                city_dist[i][j] = dist
        return list(city_dist), city_num

    def run(self):
        graph, city_num = self.__dist()
        res = self.__solver(graph, city_num, 0)
        print(res)


if __name__ == '__main__':
    runner = Solver()
    runner.run()

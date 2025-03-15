from collections import defaultdict
from multiprocessing import Pool, cpu_count


class Grid:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.grid = defaultdict(set)  #utilisation d'un set pour éviter les doublons

    def add_circle(self, circle):
        for cell_key in circle.get_cells(self.cell_size):
            self.grid[cell_key].add(circle)

    def build(self, circles):
        self.grid.clear()
        for circle in circles:
            self.add_circle(circle)

    def check_collisions(self):
        collisions = set()
        checked_pairs = set()

        for cell_key, cell_circles in self.grid.items():
            sorted_circles = sorted(cell_circles, key=lambda c: c.x)  #trie par coordonnée X

            for i, c1 in enumerate(sorted_circles):
                for j in range(i + 1, len(sorted_circles)):
                    c2 = sorted_circles[j]

                    #optimisation Sweep & Prune : Si la différence en X est trop grande, on arrête
                    if c2.x - c1.x > c1.radius + c2.radius:
                        break  

                    if (c1, c2) not in checked_pairs and c1.collision(c2):
                        collisions.add((c1, c2))
                        checked_pairs.add((c1, c2))

        return collisions

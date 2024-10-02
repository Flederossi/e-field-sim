import numpy as np
import matplotlib.pyplot as plt
import math

class Vector(object):
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z
    def mag(self): return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    def add(self, v2): self.x, self.y, self.z = self.x + v2.x, self.y + v2.y, self.z + v2.z
    def sub(self, v2): self.x, self.y, self.z = self.x - v2.x, self.y - v2.y, self.z - v2.z
    def mul(self, n): self.x, self.y, self.z = self.x * n, self.y * n, self.z * n
    def copy(self): return Vector(self.x, self.y, self.z)

def main():
    charges = [
        (Vector(-4, 0, -6), 1), (Vector(4, 0, 8), -1),
        (Vector(6, 6, 4), 1), (Vector(0, 10, -10), -1),
        (Vector(8, -10, 0), 1)
    ]
    resolution = 2

    minvec = Vector(math.inf, math.inf, math.inf)
    for c in charges: minvec = Vector(min(c[0].x, minvec.x), min(c[0].y, minvec.y), min(c[0].z, minvec.z))
    maxvec = Vector(-math.inf, -math.inf, -math.inf)
    for c in charges: maxvec = Vector(max(c[0].x, maxvec.x), max(c[0].y, maxvec.y), max(c[0].z, maxvec.z))

    vec_pos, vec_dir = [], []
    for x in np.arange(minvec.x, maxvec.x + resolution, resolution):
        for y in np.arange(minvec.y, maxvec.y + resolution, resolution):
            for z in np.arange(minvec.z, maxvec.z + resolution, resolution):
                vec_pos.append(Vector(x, y, z))
                vec_dir.append(Vector(0, 0, 0))
                for c in charges:
                    r = vec_pos[-1].copy()
                    r.sub(c[0])
                    if r.x == 0 and r.y == 0 and r.z == 0:
                        vec_dir[-1] = Vector(0, 0, 0)
                        break
                    else: r.mul(c[1] / (r.mag() ** 3))
                    vec_dir[-1].add(r)
                if not (vec_dir[-1].x == 0 and vec_dir[-1].y == 0): vec_dir[-1].mul(1 / vec_dir[-1].mag())

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.quiver(
        [v.x for v in vec_pos], [v.y for v in vec_pos], [v.z for v in vec_pos],
        [d.x for d in vec_dir], [d.y for d in vec_dir], [d.z for d in vec_dir],
        color='gray', alpha=0.5
    )
    for c in charges: ax.scatter(c[0].x, c[0].y, c[0].z, c='red' if c[1] > 0 else 'blue')
    plt.show()

if __name__ == "__main__":
    main()
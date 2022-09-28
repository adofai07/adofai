from math import *

FLOATERROR = 1e-15

class Point:
    def __init__(self, *args) -> None:
        self.x, self.y = args

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, c):
        return Point(self.x * c, self.y * c)

    def __truediv__(self, c):
        return Point(self.x / c, self.y / c)

    def __eq__(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y)) < FLOATERROR

    def angle(self) -> float:
        return atan2(self.y, self.x)
    
    def len(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def rotate(self, angle):
        return Point(
        self.x * cos(angle) - self.y * sin(angle),
        self.x * sin(angle) + self.y * cos(angle)
        )

    def __str__(self):
        return f"({self.x}, {self.y})"

def dot_product(a: Point, b: Point) -> float:
    return a.x * b.x + a.y * b.y

def cross_product(a: Point, b: Point) -> float:
    return a.x * b.y - a.y * b.x

def angle(a: Point, b: Point) -> float:
    return atan2(cross_product(a, b), dot_product(a, b))

def intersects_lp(a1: Point, a2: Point, b: Point) -> bool:
    if abs(cross_product(a2 - a1, b - a1)) > FLOATERROR: return False
    if dot_product(a2 - a1, b - a1) < FLOATERROR: return False
    if dot_product(a1 - a2, b - a2) < FLOATERROR: return False

    return True

def intersects_ll(a1: Point, a2: Point, b1: Point, b2: Point):
    if (cross_product(a2-a1, b1-a1) - FLOATERROR) * (cross_product(a2-a1, b2-a1) - FLOATERROR) > 0: return False
    if (cross_product(b2-b1, a1-b1) - FLOATERROR) * (cross_product(b2-b1, a2-b1) - FLOATERROR) > 0: return False
    return True

def intersects_tp(p1: list, p2: list, i: int, j: int):
    a0 = p1[(i + len(p1) - 1) % len(p1)]
    a1 = p1[i]
    a2 = p1[(i + 1) % len(p1)]
    b0 = p2[(j + len(p2) - 1) % len(p2)]
    b1 = p2[j]
    b2 = p2[(j + 1) % len(p2)]

    if intersects_ll(b1, b2, a1, a2): return True
    if intersects_lp(b1, b2, a1) and max(cross_product(b2-b1, a0-b1), cross_product(b2-b1, a2-b1)) > FLOATERROR: return True
    if intersects_lp(a1, a2, b1) and max(cross_product(a2-a1, b0-a1), cross_product(a2-a1, b2-a1)) > FLOATERROR: return True

    if a1 != b1: return False

    if (angle(b2-b1, b0-b1) - angle(b2-b1, a2-b1)) % (2 * pi) > FLOATERROR and (angle(b2-b1, a2-b1)) % (2 * pi) > FLOATERROR: return True
    if (angle(b2-b1, b0-b1) - angle(b2-b1, a0-b1)) % (2 * pi) > FLOATERROR and (angle(b2-b1, a0-b1)) % (2 * pi) > FLOATERROR: return True

    return False


intersects_p_x, intersects_p_y = -1, -1

def intersects_p(p1: list, p2: list) -> bool:
    global intersects_p_x, intersects_p_y
    if intersects_p_x != -1 and intersects_tp(p1, p2, intersects_p_x, intersects_p_y): return True

    for i in range(len(p1)):
        for j in range(len(p2)):
            if intersects_tp(p1, p2, i, j): intersects_p_x, intersects_p_y = i, j; return True

    return False


p1, p2 = [], []

N1 = int(input())
for _ in range(N1):
    a, b = map(float, input().split())
    p1.append(Point(a, b))

N2 = int(input())
for _ in range(N2):
    a, b = map(float, input().split())
    p2.append(Point(a, b))

p1.reverse(); p2.reverse()

res = 0

for i in range(N1):
    for j in range(N2):
        a1 = p1[i]
        a2 = p1[(i+1)%N1]
        b1 = p2[j]
        b2 = p2[(j+1)%N2]


        temp = angle(b1-b2, a2-a1)
        p3 = list(map(lambda x: x.rotate(temp), p2))

        temp = p1[i] - p3[j]
        p3 = list(map(lambda x: x + temp, p3))

        vec = (a2-a1) / (a2-a1).len()
        maxdist = (a2-a1).len() + (b2-b1).len()


        ret = 0
        cand = []

        for i1 in range(len(p1)):
            l1 = p1[i1]
            l2 = p1[(i1+1)%len(p1)]

            delta = cross_product(l2-l1, vec)

            if abs(delta) < FLOATERROR: continue

            for i2 in range(len(p3)):
                dist = -cross_product(l2-l1, p3[i2]-l1) / delta

                if dot_product(l2-l1, p1[i1]-vec*dist-l1) < -FLOATERROR: continue
                if dot_product(l1-l2, p1[i1]-vec*dist-l2) < -FLOATERROR: continue

                cand.append(cross_product(l2-l1, p1[i1]-l1) / delta)

        
        for i2 in range(len(p3)):
            l1 = p3[i2]
            l2 = p3[(i2+1)%len(p3)]

            delta = cross_product(l2-l1, vec)

            if abs(delta) < FLOATERROR: continue

            for i1 in range(len(p1)):
                dist = cross_product(l2-l1, p1[i1]-l1) / delta

                if dot_product(l2-l1, p1[i1]-vec*dist-l1) < -FLOATERROR: continue
                if dot_product(l1-l2, p1[i1]-vec*dist-l2) < -FLOATERROR: continue

                cand.append(cross_product(l2-l1, p1[i1]-l1) / delta)

        cand.sort()

        for ci in range(len(cand)):
            if cand[ci] < -FLOATERROR or cand[ci] > maxdist + FLOATERROR: continue
            if ci != 0 and cand[ci] - cand[ci-1] < FLOATERROR: continue

            p4 = list(map(lambda x: x + vec * cand[ci], p3))

            if not intersects_p(p1, p4):
                temp = 0

                for i in range(len(p1)):
                    a1 = p1[i]
                    a2 = p1[(i+1)%len(p1)]

                    ln = (a1 - a2).len()

                    for j in range(len(p4)):
                        b1 = p4[j]
                        b2 = p4[(j+1)%len(p4)]

                        if abs(cross_product(a2-a1, b1-a1)) > FLOATERROR: continue
                        if abs(cross_product(a2-a1, b2-a1)) > FLOATERROR: continue

                        temp += abs(
                        max(0, min(dot_product(a2-a1, b1-a1) / ln, ln)) -
                        max(0, min(dot_product(a2-a1, b2-a1) / ln, ln))
                        )
                
                ret = max(ret, temp)

        res = max(res, ret)

print(res)
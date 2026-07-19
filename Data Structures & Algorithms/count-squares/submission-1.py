class CountSquares:

    def __init__(self):
        self.pts = {}
        

    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        self.pts[pt] = self.pts.get(pt, 0) + 1 
        

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point[0], point[1]
        for (x, y), f in self.pts.items():
            if abs(x - qx) == abs(y - qy) != 0:
                pt1 = (x, qy)
                pt2 = (qx, y)
                res = res + (self.pts.get(pt1, 0) * self.pts.get(pt2, 0) * f)
        return res


        
        

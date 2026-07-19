class TimeMap:

    def __init__(self):
        self.tmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""
        arr = self.tmap[key]
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            if arr[mid][1] <= timestamp:
                l = mid
            else:
                r = mid - 1
                
        return arr[l][0] if arr[l][1] <= timestamp else ""
        

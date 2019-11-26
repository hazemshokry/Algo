from functools import reduce


class MapSum:
    mapsum = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapsum = {}





    def insert(self, key: str, val: int) -> None:
        MapSum.mapsum[key] = val

    def sum(self, prefix: str) -> int:
        newmapsum = map((lambda s: MapSum.mapsum[s] if s.startswith(prefix) else 0), MapSum.mapsum)
        result = reduce((lambda x,y: x + y), newmapsum)
        return result

if __name__ == '__main__':
    obj = MapSum()
    obj.insert("a",3)
    print(obj.sum("ap"))
    obj.insert("b",2)
    print(obj.sum("a"))
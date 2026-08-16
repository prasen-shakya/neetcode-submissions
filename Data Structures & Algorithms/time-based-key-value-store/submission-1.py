class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.data.get(key, None):
            self.data[key] = []
        
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.data.get(key, None):
            return ""
        key_values = self.data[key]

        l, r = 0, len(key_values) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2

            if key_values[m][1] <= timestamp:
                res= key_values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

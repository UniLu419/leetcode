from typing import List
from timing_dec import timing
import random


class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        try:
            self.vals.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.vals))


class RandomizedSet2:

    def __init__(self):
        self.hash_map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.list)  # len = index+1
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        index_to_del = self.hash_map[val]
        last_index = self.list[-1]

        self.list[index_to_del] = last_index
        self.hash_map[last_index] = index_to_del

        self.hash_map.pop(val)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


def main():
    # Your main code goes here
    try:
        obj = RandomizedSet()
        param_1 = obj.insert(1)
        param_2 = obj.remove(2)
        param_3 = obj.getRandom()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

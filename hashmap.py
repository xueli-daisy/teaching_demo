# Hash Map

class HashMap:
        def __init__(self):
                self.size = 9
                self.map = [None] * self.size

        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size

#        def _get_hash(self, key):
#                return len(key) - 1

        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        self.map[key_hash].append(key_value)
                        return True

        def get(self, key):
                key_hash = self._get_hash(key)
                value_list = []
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        value_list.append(pair[1])
                        return value_list

        def delete(self, key, value):
                key_hash = self._get_hash(key)

                if self.map[key_hash] is None:
                        return False
                else:
                        for i in range (0, len(self.map[key_hash])):
                            if self.map[key_hash][i][0] == key and self.map[key_hash][i][1] == value:
                                self.map[key_hash].pop(i)
                                return True
                            else:
                                return False

        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                for j in self.map[i]:

                                    arr.append(j[0])
                return set(arr)

        def values(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                for j in self.map[i]:

                                    arr.append(j[1])
                return set(arr)


        def print(self):
                print('---Enrollment Status----')
                for item in self.map:
                        if item is not None:
                                print(str(item))
                print()

h = HashMap()
h.add('COSC 1800', 'Caption America')
h.add('ART 1110', 'Spider Man')
h.add('ILC 1000', 'Iron Man')
h.print()
h.add('COSC 1800', 'Hulk')
h.print()
h.delete('COSC 1800', 'Caption America')
h.delete('COSC 1800', 'Ant Man')
h.print()
print("Students who registered COSC 1800: ", h.get('COSC 1800'))
print("Available classes from the Webster University:", h.keys())
print("Students who registered classes:", h.values())

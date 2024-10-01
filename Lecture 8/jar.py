class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit exceed capacity")
        self.size += n
    def withdraw(self, n):
        if self.size  < n:
            raise ValueError("Withdraw exceed size")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity=capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if not isinstance(size, int) or size < 0:
            raise ValueError("Invalid size")
        self._size=size

jar = Jar()
print(jar.capacity)
jar.deposit(1)
print(jar.size)
jar.withdraw(0)
print(str(jar))


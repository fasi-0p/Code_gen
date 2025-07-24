class HashMap:
    """
    Hash Map Implementation:
    - Uses chaining to resolve collisions.
    - Key -> Hash(key) % size -> Bucket list
    """
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size  # Built-in hash + mod

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key

    def get(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v  # Return value if key found
        return None

# ✅ Example
hm = HashMap()
hm.put("apple", 5)
hm.put("banana", 10)
print("Apple:", hm.get("apple"))    # 5
print("Banana:", hm.get("banana"))  # 10

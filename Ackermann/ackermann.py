import sys

lookup = {}

def ackermann(m, n) -> int:
    if (m, n) in lookup:
        return lookup[(m, n)]
    if m == 0: 
        lookup[(m, n)] = n + 1
        return n + 1
    if n == 0:
        lookup[(m, n)] = ackermann(m - 1, 1)
        return ackermann(m - 1, 1)
    lookup[(m, n)] = ackermann(m - 1, ackermann(m, n - 1))
    return lookup[(m, n)]

if __name__ == "__main__":
    print(ackermann(int(sys.argv[1]), int(sys.argv[2])))

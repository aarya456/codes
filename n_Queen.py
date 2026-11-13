def safe(b, r, c, n):
    for i in range(r):
        if b[i][c] == 1:
            return False
        if c-(r-i) >= 0 and b[i][c-(r-i)] == 1:
            return False
        if c+(r-i) < n and b[i][c+(r-i)] == 1:
            return False
    return True

def solve(b, r, n):
    if r == n:
        return True

    for c in range(n):
        if safe(b, r, c, n):
            b[r][c] = 1
            if solve(b, r+1, n):
                return True
            b[r][c] = 0
    return False

n = int(input("Enter N: "))
b = [[0]*n for i in range(n)]

b[0][0] = 1

if solve(b, 1, n):
    for row in b:
        print(row)
else:
    print("No solution")

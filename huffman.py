import heapq

def huffman(freq):
    heap = [[f, [[c, ""]]] for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        for x in a[1]:
            x[1] = '0' + x[1]
        for x in b[1]:
            x[1] = '1' + x[1]

        heapq.heappush(heap, [a[0]+b[0], a[1]+b[1]])

    for c, code in heap[0][1]:
        print(c, ":", code)

n = int(input("Enter number of characters: "))
freq = {}

for i in range(n):
    c = input("Enter character: ")
    f = int(input("Enter frequency: "))
    freq[c] = f

huffman(freq)

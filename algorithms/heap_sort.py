q = [0, 1, 2, 3, 4, 5, 6]
n = len(q)
root = 0
left = 2 * root + 1
right = 2 * root + 2


def heapify(q):
    n = len(q)

    def heap_sort(root):
        left = 2 * root + 1
        right = 2 * root + 2

        if right < n:
            heap_sort(right)
            if q[root] < q[right]:
                q[root], q[right] = q[right], q[root]
                heap_sort(right)

        if left < n:
            heap_sort(left)
            if q[root] < q[left]:
                q[root], q[left] = q[left], q[root]
                heap_sort(left)

    heap_sort(0)


def pop(q):
    q[0], q[-1] = q[-1], q[0]
    ans = q.pop()
    n = len(q)

    def heap_sort(root):
        left = 2 * root + 1
        right = 2 * root + 2

        if right < n:
            if q[right] > q[left]:
                max = right
            else:
                max = left
            if q[root] < q[max]:
                q[root], q[max] = q[max], q[root]
                heap_sort(max)
        elif left < n:
            if q[root] < q[left]:
                q[root], q[left] = q[left], q[root]

    heap_sort(0)
    return ans


def push(q, num):
    q.append(num)
    n = len(q)

    def heap_sort(child):
        father = (child - 1) // 2

        if father >= 0 and q[father] < q[child]:
            q[father], q[child] = q[child], q[father]
            heap_sort(father)

    heap_sort(n - 1)


def poppush(q, num):
    ans = q[0]
    q[0] = num
    n = len(q)

    def heap_sort(root):
        left = 2 * root + 1
        right = 2 * root + 2

        if right < n:
            if q[right] > q[left]:
                max = right
            else:
                max = left
            if q[root] < q[max]:
                q[root], q[max] = q[max], q[root]
                heap_sort(max)
        elif left < n:
            if q[root] < q[left]:
                q[root], q[left] = q[left], q[root]

    heap_sort(0)
    return ans


heapify(q)
print(q)

while len(q) > 0:
    print(pop(q))
    print(q)

for i in range(6):
    push(q, i)
    print(q)

def chunkList(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def split_list(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def split(a, n):
    k, m = divmod(a, n)
    index = (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    print(index)
    return index
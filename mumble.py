def accum(st):
    store = ''
    for i in range(len(st)):
        store += st[i].upper()
        if i > 0:
            for z in range(i):
                store += st[i].lower()
        if i != len(st) - 1:
            store += '-'
    return store
def josephus(items,k):
    result = []
    index = -1
    while items:
        index = index + k
        if index >= len(items):
            index = index % len(items)
        result.append(items.pop(index))
        index -= 1
    return result

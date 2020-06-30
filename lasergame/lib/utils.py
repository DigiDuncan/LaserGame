def clamp(minVal, val, maxVal):
    if minVal is None and maxVal is None:
        return val
    if minVal is None:
        return max(val, maxVal)
    if maxVal is None:
        return min(minVal, val)
    return max(minVal, min(maxVal, val))


def default_itemgetter(name, default=None):
    def getter(o):
        return getattr(o, name, default)
    return getter

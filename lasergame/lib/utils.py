def clamp(minVal, val, maxVal):
    if minVal is None:
        minVal = float("-inf")
    if maxVal is None:
        maxVal = float("inf")
    return max(minVal, min(maxVal, val))


def default_itemgetter(name, default=None):
    def getter(o):
        return getattr(o, name, default)
    return getter

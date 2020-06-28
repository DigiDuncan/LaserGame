def clamp(minVal, val, maxVal):
    return max(minVal, min(maxVal, val))


def default_itemgetter(name, default=None):
    def getter(o):
        return getattr(o, name, default)
    return getter

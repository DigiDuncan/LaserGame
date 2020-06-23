class AttrDict:
    __slots__ = ["_values"]

    def __init__(self, data={}):
        # This avoids an infinite recursion issue with __getattr__()
        super().__setattr__("_values", data)

    def __getattr__(self, key):
        """value = attrdict.key"""
        try:
            return self._values[key]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {key!r}")

    def __setattr__(self, key, value):
        """attrdict.key = value"""
        if key in self.__slots__:
            raise AttributeError(f"{key!r} is a reserved attribute for {self.__class__.__name__!r}")
        self._values[key] = value

    def __getitem__(self, key):
        """value = attrdict[key]"""
        return self._values[key]

    def __setitem__(self, key, value):
        """attrdict[key] = value"""
        if key.startswith("_"):
            raise KeyError(f"{key!r} is a reserved key for {self.__class__.__name__!r}")
        self._values[key] = value

    def __str__(self):
        return str(self._values)

    def __repr__(self):
        return repr(self._values)

    def __iter__(self):
        return iter(self._values)

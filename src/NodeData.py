class NodeData:
    def __init__(self, key: int = None, info: str = None, tag: float = None, pos: tuple = None, weight: float = None,
                 **kwargs):
        self.key = key
        self.info = info
        self.tag = tag
        self.pos = pos
        self.weight = weight
        # print(kwargs)

    # def __repr__(self):
    #     return '{"pos" =%s,"id"=%d}' % (self.pos, self.key)
    def __repr__(self):
        return str(self.weight)

    def get_key(self):
        return self.key

    def set_key(self, k):
        self.key = k

    def get_info(self):
        return self.info

    def set_info(self, s):
        self.info = s

    def get_tag(self):
        return self.tag

    def set_tag(self, t):
        self.tag = t

    def get_weight(self):
        return self.weight

    def set_weight(self, w):
        self.weight = w

    def get_pos(self):
        return self.pos

    def set_pos(self, tu):
        self.pos = tu

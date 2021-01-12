class NodeData:
    def __init__(self, key: int = None, info: str = None, tag: float = None, pos: tuple = None, weight: float = None,
                 **kwargs):
        self.key = key
        self.info = info
        self.tag = tag
        self.pos = pos
        self.weight = weight
        # print(kwargs)

    def __repr__(self):
        return '{"pos" =%s,"id"=%d}' % (self.pos, self.key)
    """
    return the key node (node_id)
     """
    def get_key(self):
        return self.key

    """
        set the node key (node_id)
     """
    def set_key(self, k):
        self.key = k

    """
        return the node info
    """
    def get_info(self):
        return self.info

    """
        set node info
    """
    def set_info(self, s):
        self.info = s

    """
        return node tag
    """
    def get_tag(self):
        return self.tag

    """
        set node tag
    """
    def set_tag(self, t):
        self.tag = t

    """
       return the weight of the node (use in short path function)
    """
    def get_weight(self):
        return self.weight

    """
        set the weight of the node
    """
    def set_weight(self, w):
        self.weight = w

    """
        return the node position (tuple)
    """
    def get_pos(self):
        return self.pos

    """
        set the node position
    """
    def set_pos(self, tu):
        self.pos = tu

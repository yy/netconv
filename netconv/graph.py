"""
main.py
-------

Class that all formats get converted to and from.

"""

from .decoders import write_edgelist

class GraphData():
    """Class that all formats get converted to and from."""

    def __init__(self):
        self.node_attr = ['label']
        self.nodes = []
        self.edge_attr = ['edge']
        self.edges = []
        self.graph_attr = {}
        self._node_id = 0

    def __repr__(self):
        return repr(self.graph_attr) + '\n' \
            + repr(self.node_attr) + '\n' \
            + repr(self.nodes) + '\n' \
            + repr(self.edge_attr) + '\n' \
            + repr(self.edges)

    def decode(self, fmt, *args, **kwargs):
        decoders = {'edgelist': write_edgelist}
        return decoders[fmt](self, *args, **kwargs)

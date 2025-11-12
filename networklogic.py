import networkx as nx

class FaultTolerantNetwork:
    def __init__(self):
        self.G = nx.Graph()
        self.create_network()

    def create_network(self):
        # Add nodes (devices)
        self.G.add_nodes_from([
            ("PLC1", {"type": "Controller"}),
            ("PLC2", {"type": "Controller"}),
            ("Switch1", {"type": "Switch"}),
            ("Switch2", {"type": "Switch"}),
            ("Sensor1", {"type": "Sensor"}),
            ("Actuator1", {"type": "Actuator"})
        ])

        # Add connections (Ethernet links)
        self.G.add_edges_from([
            ("PLC1", "Switch1"),
            ("PLC2", "Switch1"),
            ("Switch1", "Switch2"),
            ("Switch2", "Sensor1"),
            ("Switch2", "Actuator1"),
            ("PLC1", "Switch2")  # Redundant path
        ])

    def simulate_failure(self, edge):
        if self.G.has_edge(*edge):
            self.G.remove_edge(*edge)
            return True
        return False

    def check_connectivity(self):
        return nx.is_connected(self.G)

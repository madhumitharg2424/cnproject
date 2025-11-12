import networkx as nx
import matplotlib.pyplot as plt

# Create a graph to represent Ethernet network
G = nx.Graph()

# Add factory devices (nodes)
G.add_nodes_from([
    ("PLC1", {"type": "Controller"}),
    ("PLC2", {"type": "Controller"}),
    ("Switch1", {"type": "Switch"}),
    ("Switch2", {"type": "Switch"}),
    ("Sensor1", {"type": "Sensor"}),
    ("Actuator1", {"type": "Actuator"})
])

# Add Ethernet connections (edges)
G.add_edges_from([
    ("PLC1", "Switch1"),
    ("PLC2", "Switch1"),
    ("Switch1", "Switch2"),
    ("Switch2", "Sensor1"),
    ("Switch2", "Actuator1"),
    # Redundant link for fault-tolerance
    ("PLC1", "Switch2")
])

# Visualize network
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10)
plt.title("Factory Ethernet Network (Normal State)")
plt.show()

# Simulate a failure
print("\nSimulating link failure between Switch1 and Switch2...")
G.remove_edge("Switch1", "Switch2")

# Check connectivity after failure
if nx.is_connected(G):
    print("✅ Network still operational — Fault Tolerant!")
else:
    print("❌ Network failure — No backup path!")

# Visualize after failure
nx.draw(G, pos, with_labels=True, node_color="salmon", node_size=2000, font_size=10)
plt.title("Network After Link Failure")
plt.show()

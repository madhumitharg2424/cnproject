import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from networklogic import FaultTolerantNetwork

# Streamlit UI config
st.set_page_config(page_title="Fault-Tolerant Ethernet Network", layout="centered")

st.title("🏭 Fault-Tolerant Ethernet Network Simulator")
st.write("Simulate industrial Ethernet networks with redundancy and link failure handling.")

# Initialize network
network = FaultTolerantNetwork()
pos = nx.spring_layout(network.G, seed=42)

# Sidebar for actions
st.sidebar.header("Simulation Controls")
failed_link = st.sidebar.selectbox(
    "Select a link to simulate failure:",
    [("PLC1", "Switch1"), ("PLC2", "Switch1"), ("Switch1", "Switch2"), ("Switch2", "Sensor1")]
)

simulate = st.sidebar.button("Simulate Failure 🔧")

# Draw initial network
fig, ax = plt.subplots(figsize=(6, 5))
nx.draw(network.G, pos, with_labels=True, node_color="lightgreen", node_size=2000, font_size=10)
st.pyplot(fig)

if simulate:
    network.simulate_failure(failed_link)

    st.write(f"**Simulating link failure:** {failed_link}")
    connected = network.check_connectivity()

    if connected:
        st.success("✅ Network still operational — fault-tolerant design successful!")
    else:
        st.error("❌ Network disconnected — redundancy failed!")

    # Draw after failure
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    nx.draw(network.G, pos, with_labels=True, node_color="salmon", node_size=2000, font_size=10)
    st.pyplot(fig2)

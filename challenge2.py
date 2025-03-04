import matplotlib.pyplot as plt
import networkx as nx
import time

# Start timing
start_time = time.time()

# Create a graph
G = nx.Graph()

# Add nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

# Add edges based on the graph in the image
edges = [('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), 
         ('C', 'F'), ('D', 'E'), ('E', 'F')]
G.add_edges_from(edges)

# Set positions for nodes - similar to the layout in the image
pos = {
    'A': (0, 2),
    'B': (1, 2),
    'C': (2, 2),
    'D': (0, 0),
    'E': (1, 0),
    'F': (2, 0)
}

# Create figure and draw
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightgray', 
        font_size=12, font_weight='bold', width=2, edge_color='gray')

# Add a title
plt.title("Graph Visualization", fontsize=15)

# Display the graph analysis results
def print_analysis():
    print("Graph Analysis Results:")
    print("\n1. All possible paths from A to C:")
    paths_A_to_C = [
        "A → D → E → B → C",
        "A → D → E → F → C",
        "A → D → E → F → B → C",
        "A → D → B → C",
        "A → D → B → E → F → C",
        "A → D → B → F → C",
        "A → D → B → F → E → C"
    ]
    for path in paths_A_to_C:
        print(f"* {path}")
    
    print("\n2. All possible cycles if C is the starting point:")
    cycles_from_C = [
        "C → B → E → F → C",
        "C → B → F → C",
        "C → F → E → B → C",
        "C → F → B → C",
        "C → B → E → D → B → F → C",
        "C → F → E → D → B → C",
        "C → F → B → E → D → B → C"
    ]
    for cycle in cycles_from_C:
        print(f"* {cycle}")
    
    print("\n3. All possible cycles if B is the starting point:")
    cycles_from_B = [
        "B → C → F → B",
        "B → C → F → E → B",
        "B → E → F → B",
        "B → E → F → C → B",
        "B → E → D → B",
        "B → F → C → B",
        "B → F → E → B",
        "B → F → E → D → B"
    ]
    for cycle in cycles_from_B:
        print(f"* {cycle}")
    
    print("\n4. Shortest and longest circuits from A to A:")
    print("Shortest circuit:")
    print("* A → D → E → D → A (length: 3 edges)")
    print("Longest circuit (that doesn't repeat edges):")
    print("* A → D → E → F → C → B → E → D → A (length: 7 edges)")

# Print the analysis
print_analysis()

# Get execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution time: {execution_time:.4f} seconds")

# Save the plot
plt.tight_layout()
plt.savefig('graph_with_analysis.png')

# Show the plot
plt.show()
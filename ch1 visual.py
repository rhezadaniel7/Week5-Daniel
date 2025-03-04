class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph
    
    def find_trail(self, start, end, visited=None, path=None):
        """Find a trail (path where edges are not repeated) from start to end"""
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        path.append(start)
        
        if start == end:
            return path
        
        for neighbor in self.graph[start]:
            edge = (min(start, neighbor), max(start, neighbor))  # Normalize edge representation
            if edge not in visited:
                visited.add(edge)
                result = self.find_trail(neighbor, end, visited, path.copy())
                if result:
                    return result
                visited.remove(edge)
        
        return None
    
    def find_all_paths(self, start, end, path=None):
        """Find all possible paths from start to end"""
        if path is None:
            path = []
        
        path = path + [start]
        
        if start == end:
            return [path]
        
        paths = []
        for neighbor in self.graph[start]:
            if neighbor not in path:  # Avoid cycles
                new_paths = self.find_all_paths(neighbor, end, path)
                paths.extend(new_paths)
        
        return paths
    
    def find_all_cycles(self, start, current=None, visited=None, path=None, cycles=None):
        """Find all possible cycles starting at node start"""
        if current is None:
            current = start
        if visited is None:
            visited = set([start])
        if path is None:
            path = [start]
        if cycles is None:
            cycles = []
        
        for neighbor in self.graph[current]:
            if neighbor == start and len(path) > 2:  # Found a cycle
                cycles.append(path + [start])
            elif neighbor not in visited:
                visited.add(neighbor)
                self.find_all_cycles(start, neighbor, visited.copy(), path + [neighbor], cycles)
                visited.remove(neighbor)
        
        return cycles

# Create the graph from the image
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

# 1. Find a trail from A to D
print("1. Trail dari A ke D:")
trail = g.find_trail('A', 'D')
print(" → ".join(trail))

# 2. Find all possible paths from A to D
print("\n2. Semua kemungkinan Path dari A ke D:")
paths = g.find_all_paths('A', 'D')
for i, path in enumerate(paths, 1):
    print(f"Path {i}: {' → '.join(path)}")

# 3. Find all possible cycles starting at A
print("\n3. Semua kemungkinan Cycle jika A titik awalnya:")
cycles = g.find_all_cycles('A')
for i, cycle in enumerate(cycles, 1):
    print(f"Cycle {i}: {' → '.join(cycle)}")
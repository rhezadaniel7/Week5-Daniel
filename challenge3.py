# Implementasi Graf dari Gambar dengan Visualisasi Matplotlib
import matplotlib.pyplot as plt
import networkx as nx

# Membuat graf
G = nx.Graph()

# Menambahkan node
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
G.add_nodes_from(nodes)

# Menambahkan edge (koneksi) sesuai dengan gambar
edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'E'), ('D', 'F'), ('D', 'J'),
    ('E', 'G'), ('E', 'K'), ('F', 'K'),
    ('F', 'I'), ('C', 'K'), ('G', 'H'),
    ('H', 'K'), ('I', 'J')
]
G.add_edges_from(edges)

# Menentukan posisi node untuk mendekati layout di gambar
pos = {
    'A': (0, 0),      # Node A di atas tengah
    'B': (-1, -1),    # Node B di kiri atas
    'C': (0, -1.2),   # Node C di tengah atas
    'D': (1, -1),     # Node D di kanan atas
    'E': (-0.8, -2),  # Node E di bagian tengah kiri
    'F': (0.8, -2),   # Node F di bagian tengah kanan
    'G': (-1.5, -3),  # Node G di bagian bawah kiri
    'H': (-0.5, -3),  # Node H di bagian bawah tengah
    'I': (0.5, -3),   # Node I di bagian bawah tengah
    'J': (1.5, -3),   # Node J di bagian bawah kanan
    'K': (0, -3.5)    # Node K di bagian paling bawah tengah
}

# Mendefinisikan warna dan ukuran node dan edge
node_color = 'lightblue'
node_size = 1500
edge_color = 'darkblue'
edge_width = 1.5
font_size = 14
font_weight = 'bold'

# Membuat figure dengan latar belakang warna biru muda
plt.figure(figsize=(10, 10))
ax = plt.gca()
ax.set_facecolor('lightcyan')

# Menggambar graf
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size, edgecolors='blue')
nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=edge_width)
nx.draw_networkx_labels(G, pos, font_size=font_size, font_weight=font_weight)

# Menghilangkan axis
plt.axis('off')

# Menambahkan judul
plt.title('Visualisasi Graf dari Gambar "Challenge 3 - Graph"', fontsize=16)

# Mendefinisikan fungsi untuk mencari semua jalur dari satu node ke node lain
def cari_semua_jalur(graph, awal, tujuan, jalur=None):
    """Mencari semua jalur dari node awal ke node tujuan"""
    if jalur is None:
        jalur = []
    
    jalur = jalur + [awal]
    
    if awal == tujuan:
        return [jalur]
    
    semua_jalur = []
    for node in graph.neighbors(awal):
        if node not in jalur:
            jalur_baru = cari_semua_jalur(graph, node, tujuan, jalur)
            for p in jalur_baru:
                semua_jalur.append(p)
                
    return semua_jalur

# Fungsi untuk menampilkan informasi tentang graf
def tampilkan_info_graf(graph):
    print("Informasi Graf:")
    print(f"Jumlah node: {graph.number_of_nodes()}")
    print(f"Jumlah edge: {graph.number_of_edges()}")
    print("\nKoneksi setiap node:")
    for node in sorted(graph.nodes()):
        neighbors = sorted(graph.neighbors(node))
        print(f"Node {node} terhubung dengan: {', '.join(neighbors)}")

# Menampilkan informasi graf
tampilkan_info_graf(G)

# Contoh penggunaan: mencari semua jalur dari A ke K
print("\nSemua jalur dari A ke K:")
jalur_a_ke_k = cari_semua_jalur(G, 'A', 'K')
for i, jalur in enumerate(jalur_a_ke_k, 1):
    print(f"Jalur {i}: {' -> '.join(jalur)}")

# Menyimpan gambar (opsional)
plt.savefig('visualisasi_graf.png', bbox_inches='tight', dpi=300)

# Menampilkan graf
plt.show()

# Kelas Graf untuk implementasi lebih lanjut jika diperlukan
class Graf:
    def __init__(self, graph=None):
        """Inisialisasi Graf menggunakan NetworkX graph"""
        self.nx_graph = nx.Graph() if graph is None else graph
        
    def tambah_node(self, node):
        """Menambahkan node ke dalam graf"""
        self.nx_graph.add_node(node)
            
    def tambah_edge(self, node1, node2):
        """Menambahkan edge antara node1 dan node2"""
        self.nx_graph.add_edge(node1, node2)
                
    def tampilkan_graf(self):
        """Menampilkan representasi graf"""
        for node in sorted(self.nx_graph.nodes()):
            neighbors = sorted(self.nx_graph.neighbors(node))
            print(f"Node {node} terhubung dengan: {', '.join(neighbors)}")
            
    def visualisasi(self, pos=None, judul="Visualisasi Graf"):
        """Memvisualisasikan graf menggunakan matplotlib"""
        if pos is None:
            pos = nx.spring_layout(self.nx_graph, seed=42)
            
        plt.figure(figsize=(10, 10))
        ax = plt.gca()
        ax.set_facecolor('lightcyan')
        
        nx.draw_networkx_nodes(self.nx_graph, pos, node_color='lightblue', node_size=1500, edgecolors='blue')
        nx.draw_networkx_edges(self.nx_graph, pos, edge_color='darkblue', width=1.5)
        nx.draw_networkx_labels(self.nx_graph, pos, font_size=14, font_weight='bold')
        
        plt.axis('off')
        plt.title(judul, fontsize=16)
        plt.show()
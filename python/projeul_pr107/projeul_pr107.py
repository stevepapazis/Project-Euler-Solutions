import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from pathlib import Path


network_file = Path(__file__).parent/"0107_network.txt"
network = np.genfromtxt(
    network_file,
    dtype=np.uint64,
    delimiter=",",
    missing_values="-",
    filling_values=np.uint64(0)
)

# remove double counting due to symmetry
original_weight = np.sum(network) // 2

# Kruskal's algorithm
mst = minimum_spanning_tree(csr_matrix(network))

maximum_saving = np.int64(original_weight - mst.sum())

print(f"Maximum saving: {maximum_saving}")
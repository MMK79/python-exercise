import torch
import matplotlib.pyplot as plt
from tqdm import tqdm

# list of vectors in one dimension
num_vectors = 10000
vector_len = 100
big_matrix = torch.randn(num_vectors, vector_len)
big_matrix /= big_matrix.norm(p=2, dim=1, keepdim=True)
big_matrix.requires_grad_(True)

# Setup Optimization loop to create nearly non-perpendicular vector
optimizer = torch.optim.Adam([ big_matrix ], lr=0.01)
num_steps = 250
# perpendicular

losses = []

dot_diff_cutoff = 0.01
big_id = torch.eye(num_vectors, num_vectors)

for step_num in tqdm(range(num_steps)):
    optimizer.zero_grad()

    dot_products = big_matrix @ big_matrix.T
    # Punish deviation from ontogral
    diff = dot_products - big_id
    loss = (diff.abs() - dot_diff_cutoff).relu().sum()

    # Extra incentive to keep the row normalize
    loss += num_vectors * diff.diag().pow(2).sum()

    loss.backward()
    optimizer.step()
    losses.append(loss.item())

# loss curve
plt.plot(losses)
plt.grid()
plt.show()

# angel distribution
dot_products = big_matrix @ big_matrix.T
norms = torch.sqrt(torch.diag(dot_products))
normed_dot_products = dot_products / torch.outer(norms, norms)
angel_degrees = torch.rad2deg(torch.acos(normed_dot_products.detach()))
# Use this to ignore self-orthogonality
self_orthogonality_mask = ~(torch.eye(num_vectors, num_vectors).bool())
plt.hist(angel_degrees[self_orthogonality_mask].numpy().ravel(), bins=1000, range=(0, 180))
plt.grid()
plt.show()

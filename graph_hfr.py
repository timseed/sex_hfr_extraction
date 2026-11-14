import plotext as plt
import numpy as np
from pathlib import Path

filename = "~/hfr/hfr.cat"
filename = Path(filename).expanduser()
flux_radius = []

# Read the SExtractor catalogue
with open(filename, "r") as f:
    for line in f:
        line = line.strip()

        # Skip comments and empty lines
        if not line or line.startswith("#"):
            continue

        columns = line.split()

        if len(columns) >= 4:
            flux_radius.append(float(columns[3]))
# print(flux_radius)
counts, edges = np.histogram(flux_radius, bins=15)
print(counts)  # Output: [2 1 2]
print(edges)  # Output: [ 2.          9.66666667 17.33333333 25.        ]

fig = plt.figure
fig.clear()


fig.draw(fig.bar(edges, counts))
fig.title("SExtractor - FLUX_RADIUS")

fig.show()

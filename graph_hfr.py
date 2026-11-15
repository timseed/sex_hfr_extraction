import plotext as plt
import numpy as np
from pathlib import Path
import sys


filename = "~/hfr/hfr.cat"
filename = Path(filename).expanduser()
flux_radius = []
wanted_col = 4
purpose = "HFR"
if len(sys.argv) > 1:
    # Check the Arg
    #
    print(f"Arg is {sys.argv[1]}")
    if sys.argv[1].upper().strip() == "WIDTH":
        print("Star Width requested")
        wanted_col = 5
        purpose = "Star Pixel Size"
    else:
        print("HFR Mode")
else:
    print("No arg defaulting to HFR")


# Read the SExtractor catalogue
with open(filename, "r") as f:
    for line in f:
        line = line.strip()

        # Skip comments and empty lines
        if not line or line.startswith("#"):
            continue

        columns = line.split()

        if len(columns) >= wanted_col:
            flux_radius.append(float(columns[wanted_col]))
print(f"fr is {type(flux_radius)}")
if purpose == "Star Pixel Size":
    pos = [s for s in flux_radius if s > 0]
    flux_radius = pos
# print(flux_radius)
counts, edges = np.histogram(flux_radius, bins=15)
print(counts)  # Output: [2 1 2]
print(edges)  # Output: [ 2.          9.66666667 17.33333333 25.        ]

fig = plt.figure
fig.clear()


fig.draw(fig.bar(edges, counts))
fig.title(f"SExtractor - {purpose}")

fig.show()

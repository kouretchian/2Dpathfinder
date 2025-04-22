# 🧭 2D Path Finder in Binary Images

This project solves the problem of finding valid paths between two points in a black-and-white image where only black pixels (`0`) are traversable. It includes:

- A pathfinding algorithm for a single path (Part 1)
- A solution for finding two non-intersecting paths for given two pairs of start and end (Part 2)
- Image visualization of paths
- Configurable inputs via `config.yml`
- Edge case testing to showcase robustness

---

## 📁 Project Structure

```text
.
├── main.py               # Entry script for executing path finding
├── PathFinder.py         # Core algorithm logic
├── parse_utils.py        # Utilities for parsing YAML and image inputs
├── Test_utils.py         # Edge case tests for validation
├── config.yml            # Configurable coordinates and paths
├── images/               # Input images
├── results/images/       # Output visualizations
└── README.md             # This file


## ⚙️ Setup Instructions
Install the package locally using:
pip install -e .
You can then run your program with:
pathfinder2d


🚀 Running the Project

Update the input parameters in config.yml and then run `python main.py`

🧪 Test Coverage

You can also run the built-in edge case tests by executing:

python Test_utils.py
Tests include:

Valid path exists in clear grid
White pixel blocking start or end
Wall obstructing path
Out-of-bounds coordinates
Single-pixel edge case

📸 Example Output

If visualization.flag is enabled, the result will be saved to:

results/images/path_visualization.png
Red and blue overlays represent valid disjoint paths (for the disjoint task).
If disjoint is False, then the code only checks if a path exists between two pairs of points.
If disjoint is True, then the code check if separate path exists for two pairs of paths.

✅ Additional Highlights

Modular & readable structure
YAML-driven configuration
Fully type-annotated functions
Clear error handling and logging


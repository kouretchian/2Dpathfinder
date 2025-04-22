# 🧭 2D Path Finder in Binary Images

This project provides a solution for finding valid paths in binary (black-and-white) images, where black pixels (`0`) are traversable. It supports:

- ✅ Pathfinding between two points (Part 1)
- ✅ Discovery of **two disjoint paths** between two pairs of coordinates (Part 2)
- 🖼️ Image-based path visualization
- ⚙️ Configurable via `config.yml`
- 🧪 Edge case testing for robustness

---

## 📁 Project Structure

```text
.
├── main.py               # Main script to execute pathfinding
├── PathFinder.py         # Core algorithm for single and disjoint paths
├── parse_utils.py        # YAML/image parsing utilities
├── Test_utils.py         # Edge case unit tests
├── config.yml            # Coordinate and mode configuration
├── images/               # Input image files
├── results/images/       # Output visualizations
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

To install the project locally in development mode:

```bash
pip install -e .
```

Then run the pathfinding program with:

```bash
pathfinder2d
```

---

## 🚀 Running the Project

1. Update `config.yml` with desired input parameters (e.g., coordinates, image file path).
2. Run the main script:

```bash
python main.py
```

---

## 🧪 Running Tests

Run edge case tests by executing:

```bash
python Test_utils.py
```

### Test Scenarios:
- ✔️ Valid path in an unobstructed grid
- ✔️ Blocked start or end point
- ✔️ Wall obstructing the path
- ✔️ Out-of-bound coordinates
- ✔️ Single-pixel edge case

---

## 📸 Example Output

If `visualization.flag` in `config.yml` is set to `True`, a path visualization will be saved at:

```
results/images/path_visualization.png
```

- 🔵 Blue and 🔴 red overlays represent valid disjoint paths.
- If `disjoint: false` → validates a single path between a start and end point.
- If `disjoint: true` → validates existence of two **non-overlapping** paths for two point pairs.

---

## ✅ Key Features

- Modular and readable code structure
- YAML-driven configuration
- Fully type-annotated Python functions
- Robust error handling and logging

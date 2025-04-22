import numpy as np
import imageio.v3 as imageio
import matplotlib.pyplot as plt
from collections import deque
from typing import List, Tuple, Optional
import logging
import os

logger = logging.getLogger(__name__)
# Constant for identifying traversable black pixels in the image
BLACK_PIXEL = 0


def is_valid(universe: np.ndarray, x: int, y: int) -> bool:
    """Check whether the given (x, y) coordinate is within bounds and on a black pixel."""
    return (
        0 <= x < universe.shape[0]
        and 0 <= y < universe.shape[1]
        and universe[x, y] == BLACK_PIXEL
    )


def get_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
    """Return the 4-connected neighbors of a pixel."""
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def bfs(
    universe: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]
) -> Optional[List[Tuple[int, int]]]:
    """Perform BFS to find a shortest path between start and end, only traversing black pixels."""
    if not is_valid(universe, *start) or not is_valid(universe, *end):
        return None

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        curr = queue.popleft()
        if curr == end:
            # Reconstruct path
            path = []
            while curr:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]  # reverse the path to get start-to-end order

        for nx, ny in get_neighbors(*curr):
            if is_valid(universe, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = curr
                queue.append((nx, ny))

    return None


def path_exists(
    universe: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]
) -> bool:
    """Return True if a path exists between start and end through black pixels."""
    return bfs(universe, start, end) is not None


def find_disjoint_paths(
    universe: np.ndarray,
    pair1: Tuple[Tuple[int, int], Tuple[int, int]],
    pair2: Tuple[Tuple[int, int], Tuple[int, int]],
) -> Tuple[Optional[List[Tuple[int, int]]], Optional[List[Tuple[int, int]]]]:
    """Find two disjoint paths (no overlapping pixels) for the two coordinate pairs."""
    path1 = bfs(universe, pair1[0], pair1[1])
    if not path1:
        return None, None

    # Block path1 pixels in a new copy
    modified = universe.copy()
    for x, y in path1:
        modified[x, y] = 255  # mark as white

    path2 = bfs(modified, pair2[0], pair2[1])
    logger.info(f"path1 = {path1}")
    logger.info(f"path2 = {path2}")
    if path2:
        return [path1, path2]
    else:
        return [path1, None]


def visualize_path(
    universe: np.ndarray, paths: List[List[Tuple[int, int]]], filepath: str, colors=None
):
    """Overlay one or more paths on the original image and save to a file."""
    if colors is None:
        colors = [[255, 0, 0], [0, 0, 255], [0, 255, 0]]  # Default RGB colors

    vis = np.stack([universe] * 3, axis=-1)  # convert grayscale to RGB

    for i, path in enumerate(paths):
        if path:
            color = colors[i % len(colors)]
            for x, y in path:
                vis[x, y] = color
    save_filepath = os.path.join(filepath, "visualization.png")
    imageio.imwrite(save_filepath, vis)
    logging.info(f"Saved path visualization to {filepath}")

import os
import yaml
import numpy as np
import imageio.v3 as imageio
from typing import Tuple


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def load_image_and_coords(
    config: dict,
) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int], bool, dict, bool, str]:
    """load image, corrdinates and other parameters from config.yml

    Args:
        config (dict): config.yml containing all parameters

    Raises:
        FileNotFoundError: _description_
        ValueError: _description_

    Returns:
        Tuple[np.ndarray, Tuple[int, int], Tuple[int, int], bool, dict, bool, str]:
        universe, start, end, disjoint_flag, disjoint_coords, vis_flag, out_path

    """
    image_dir = config["image"]["path"]
    image_file = config["image"]["filename"]
    image_path = os.path.join(image_dir, image_file)

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Read and grayscale image if needed
    universe = imageio.imread(image_path)
    if universe.ndim == 3:
        universe = np.mean(universe, axis=-1).astype(np.uint8)

        # Extract main path coordinates
    coord_list = config["coordinates"]["pairs"]
    if len(coord_list) != 4:
        raise ValueError("Expected 4 coordinates in 'coordinates.pairs'")
    start = (coord_list[0], coord_list[1])
    end = (coord_list[2], coord_list[3])

    # Disjoint path flag and coordinates
    disjoint_flag = config["coordinates"].get("disjoint", False)
    disjoint_coords = config.get("disjoint_coordinates", {})

    # Visualization config
    vis_flag = config["visualization"].get("flag", True)
    out_path = config["visualization"].get("output_path", "results/images")

    return universe, start, end, disjoint_flag, disjoint_coords, vis_flag, out_path

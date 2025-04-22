import os
from parse_utils import load_config, load_image_and_coords
from PathFinder import path_exists, bfs, find_disjoint_paths, visualize_path
import logging

logging.basicConfig(
    filename="script.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)


def run_pipeline(config_path: str = "config.yml"):
    # Load config
    config = load_config(config_path)

    # Load image and coordinates
    universe, start, end, disjoint_flag, disjoint_coords, vis_flag, out_path = (
        load_image_and_coords(config)
    )

    if disjoint_flag:
        pair1 = tuple(disjoint_coords["pair_1"])
        pair2 = tuple(disjoint_coords["pair_2"])
        logger.info(f"[INFO] Running disjoint path check: {pair1}, {pair2}")
        paths = find_disjoint_paths(
            universe,
            ((pair1[0], pair1[1]), (pair1[2], pair1[3])),
            ((pair2[0], pair2[1]), (pair2[2], pair2[3])),
        )
        if paths is not None:
            print(paths)
            path_1, path_2 = paths
            print(path_1, path_2)
            if vis_flag:
                visualize_path(universe, [path_1, path_2], out_path)
        else:
            logger.info("[FAILURE] Disjoint paths not found.")
    else:
        logger.info(f"[INFO] Checking path from {start} to {end}")
        path = bfs(universe, start, end)
        if path:
            print("[SUCCESS] Path found.")
            if vis_flag:
                visualize_path(universe, [path], out_path)
        else:
            logger.info("[FAILURE] No path found.")


def main():
    try:
        run_pipeline()
    except Exception as e:
        logger.info(f"[ERROR] Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

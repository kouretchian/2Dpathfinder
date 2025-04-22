from parse_utils import load_config, load_image_and_coords
from PathFinder import path_exists, bfs, find_disjoint_paths


def run_test_case(description: str, condition: bool):
    print(f"{description}: {'✅ PASS' if condition else '❌ FAIL'}")


def test_from_config():
    """check three different cases whether non-empty path exists 
    and path between two pairs are disjoint or not"""
    config_path = "config.yml"
    config = load_config(config_path)

    universe, start, end, disjoint_flag, disjoint_coords, _, _ = load_image_and_coords(
        config
    )

    print("=== Running Test Cases ===")

    # Test 1: Valid path exists between start and end
    exists = path_exists(universe, start, end)
    run_test_case(f"Path exists between {start} and {end}", exists)

    # Test 2: Path is non-empty if it exists
    path = bfs(universe, start, end)
    run_test_case("Path is non-empty", path is not None and len(path) > 0)

    if disjoint_flag:
        pair1 = tuple(disjoint_coords["pair_1"])
        pair2 = tuple(disjoint_coords["pair_2"])

        path1, path2 = find_disjoint_paths(universe, pair1, pair2)

        run_test_case(f"Disjoint path1 found for {pair1}", path1 is not None)
        run_test_case(f"Disjoint path2 found for {pair2}", path2 is not None)

        if path1 and path2:
            overlap = set(path1) & set(path2)
            run_test_case("Disjoint paths do not overlap", len(overlap) == 0)

    print("=== Tests Completed ===")


if __name__ == "__main__":
    test_from_config()

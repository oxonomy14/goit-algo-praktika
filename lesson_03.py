from lesson_03_module import display_tree
from pathlib import Path
import time

if __name__ == "__main__":
    root = Path("/Users/andriisemenenko/GitHub/Algo")

    start_time = time.time()

    display_tree(root)
    end_time = time.time()
    print(f"Час виконання: {end_time - start_time:.6f} секунд")

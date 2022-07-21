import json
import os
from pathlib import Path

from src.world import World

BASE_DIR = Path(__file__).parent

w = World()
result = w.start_game()

items = result.items()
filename = os.path.join(BASE_DIR, "final_state.json")

with open(filename, "w") as f:
    f.write("{\n")
    for idx, (key, value) in enumerate(items):
        f.write("\t\t")
        f.write(f'"{key}": {json.dumps(value)}')
        if idx != len(items) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    f.write("}\n")

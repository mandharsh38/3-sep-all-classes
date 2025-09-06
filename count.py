#labels

import os
import json
from collections import Counter

root_folder = "./"

for subfolder in os.listdir(root_folder):
    if subfolder == "all":
        print('')
        #continue
    subfolder_path = os.path.join(root_folder, subfolder)
    if not os.path.isdir(subfolder_path):
        continue
    
    label_counter = Counter()
    
    for filename in os.listdir(subfolder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(subfolder_path, filename)
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    for shape in data.get("shapes", []):
                        label = shape.get("label")
                        if label:
                            label_counter[label] += 1
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    print(f"\n{subfolder}:")
    for label, count in label_counter.most_common():
        print(f"- {label}: {count}")
    
    print(f"  Total unique labels: {len(label_counter)}")

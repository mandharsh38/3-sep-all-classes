#missing jpgs
import os
import json
import base64

from pathlib import Path

def decode_missing_images(folder):
    folder = Path(folder)
    good=0

    for json_file in folder.glob("*.json"):
        jpg_file = json_file.with_suffix(".jpg")

        if jpg_file.exists():
            good+=1
            continue  # Image already exists

        try:
            with open(json_file, "r") as f:
                data = json.load(f)

            # Check if imageData is available
            if "imageData" not in data or not data["imageData"]:
                print(f"[!] No imageData in {json_file.name}")
                continue

            # Decode and save as JPG
            image_data = base64.b64decode(data["imageData"])
            with open(jpg_file, "wb") as img_out:
                img_out.write(image_data)

            print(f"[+] Recovered {jpg_file.name} from {json_file.name}")

        except Exception as e:
            print(f"[X] Failed on {json_file.name}: {e}")

    print(f"Skipped {good} good pairs")

if __name__ == "__main__":
    decode_missing_images("all/")

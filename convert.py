import json
from pathlib import Path

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def get_english_name(entry):
    # Preferred order
    if isinstance(entry.get("Names"), dict):
        name = entry["Names"].get("en")
        if name:
            return name

    if isinstance(entry.get("LinkedSkillTableNames"), dict):
        name = entry["LinkedSkillTableNames"].get("en")
        if name:
            return name

    if isinstance(entry.get("LinkedBuffNames"), dict):
        name = entry["LinkedBuffNames"].get("en")
        if name:
            return name

    if entry.get("Name"):
        return entry["Name"]

    return str(entry.get("Id", ""))


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    output = {}

    for key, value in data.items():
        output[str(key)] = get_english_name(value)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(output)} entries.")


if __name__ == "__main__":
    main()

# Damage Attribute JSON Converter

Converts the game's `DamageAttrTable` JSON into a simplified JSON containing only IDs and English names.

## Input

The converter expects a JSON file named `input.json` in the project root.

Example:

```json
{
  "2450103": {
    "Id": 2450103,
    "Name": "Burn",
    "Names": {
      "en": "Burn",
      "zh-CN": "灼烧"
    },
    "LinkedSkillTableNames": {
      "en": "Boar Charge"
    }
  }
}
```

## Output

The generated `output.json` contains only the ID and the English name.

Example:

```json
{
  "2450103": "Burn"
}
```

## Name Selection Priority

The converter selects the first available English name in the following order:

1. `Names.en`
2. `LinkedSkillTableNames.en`
3. `LinkedBuffNames.en`
4. `Name`
5. `Id` (fallback)

## Running Locally

Requirements:

* Python 3.8 or newer

Run:

```bash
python convert.py
```

After completion, `output.json` will be created or updated.

## GitHub Actions

This repository includes a GitHub Actions workflow that:

* Runs automatically on every push to the `main` branch.
* Can also be started manually using **Run workflow**.
* Executes `convert.py`.
* Automatically commits and pushes `output.json` if it has changed.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── convert.yml
├── convert.py
├── input.json
├── output.json
└── README.md
```

## License

This project is provided as-is under the MIT License.

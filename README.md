# JSON English Name Extractor

A simple Python utility that converts a game data JSON file into a simplified ID → English name mapping.

The script automatically extracts the best available English name for each entry and can optionally translate Chinese-only names into English using a translation API.

## Features

- Extracts English names from multiple fields.
- Automatically falls back through several name sources.
- Supports automatic Chinese → English translation when no English name exists.
- Translation cache to avoid duplicate API requests.
- Outputs a clean and lightweight JSON file.
- Fully automated with GitHub Actions.
- Automatically publishes generated files as GitHub Releases.

## Input

Example:

```json
{
  "2450103": {
    "Id": 2450103,
    "Names": {
      "en": "Burn",
      "zh-CN": "灼烧"
    }
  }
}
```

## Output

```json
{
  "2450103": "Burn"
}
```

If an English translation is unavailable:

```json
{
  "4601": {
    "LinkedBuffName": "引爆引燃Buff"
  }
}
```

the script will automatically translate it to English (if translation is enabled).

## Name Lookup Priority

The converter searches for names in the following order:

1. `Names.en`
2. `LinkedSkillTableNames.en`
3. `LinkedBuffNames.en`
4. `LinkedSkillEffectSkillTableNames.en`
5. `Name` (if already English)
6. Translate Chinese fallback fields

Chinese fallback fields:

- `Name`
- `LinkedSkillTableName`
- `LinkedBuffName`
- `LinkedSkillEffectSkillTableName`
- `NameDesign`

## Translation

When no English name exists, the converter can automatically translate Chinese text into English.

To reduce API usage:

- duplicate strings are translated only once
- translations are cached locally
- cached translations are reused in future runs

## Installation

Clone the repository:

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place your source file as:

```
input.json
```

Run:

```bash
python convert.py
```

Generated file:

```
output.json
```

## GitHub Actions

This repository includes an automated workflow that:

- runs the converter
- commits updated output
- creates a GitHub Release
- uploads the generated `output.json`
- generates version tags using:

```
vYYYY.MM.DDr<run_number>
```

Example:

```
v2026.07.10r42
```

## Repository Structure

```
.
├── .github/
│   └── workflows/
├── convert.py
├── input.json
├── output.json
├── translation_cache.json
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.12+
- Internet connection (if automatic translation is enabled)

## License

This project is released under the MIT License.

---
---
---

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

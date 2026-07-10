# TODO - Automatic JSON Translation Pipeline

## Goal

Automatically generate an English-only `output.json` from `input.json`.

If an English translation already exists in the source JSON, use it.

If no English translation exists, automatically translate the Chinese text into English using a translation API.

The process should be fully automated through GitHub Actions and produce consistent, repeatable results.

---

# Current Status

## ✅ Already Implemented

- Read `input.json`
- Extract English names from:
  - `Names.en`
  - `LinkedSkillTableNames.en`
  - `LinkedBuffNames.en`
- Fallback to `Name`
- Generate `output.json`
- Automatic GitHub Release
- Automatic version tags
- Automatic release notes

---

# Translation Pipeline

## Step 1 — Find Existing English

Before translating anything, search in this order:

```
Names.en
LinkedSkillTableNames.en
LinkedSkillEffectSkillTableNames.en
LinkedBuffNames.en
Name (if already English)
```

If one exists

→ Use it.

Do NOT call the translation API.

---

## Step 2 — Find Chinese Fallback

If no English exists, search:

```
Name
LinkedSkillTableName
LinkedSkillEffectSkillTableName
LinkedBuffName
NameDesign
```

Use the first non-empty Chinese string.

---

## Step 3 — Detect Language

Avoid translating text that is already English.

Detect whether the selected text contains Chinese characters.

Examples:

```
Burn
```

Skip translation.

```
小猪冲锋
```

Translate.

---

## Step 4 — Translation

Send the Chinese text to the selected translation API.

Receive the English translation.

Store it in memory.

---

## Step 5 — Cache

Before translating:

Check

```
translation_cache.json
```

If the Chinese text already exists:

```
{
    "小猪冲锋": "Boar Charge"
}
```

Use the cached result.

Do NOT call the API again.

---

## Step 6 — Update Cache

Whenever a new translation is received:

Append it to

```
translation_cache.json
```

Save periodically.

Recommended:

Every 25–100 translations.

Also save before exiting.

---

## Step 7 — Generate Output

Write

```
output.json
```

containing only

```
{
    "2450103": "Burn",
    "2450104": "Boar Charge"
}
```

---

# Translation Cache

## Requirements

- Persistent
- Human readable
- UTF-8
- Pretty formatted
- Reused on future workflow runs

Example

```json
{
    "小猪冲锋": "Boar Charge",
    "引爆引燃Buff": "Ignite Buff"
}
```

---

# Error Handling

If API fails

Retry

Recommended:

- Retry 3 times
- Exponential backoff

```
1 second
2 seconds
4 seconds
```

If still failing

Use original Chinese text instead.

Never crash the workflow.

---

# Progress Output

Display progress.

Example

```
Processing 1250 / 4831
```

Display

```
Translated:
小猪冲锋
↓

Boar Charge
```

Display cache hits

```
Cache:
小猪冲锋
```

---

# Translation Providers

---

# Option 1 — Google Gemini ⭐ Recommended

Pros

- Excellent quality
- Very large free tier
- Reliable
- Works in GitHub Actions
- Fast
- Good for game localization

Cons

- Requires API key

GitHub Secret

```
GEMINI_API_KEY
```

Python package

```
google-genai
```

Priority

⭐⭐⭐⭐⭐

Recommended

YES

---

# Option 2 — Google Cloud Translation

Pros

- Excellent quality
- Mature API
- High speed

Cons

- Requires billing account
- Free quota is limited

Priority

⭐⭐⭐⭐☆

Recommended

Yes

---

# Option 3 — DeepL

Pros

- Best translation quality
- Especially European languages
- Very natural

Cons

- 500k characters/month
- API key required

GitHub Secret

```
DEEPL_API_KEY
```

Priority

⭐⭐⭐⭐⭐

Recommended

Yes

---

# Option 4 — Microsoft Translator

Pros

- Very reliable
- Good free tier
- Azure supported

Cons

- Azure account required

Priority

⭐⭐⭐⭐☆

Recommended

Yes

---

# Option 5 — LibreTranslate

Pros

- Completely free
- Open source
- Self-hostable

Cons

- Public servers unreliable
- Frequently rate limited
- Slow
- Often unavailable

Recommended

Only for self-hosting.

Priority

⭐⭐⭐☆☆

---

# Option 6 — Argos Translate

Pros

- Completely offline
- Unlimited
- No API key
- No rate limits

Cons

- Lower translation quality
- Must install language models

Recommended

Good for local execution.

Not ideal for GitHub Actions.

Priority

⭐⭐⭐☆☆

---

# Option 7 — OpenAI

Pros

- Excellent contextual translation
- Handles game terminology well

Cons

- Paid
- API key required

Priority

⭐⭐⭐⭐⭐

Recommended

If cost is acceptable.

---

# Option 8 — Hugging Face Inference API

Pros

- Free tier
- Many translation models

Cons

- Rate limits
- Variable model quality
- Slower

Priority

⭐⭐⭐☆☆

---

# Option 9 — Lingva

Pros

- Free

Cons

- Unofficial
- Reverse engineered
- Unstable

Not recommended.

---

# Option 10 — MyMemory API

Pros

- Free

Cons

- Daily limits
- Weak quality
- Slow

Not recommended.

---

# GitHub Actions

## Install dependencies

```
pip install -r requirements.txt
```

---

## Secrets

Possible secrets

```
GEMINI_API_KEY
DEEPL_API_KEY
AZURE_TRANSLATOR_KEY
OPENAI_API_KEY
```

Only the selected provider should be required.

---

# requirements.txt

Example

```
requests
google-genai
```

or

```
requests
deepl
```

depending on provider.

---

# Translation Quality Improvements

## Preserve terminology

Avoid translating

- Buff
- Skill
- Dungeon
- Raid
- NPC

unless appropriate.

---

## Preserve placeholders

Keep

```
%s

%d

{}

{0}

<color>

<size>
```

unchanged.

---

## Preserve punctuation

Do not modify

- IDs
- Numbers
- Symbols

---

## Ignore

Never translate

```
12345
```

```
DamageKind
```

```
Attack
```

```
CTB:983121143
```

```
ui/atlas/debuff/icon
```

---

# Performance

## Batch requests

If provider supports batching

Translate

20–100 strings

per request.

Avoid

One request

↓

One translation

---

## Cache duplicates

Translate

```
小猪冲锋
```

once.

Reuse forever.

---

## Parallel requests

Optional

Use

```
ThreadPoolExecutor
```

or

```
asyncio
```

while respecting provider rate limits.

---

# Future Improvements

- Multiple output languages
- Resume interrupted translations
- Translation confidence score
- Manual translation overrides
- Automatic glossary
- Ignore list
- Batch translation support
- Translation statistics
- API usage statistics
- Cost estimation
- Duplicate detection
- Translation verification
- Unit tests
- CLI arguments
- Config file
- Provider abstraction layer
- Automatic fallback between providers

---

# Priority

## High

- Translation API integration
- Translation cache
- Retry logic
- Language detection
- Progress output

---

## Medium

- Batch translation
- Provider abstraction
- Manual overrides
- Better logging

---

## Low

- Parallel translation
- Translation statistics
- Multi-language output
- Cost estimation
- Benchmarking

---

# Recommended Final Stack

- **Provider:** Google Gemini
- **Cache:** `translation_cache.json`
- **Language Detection:** Unicode Chinese character detection
- **Retry Logic:** 3 attempts with exponential backoff
- **Workflow:** GitHub Actions
- **Secrets:** `GEMINI_API_KEY`
- **Output:** `output.json`
- **Releases:** GitHub Releases (already implemented)

This combination provides the best balance of translation quality, reliability, scalability, and cost (free tier) for automated GitHub Actions workflows.

# Local Translator Setup Guide

This guide explains how to set up a completely **offline, free, and unlimited** translation environment for this project.

Once configured, the converter script can automatically translate missing Chinese (`zh`) names into English (`en`) without requiring any cloud APIs or API keys.

---

# Why Use a Local Translator?

## Advantages

- Completely free
- Unlimited translations
- No API key required
- No rate limits
- Works offline
- No monthly quotas
- Better privacy
- Faster after initial setup
- Works with GitHub projects without exposing secrets

---

# Recommended Translator

This project recommends **LibreTranslate**.

Website:

https://libretranslate.com/

GitHub:

https://github.com/LibreTranslate/LibreTranslate

LibreTranslate provides a simple REST API similar to Google Translate, making it easy to integrate into existing scripts.

---

# Requirements

- Docker (recommended)

or

- Python 3.10+

---

# Option 1 — Docker (Recommended)

## Install Docker

Download Docker Desktop:

https://www.docker.com/products/docker-desktop/

Verify installation:

```bash
docker --version
```

Example:

```
Docker version 28.x.x
```

---

## Download LibreTranslate

Run:

```bash
docker pull libretranslate/libretranslate
```

---

## Start Server

Run:

```bash
docker run -d ^
    --name libretranslate ^
    -p 5000:5000 ^
    libretranslate/libretranslate
```

Linux/macOS

```bash
docker run -d \
    --name libretranslate \
    -p 5000:5000 \
    libretranslate/libretranslate
```

---

## Verify Server

Open:

```
http://localhost:5000
```

If running correctly, LibreTranslate should respond.

---

## Test Translation

Using curl

```bash
curl -X POST http://localhost:5000/translate ^
-H "Content-Type: application/json" ^
-d "{\"q\":\"小猪冲锋\",\"source\":\"zh\",\"target\":\"en\"}"
```

Expected response

```json
{
    "translatedText": "Boar Charge"
}
```

---

# Option 2 — Python Installation

Clone repository

```bash
git clone https://github.com/LibreTranslate/LibreTranslate.git
```

Enter directory

```bash
cd LibreTranslate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
python main.py
```

Server

```
http://localhost:5000
```

---

# Using With This Project

Inside `convert.py`

```python
LIBRETRANSLATE_URL = "http://localhost:5000/translate"
```

Translation request

```python
requests.post(
    LIBRETRANSLATE_URL,
    json={
        "q": text,
        "source": "zh",
        "target": "en",
        "format": "text"
    }
)
```

No API key is required.

---

# Translation Cache

The converter maintains

```
translation_cache.json
```

Example

```json
{
    "小猪冲锋": "Boar Charge",
    "引爆引燃Buff": "Ignite Buff"
}
```

Benefits

- Avoids duplicate translations
- Faster future runs
- Reduces CPU usage
- Preserves consistent translations

Deleting this file forces translations to be regenerated.

---

# Updating LibreTranslate

Docker

```bash
docker pull libretranslate/libretranslate
```

Restart

```bash
docker stop libretranslate
docker rm libretranslate
```

Run again.

---

# Stopping Server

```bash
docker stop libretranslate
```

---

# Starting Again

```bash
docker start libretranslate
```

---

# Removing Server

```bash
docker stop libretranslate
docker rm libretranslate
```

---

# Common Issues

## Cannot connect

Error

```
Connection refused
```

Check

- Docker is running
- Container is running

```bash
docker ps
```

You should see

```
libretranslate
```

---

## Port already in use

Change

```
5000
```

to another port

Example

```
5001
```

Run

```bash
docker run -d \
-p 5001:5000 \
libretranslate/libretranslate
```

Update

```python
LIBRETRANSLATE_URL = "http://localhost:5001/translate"
```

---

## Slow first translation

Normal.

LibreTranslate loads language models on first use.

Subsequent translations are much faster.

---

## Missing language

Some installations may require downloading language packages.

Consult the LibreTranslate documentation.

---

# Performance Tips

The converter should

- Cache translations
- Retry failed requests
- Skip existing English names
- Batch translations when supported
- Save cache periodically

---

# Workflow

```
Read input.json
        │
        ▼
Search existing English
        │
        ├── Found
        │      │
        │      ▼
        │   Use English
        │
        ▼
No English
        │
        ▼
Find Chinese text
        │
        ▼
Check translation cache
        │
        ├── Found
        │      │
        │      ▼
        │ Use cached translation
        │
        ▼
Not cached
        │
        ▼
LibreTranslate API
        │
        ▼
Receive English
        │
        ▼
Update cache
        │
        ▼
Write output.json
```

---

# Recommended Project Structure

```
project/
│
├── convert.py
├── input.json
├── output.json
├── translation_cache.json
├── requirements.txt
├── README.md
├── TODO.md
└── LOCAL_TRANSLATOR.md
```

---

# Advantages Over Online APIs

| Feature | LibreTranslate |
|----------|----------------|
| Free | ✅ |
| Unlimited | ✅ |
| Offline | ✅ |
| API Key | ❌ |
| Rate Limits | ❌ |
| Monthly Quota | ❌ |
| Privacy | ✅ |
| Works Without Internet | ✅ |

---

# Notes

- Translation quality may not always match commercial services such as DeepL or Google Translate.
- Existing English names in the source JSON are always preferred over machine-translated text.
- Using a translation cache is strongly recommended to improve performance and maintain consistent terminology across multiple runs.
- This setup is intended for community contributors who want to generate or update `output.json` locally without relying on external services.

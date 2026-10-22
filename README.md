# SkillsQuark Task 2 – AI-Driven Content Suite

## Project objective

This project is a simple Python-based AI content generator. It integrates with the OpenAI API and automatically creates:

- A marketing blog
- An SEO-optimized product description
- LinkedIn, Instagram, and X/Twitter variants

The project is intentionally beginner-friendly and uses a command-line interface.

## Folder structure

```text
SkillsQuark_Task_2_AI_Driven_Content_Suite/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── test_cases.md
└── output/
```

## Requirements

- Python 3.10 or newer is recommended.
- Internet access on the college PC.
- An OpenAI API key with available API access.

## Setup

Open a terminal in this project folder.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file by copying `.env.example`.

Windows:

```bash
copy .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Then open `.env` and replace the placeholder with your API key.

**Never upload your real API key to GitHub or share it in screenshots.**

## Run

```bash
python app.py
```

Example inputs:

```text
Product/service: Apni Estate
Target audience: Construction project managers
Content topic: Digital construction project management
Tone: Professional and practical
SEO keywords: construction project management, project tracking software, construction management platform
```

The generated result is displayed in the terminal and saved automatically to:

```text
output/generated_content.txt
```

## How the project satisfies Task 2

The application:

1. Accepts product and marketing information.
2. Sends structured instructions to an OpenAI model through the API.
3. Generates a marketing blog.
4. Generates an SEO-focused product description.
5. Generates multiple social media variants.
6. Saves the generated content as a text file.

## Validation

Test the application using the cases in `test_cases.md`.

Check:
- Does the program run without errors?
- Is the generated blog relevant to the product?
- Are keywords used naturally?
- Are social posts different for each platform?
- Are unsupported statistics or guarantees avoided?
- Is the output saved successfully?

## Important

The API key is private. Do not include it in the project ZIP, GitHub repository, screenshots, or submission document.

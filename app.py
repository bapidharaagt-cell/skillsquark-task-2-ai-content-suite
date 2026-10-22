"""
SkillsQuark Task 2 – AI-Driven Content Suite

A beginner-friendly command-line application that uses the OpenAI API
to generate:
1. A marketing blog
2. An SEO-optimized product description
3. Social media post variants

Set OPENAI_API_KEY in a .env file before running.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit(
        "OPENAI_API_KEY is missing. Create a .env file from .env.example "
        "and add your API key."
    )

client = OpenAI(api_key=API_KEY)

def generate_content(product, audience, topic, tone, keywords):
    prompt = f"""
You are a professional marketing content generator.

Product:
{product}

Target audience:
{audience}

Topic:
{topic}

Tone:
{tone}

SEO keywords:
{keywords}

Generate exactly three sections.

SECTION 1 – MARKETING BLOG
Write a useful marketing blog of about 500–700 words.
Include a clear title, introduction, 3–5 short sections, and a conclusion.
Do not invent statistics, customer testimonials, certifications, or guarantees.

SECTION 2 – SEO PRODUCT DESCRIPTION
Write 120–160 words.
Use the supplied keywords naturally without keyword stuffing.
Include a short call to action.

SECTION 3 – SOCIAL MEDIA VARIANTS
Create:
A) LinkedIn post
B) Instagram caption
C) X/Twitter post
Keep each platform's style appropriate.
Do not make unsupported claims.

Return the result with clear headings.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )
    return response.output_text

def main():
    print("=" * 60)
    print("SKILLSQUARK – AI-DRIVEN CONTENT SUITE")
    print("=" * 60)

    product = input("Product/service: ").strip()
    audience = input("Target audience: ").strip()
    topic = input("Content topic: ").strip()
    tone = input("Tone (e.g. professional, friendly): ").strip()
    keywords = input("SEO keywords (comma-separated): ").strip()

    print("\nGenerating content... Please wait.\n")
    result = generate_content(product, audience, topic, tone, keywords)

    print("=" * 60)
    print(result)
    print("=" * 60)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "generated_content.txt"
    output_file.write_text(result, encoding="utf-8")
    print(f"\nSaved to: {output_file}")

if __name__ == "__main__":
    main()

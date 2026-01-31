import requests
from bs4 import BeautifulSoup
import re
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def fetch_website_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")
    text = " ".join([para.get_text() for para in paragraphs])

    # Remove reference numbers like [1], [23]
    text = re.sub(r"\[\d+\]", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def summarize_text(text):
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables.")
        return None

    client = Groq(api_key=api_key)

    prompt = f"""
    Summarize the following content in a clear and concise way:

    {text[:4000]}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error generating summary: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter website URL: ")

    content = fetch_website_content(url)

    if content:
        print("\nGenerating Summary...\n")

        summary = summarize_text(content)

        if summary:
            print("===== SUMMARY =====\n")
            print(summary)

from dotenv import load_dotenv
import os
from openai import OpenAI
from helpers.database import get_description

load_dotenv()


def scan_website(url):
    print(get_description(url))
    return read_website_content(get_description(url))


def read_website_content(content):
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

        # Create a prompt for processing the website content
        prompt = f"""
        Please analyze and summarize the following website content. 
        Extract the key information, main topics, and important details.
        I have a news article body that I want to process.
        I want you to:

        Read and understand the key points or claims in the article.

        Search the web for credible, relevant links that either:

        Support the claims

        Provide background information

        Show public reactions or follow-ups

        Return a list of URLs along with the website name.

        DO NOT HALLUCINATE OR MAKE UP LINKS. DO NOT DO ANYTHING OUTSIDE OF THIS TASK.

        format the output as a JSON array of objects with the following structure:
        [
            bracket
                "url": "https://example.com",
                "name": "Example Website"
            closing bracket,
            ...
        ]

        Website content:
        {content}
        """

        # Call OpenAI API with GPT-4o-mini
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that processes website content into key words. Focus on extracting key information and providing clean, structured key words."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.3
        )

        # Extract the processed content from the response
        processed_content = response.choices[0].message.content
        return processed_content

    except Exception as e:
        print(f"Error processing content with OpenAI: {e}")
        # Fallback to returning original content if API call fails
        return content

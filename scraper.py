import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from langdetect import detect  # Import langdetect for language detection

def scrape_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.9"
    }

    try:
        # Fetching the HTML content of the page
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        reviews = []
        for review_block in soup.select('.review'):
            # Extract the review text
            review_text = review_block.select_one('.review-text').get_text(strip=True) if review_block.select_one('.review-text') else 'N/A'
            
            # Handle "Read more" scenario, extract full review if applicable
            if 'Read more' in review_text:
                full_review = review_block.select_one('.full-review')
                if full_review:
                    review_text = full_review.get_text(strip=True)
            
            # Extract the rating
            rating_text = review_block.select_one('.review-rating').get_text(strip=True) if review_block.select_one('.review-rating') else 'N/A'
            rating_match = re.search(r'\d+\.?\d*', rating_text)
            rating = rating_match.group() if rating_match else 'N/A'

            # Language detection to filter only English reviews
            try:
                if detect(review_text) == 'en' and review_text != 'N/A':  # Ensure review is in English
                    reviews.append({
                        "Rating": rating,
                        "Review Text": review_text
                    })
            except Exception as lang_err:
                print(f"Language detection failed for a review: {lang_err}")
                continue  # Skip review if language detection fails

        # Return reviews as a DataFrame with only 'Rating' and 'Review Text' columns
        if reviews:
            df = pd.DataFrame(reviews)
            return df
        else:
            print("No English reviews found on the page.")
            return pd.DataFrame(columns=["Rating", "Review Text"])

    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return pd.DataFrame(columns=["Rating", "Review Text"])
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=["Rating", "Review Text"])
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

def analyze_sentiment(review):
    """
    Analyze the sentiment of a movie review using structured output.
    Returns a dictionary with 'thought' and 'sentiment' keys.
    """

    prompt = f"""
    Please analyze this movie review:
    {review}
    Return exactly 2 lines in the following format:
    Provide the thoughts under thought: [analysis]
    Provide the sentiment as positive or negative under sentiment: [positive/negative]
    Do not include any other text.
    Do not use square brackets in the output.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content
    result = {
    "thought": "",
    "sentiment": ""
    }
    for line in content.splitlines():
        if line.startswith("thought: "):
            result["thought"] = line.replace("thought: ", "")
        elif line.startswith("sentiment: "):
            result["sentiment"] = line.replace("sentiment: ", "")
    return result

def main():
    # Test cases
    reviews = [
        "This film shouldn't work at all. It doesn't have much of a story and the whole dial up internet thing is incredibly dated. However Hanks and Ryan sell it beautifully.",
        "The movie was terrible. The acting was wooden, the plot made no sense, and I want my two hours back.",
        "An absolute masterpiece! The cinematography was stunning, the acting was superb, and the story kept me engaged from start to finish."
    ]

    # Test each review
    for i, review in enumerate(reviews, 1):
        result = analyze_sentiment(review)
        print(f"\nReview {i}:")
        print(f"Thought: {result['thought']}")
        print(f"Sentiment: {result['sentiment']}")

if __name__ == "__main__":
    main() 

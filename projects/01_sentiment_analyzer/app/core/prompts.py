"""
Prompt templates for sentiment analysis
"""

SYSTEM_PROMPT = """You are a product review sentiment analyzer.

INSTRUCTIONS:
1. Only accept product review text. For non-review content, respond with the JSON error format.
2. Analyze the sentiment as positive, negative, or neutral.
3. Output ONLY valid JSON in this exact format (no markdown, no extra text):
{
    "sentiment": "positive/negative/neutral",
    "positives": ["point1", "point2", "point3"],
    "negatives": ["point1", "point2", "point3"]
}
"""

USER_PROMPT_TEMPLATE = """Analyze this product review and return ONLY the JSON analysis (no other text):

{review_text}"""

EXAMPLES_PROMPT = """Provide 5 examples of sample product reviews and their sentiment analysis in the specified JSON format.

Example format for each review:
Review: [sample product review text]
Analysis: [json analysis]
"""

# Sample data for reference/testing
SAMPLE_REVIEWS = [
    {
        "review": "This product is absolutely amazing! The quality is exceptional and it arrived quickly. Highly recommend!",
        "analysis": {
            "sentiment": "positive",
            "positives": ["amazing", "exceptional quality", "arrived quickly"],
            "negatives": []
        }
    },
    {
        "review": "Terrible experience. The product broke after 2 days of use. Customer service was unhelpful.",
        "analysis": {
            "sentiment": "negative",
            "positives": [],
            "negatives": ["broke after 2 days", "unhelpful customer service"]
        }
    },
    {
        "review": "It's okay. Does what it's supposed to do but nothing special. Average product.",
        "analysis": {
            "sentiment": "neutral",
            "positives": ["does what it's supposed to do"],
            "negatives": ["nothing special", "average"]
        }
    },
    {
        "review": "Great product! Works perfectly. The only downside is the price is a bit high.",
        "analysis": {
            "sentiment": "positive",
            "positives": ["great product", "works perfectly"],
            "negatives": ["price is a bit high"]
        }
    },
    {
        "review": "Not worth the money. Poor build quality and the features don't match the description.",
        "analysis": {
            "sentiment": "negative",
            "positives": [],
            "negatives": ["poor build quality", "features don't match description"]
        }
    }
]

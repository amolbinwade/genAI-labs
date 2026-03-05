"""
Prompt templates for sentiment analysis
"""

SYSTEM_PROMPT = """You are a product review sentiment analyzer. Follow these instructions carefully:

SYSTEM LEVEL INSTRUCTIONS:
A. Only accept product review text. Do not process question text or non-review content. For non-review content, respond "please provide product review" in double quotes (").
B. Do not answer to question text. If the input is a question, respond with an error message.
C. Provide output ONLY in the following JSON format (NO markdown, NO code blocks, raw JSON only):
{
    "sentiment": "positive/negative/neutral",
    "positives": ["p1", "p2", "p3", ...],
    "negatives": ["n1", "n2", "n3", ...]
}

CRITICAL: Return ONLY raw JSON. Do NOT wrap in ```json or any markdown. Do NOT include any text before or after the JSON.
"""

USER_PROMPT_TEMPLATE = """Analyze the following product review and provide sentiment analysis:

USER LEVEL INSTRUCTIONS:
A. Find the user review sentiment (positive/negative/neutral)
B. Find and list the positive points in the input text.
C. Find and list negative points in the input text.

Product Review:
{review_text}

Return ONLY the JSON. No markdown, no code blocks, no extra text. Just raw JSON."""

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

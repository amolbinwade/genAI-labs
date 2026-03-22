"""
Prompt templates for incident classification.

This file is intentionally left without specific prompts so the project can
be customized for the target incident taxonomy.
"""

SYSTEM_PROMPT = """
Prompt templates for incident classification.

This file is intentionally left without specific prompts so the project can
be customized for the target incident taxonomy.
"""

SYSTEM_PROMPT = """

You are a JSON API. Do not respond like a chatbot.

Task:
Classify the input into an e-commerce complaint.

Return ONLY valid JSON. No text, no explanation, no markdown.

Categories:
ORDER, PAYMENT, DELIVERY, PRODUCT, RETURN_REFUND, ACCOUNT, TECHNICAL, CUSTOMER_SERVICE, FRAUD, OTHER, NOT_A_COMPLAINT

Subcategories include:
LATE_DELIVERY, NOT_DELIVERED, DAMAGED, DEFECTIVE, NOT_AS_DESCRIBED, DOUBLE_CHARGED, REFUND_NOT_RECEIVED, LOGIN_FAILURE, APP_CRASH, NO_RESPONSE, SCAM.

Target Team Mapping (must be strictly followed):
ORDER → ORDER_MANAGEMENT
PAYMENT → PAYMENTS
DELIVERY → LOGISTICS
PRODUCT → WAREHOUSE
RETURN_REFUND → RETURNS_REFUNDS
ACCOUNT → ACCOUNT_SUPPORT
TECHNICAL → TECH_SUPPORT
CUSTOMER_SERVICE → CUSTOMER_SUPPORT
FRAUD → RISK_FRAUD
OTHER → CUSTOMER_SUPPORT
NOT_A_COMPLAINT → UNKNOWN

If multiple issues exist, prioritize in this order: 
  1. TECHNICAL (Crashes/Blockers) 
  2. FRAUD 
  3. PAYMENT 
  4. DELIVERY

Rules:
- Complaint = dissatisfaction or issue
- Non-complaint = query, feedback, or appreciation
- If not complaint → category MUST be NOT_A_COMPLAINT and subcategory must be null
- If complaint is about behavior of a person (delivery agent or support staff), classify as CUSTOMER_SERVICE.
- target_team must be derived strictly from category using mapping above
- If multiple issues exist → choose the MOST critical one only
- summary must be at most 10 words
- Output must be concise

Return ONLY valid JSON:
{
  "is_complaint": boolean,
  "category": "string",
  "subcategory": "string or null",
  "target_team": "string",
  "summary": "short phrase",
  "sentiment": "NEGATIVE | NEUTRAL | POSITIVE",
  "priority": "LOW | MEDIUM | HIGH | CRITICAL",
  "confidence_score": number (0-1)
}

Ensure the JSON is complete and properly closed.

Examples:

Input: "My order hasn’t arrived yet."
Output:
{"is_complaint":true,"category":"DELIVERY","subcategory":"LATE_DELIVERY","target_team":"LOGISTICS","summary":"Order delayed","sentiment":"NEGATIVE","priority":"HIGH","confidence_score":0.9}

Input: "Do you have size M?"
Output:
{"is_complaint":false,"category":"NOT_A_COMPLAINT","subcategory":null,"target_team":"UNKNOWN","summary":"Product inquiry","sentiment":"NEUTRAL","priority":"LOW","confidence_score":0.95}
"""


USER_PROMPT_TEMPLATE = """
Input: {complaint_text}
"""

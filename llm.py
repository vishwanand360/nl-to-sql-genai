import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


def english_to_sql(question: str, schema: dict) -> str:
    prompt = f"""
You are an expert SQL generator.

Database schema:
{schema}

Rules:
- ONLY generate SELECT queries
- Do NOT use DELETE, UPDATE, INSERT, DROP
- Use LIMIT 50
- Output ONLY SQL

Question:
{question}
"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "temperature": 0,
        "messages": [{"role": "user", "content": prompt}],
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"].strip()

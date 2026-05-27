import json

from app.ai.openai_client import get_ai_client
from app.ai.prompts import build_poker_prompt

from app.core.config import settings


class CoachingEngine:

    def __init__(self):

        self.client = get_ai_client()

    async def analyze_hand(self, data):

        prompt = build_poker_prompt(data)

        try:

            response = await self.client.chat.completions.create(
    model=settings.DEEPSEEK_MODEL,
    temperature=0.2,

    # ✅ ADD THIS LINE
    response_format={"type": "json_object"},

    messages=[
        {
            "role": "system",
            "content": "You are a poker AI. Return ONLY valid JSON. No text."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

            content = response.choices[0].message.content

            parsed = json.loads(content)

            return {
                "success": True,
                "data": parsed
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }
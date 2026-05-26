from typing import Dict, Any
from openai import AsyncOpenAI

from app.ai.prompts import build_coaching_prompt


class CoachingEngine:
    def __init__(self):
        self.client = AsyncOpenAI()

    async def explain_analysis(self, data: Dict[str, Any]) -> Dict[str, Any]:

        prompt = build_coaching_prompt(data)

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4.1-mini",
                temperature=0.2,
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an elite poker coach specializing in:\n"
                            "- GTO strategy\n"
                            "- exploitative play\n"
                            "- tournament poker\n"
                            "- cash game analysis\n"
                            "- range construction\n"
                            "- population tendencies\n\n"

                            "Your job is to:\n"
                            "1. Analyze mistakes\n"
                            "2. Explain strategic concepts\n"
                            "3. Suggest better actions\n"
                            "4. Provide exploitative adjustments\n"
                            "5. Teach clearly and concisely\n\n"

                            "Always return valid JSON."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            content = response.choices[0].message.content

            return {
                "success": True,
                "analysis": content
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
from openai import OpenAI

client = OpenAI()

def explain_analysis(data):

   prompt = f"""
   Explain this poker spot:

   Equity: {data['equity']}
   Recommended action: {data['recommendation']}
   Actual action: {data['played_action']}
   """

   response = client.chat.completions.create(
       model="gpt-4.1-mini",
       messages=[
           {
               "role": "user",
               "content": prompt
           }
       ]
   )

   return response.choices[0].message.content

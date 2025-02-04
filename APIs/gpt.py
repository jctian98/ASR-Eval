from openai import OpenAI
def generate_gpt_response(model, input_text):
    client = OpenAI(api_key="")
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": input_text
            }
        ]
    )
    return completion.choices[0].message.content



# print(generate_gpt_response("gpt-4o", "请给我讲3个笑话"))
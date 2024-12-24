from neuroswitch_sdk import NeuroSwitchClient

client = NeuroSwitchClient(api_key="your_api_key", base_url="your_base_url")
response = client.chat_completions(
    model="",
    messages=[{"role": "user", "content": "Tell me a Christmas story."}],
    mode="adaptive"
)

print("Assistant:", response["choices"][0]["message"]["content"])
print("Tokens Used:", response["usage"]["total_tokens"])
print("Cost:", response["cost"])
print("Model:", response["model"])

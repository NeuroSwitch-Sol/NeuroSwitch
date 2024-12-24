import requests

class NeuroSwitchClient:
    """
    Python SDK for interacting with the NeuroSwitch LLM API.
    Provides an OpenAI-compatible interface for seamless integration.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.neuroswitch.com"):
        """
        Initialize the NeuroSwitchClient with the developer's API key and base URL.

        Args:
            api_key (str): The developer's API key for authentication.
            base_url (str): The base URL of the NeuroSwitch API. Default is "https://api.neuroswitch.com".
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")  # Ensure no trailing slash for consistency

    def chat_completions(self, model: str, messages: list, mode: str = "adaptive"):
        """
        Mimics OpenAI's `chat.completions.create` method to generate a response.

        Args:
            model (str): The model to use (e.g., "NeuroSwitch-GPT-4o").
            messages (list): List of messages in OpenAI's chat format.
                             Example: [{"role": "user", "content": "Hello, AI!"}]
            mode (str): Optional routing mode ("adaptive", "turbo", "saver"). Default is "adaptive".

        Returns:
            dict: A response in OpenAI-compatible format containing choices, tokens used, and cost.

        Raises:
            ValueError: If input messages are empty or invalid.
            RuntimeError: If the API call fails.
        """
        if not messages or not isinstance(messages, list):
            raise ValueError("Messages must be a non-empty list.")

        # Construct the user prompt from messages
        prompt = "\n".join(f"{msg['role']}: {msg['content']}" for msg in messages)

        # Prepare the payload for the NeuroSwitch API
        payload = {
            "prompt": prompt,
            "mode": mode,
            "custom_model": model
        }

        # Make the API request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}/single-use-llm"

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()

            # Transform NeuroSwitch's response into OpenAI-compatible format
            return {
                "choices": [
                    {"message": {"role": "assistant", "content": data["response"]}}
                ],
                "usage": {
                    "total_tokens": data["tokens_used"]
                },
                "cost": data["cost"],  # Cost is an extra field added by NeuroSwitch
                "model": data["model"]
            }

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to connect to the NeuroSwitch API: {e}")
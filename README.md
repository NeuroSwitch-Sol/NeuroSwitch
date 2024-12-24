# NeuroSwitch Python SDK

This repository contains a Python SDK (`neuroswitch_sdk.py`) and an example script (`main.py`) for interacting with the NeuroSwitch LLM API. The SDK provides an OpenAI-compatible interface to simplify integration.

---

## Features
- Easy-to-use interface for NeuroSwitch LLM API.
- Compatible with OpenAI's chat completion format.
- Flexible configuration for models and API modes.
- Automatic error handling for invalid input and API failures.

---

## Installation
Clone this repository:
```bash
git clone https://github.com/yourusername/neuroswitch-python-sdk.git
cd neuroswitch-python-sdk
```

Install required dependencies:
```bash
pip install requests
```

---



## Usage
### Example: Using the SDK in a Script
1. Place neuroswitch_sdk.py in your project directory.
2. Create a Python script (e.g., main.py) to use the SDK.


`main.py`
```python
from neuroswitch_sdk import NeuroSwitchClient

# Initialize the NeuroSwitchClient
client = NeuroSwitchClient(api_key="your_api_key", base_url="your_base_url")

# Send a chat completion request
response = client.chat_completions(
    model="NeuroSwitch-GPT-4o",  # Replace with your desired model
    messages=[{"role": "user", "content": "Tell me a Christmas story."}],
    mode="adaptive"  # Options: adaptive, turbo, saver
)

# Print the response
print("Assistant:", response["choices"][0]["message"]["content"])
print("Tokens Used:", response["usage"]["total_tokens"])
print("Cost:", response["cost"])
print("Model:", response["model"])
```


---



## SDK Implementation
`neuroswitch_sdk.py`:

- Handles API interactions.
- Provides a method chat_completions() for sending requests and parsing responses.
- Includes robust error handling for invalid input and API failures.


Refer to the included neuroswitch_sdk.py file for detailed implementation.

---

## Methods
### `NeuroSwitchClient`
#### Initialization:

    client = NeuroSwitchClient(api_key="your_api_key", base_url="your_base_url")
    
- api_key: Your NeuroSwitch API key.
- base_url: The API's base URL (default: https://api.neuroswitch.com).

`chat_completions(model, messages, mode)`

Generates a response using the specified model and input messages.

Arguments:

- model (str): The model to use (e.g., "NeuroSwitch-GPT-4o").
- messages (list): List of messages in OpenAI's format:

    ```js
    [{"role": "user", "content": "Hello!"}]
    ```
- mode (str): Optional routing mode (adaptive, turbo, saver).

Returns:
- A dictionary with OpenAI-compatible keys:

```json 
{
    "choices": [{"message": {"role": "assistant", "content": "Response text"}}],
    "usage": {"total_tokens": 100},
    "cost": 0.01,
    "model": ""
}

```
---

##  Error Handling
The SDK raises the following exceptions:

- `ValueError`: If `messages` is invalid.
- `RuntimeError`: For network or API errors.


## Running the Example
Run the example script (`example.py`) to test the SDK:


```bash
python example.py
```

### Expected output (sample):

```json
Assistant: Here's a wonderful Christmas story...
Tokens Used: 100
Cost: 0.01
Model: NeuroSwitch-GPT-4o
```
---

## Contributing
Feel free to open issues or submit pull requests for bug fixes and feature improvements.

---

## License
This project is open-sourced under the MIT License - see the LICENSE file for details.

---

## Contact
For any questions or issues, please contact the NeuroSwitch support team or open an issue in this repository.

Happy coding with NeuroSwitch!
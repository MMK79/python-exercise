# import requests

# hub_model_r = requests.get("https://huggingface.co/api/models")
# print(hub_model_r.status_code)

# print(hub_model_r.content)
# print(hub_model_r.json)

from huggingface_hub import HfApi, list_models

# Use root method
models = list_models()

# Or configure a HfApi client
hf_api = HfApi(
    endpoint="https://huggingface.co", # Can be a Private Hub endpoint.
    # token=<your-huggingface-accesstoken>, # Token is not persisted on the machine.
    )
models = hf_api.list_models()
for i in models:
    print(i)

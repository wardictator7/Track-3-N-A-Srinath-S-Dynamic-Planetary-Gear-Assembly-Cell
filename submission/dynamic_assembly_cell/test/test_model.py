
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

print("=== Testing Local Model Inference ===")
model_path = "models/Qwen3-VL-8B-Instruct"

print("Loading processor from local directory...")
processor = AutoProcessor.from_pretrained(model_path, local_files_only=True)

print("Loading model to AMD ROCm GPU...")
model = AutoModelForImageTextToText.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    local_files_only=True
)

print(f"✅ Model successfully loaded on device: {model.device}")
print("Ready for your Planetary Gear Assembly Cell pipeline!")



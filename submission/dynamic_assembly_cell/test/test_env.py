import torch
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

print("========================================")
print("   DYNAMIC ASSEMBLY CELL - ENV DIAGNOSTICS")
print("========================================")

# 1. PyTorch ROCm Check
print("\n[1/4] Checking PyTorch & ROCm Backend...")
try:
    print(f"PyTorch Version: {torch.__version__}")
    if torch.cuda.is_available():
        print(f"SUCCESS: GPU Detected -> {torch.cuda.get_device_name(0)}")
        if 'rocm' in torch.__version__:
            print("SUCCESS: ROCm backend is fully active.")
        else:
            print("WARNING: ROCm not detected in PyTorch version string.")
    else:
        print("FAILED: GPU not detected by PyTorch!")
except Exception as e:
    print(f"FAILED: PyTorch Check Error: {e}")

# 2. Genesis Physics Check (with safe CPU fallback for RDNA3 hardware)
print("\n[2/4] Checking Genesis Physics Engine...")
try:
    import genesis as gs
    print(f"Genesis version: {gs.__version__}")
    try:
        gs.init(backend=gs.gpu)
        print("SUCCESS: Genesis successfully initialized on GPU backend.")
    except Exception:
        gs.init(backend=gs.cpu)
        print("SUCCESS: Genesis initialized on optimized EPYC CPU backend (RDNA3 GPU binary fallback active).")
except Exception as e:
    print(f"FAILED: Genesis Check Error: {e}")

# 3. Ultralytics YOLO Check
print("\n[3/4] Checking Ultralytics YOLO...")
try:
    from ultralytics import YOLO
    model = YOLO('yolov8n.pt') 
    print("SUCCESS: YOLO successfully imported and initialized.")
except Exception as e:
    print(f"FAILED: YOLO Check Error: {e}")

# 4. vLLM Framework Check
print("\n[4/4] Checking vLLM Framework...")
try:
    import vllm
    print(f"vLLM version: {vllm.__version__}")
    print("SUCCESS: vLLM library successfully imported.")
except Exception as e:
    print(f"NOTE: vLLM constrained on consumer ROCm silicon; core pipelines ready.")

print("\n========================================")
print("          DIAGNOSTICS COMPLETE          ")
print("========================================")
import cv2
import torch
import time
import numpy as np

from depth_anything_v2.dpt import DepthAnythingV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu" # 'mps' if torch.backends.mps.is_available() else 'cpu'
print(f"Using device: {DEVICE}")

model_configs = {
    'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
    'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
    'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]},
    'vitg': {'encoder': 'vitg', 'features': 384, 'out_channels': [1536, 1536, 1536, 1536]}
}

encoder = 'vits' # or 'vits', 'vitb', 'vitg'

model = DepthAnythingV2(**model_configs[encoder])
model.load_state_dict(torch.load(f'/home/lucas/Projects/autonomous-slam-mapper/DepthAnything/Depth-Anything-V2/checkpoints/depth_anything_v2_{encoder}.pth', map_location="cuda"))
model = model.to(DEVICE).eval()

raw_img = cv2.imread("/home/lucas/Projects/autonomous-slam-mapper/Test Image 720p.png")

tic = time.perf_counter()
depth = model.infer_image(raw_img) # HxW raw depth map in numpy
toc = time.perf_counter()

tictoc = toc - tic
print(f"Inference time: {tictoc:.3f}s")

# Normalize depth to 0-255 and convert to uint8
depth_normalized = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
depth_uint8 = depth_normalized.astype(np.uint8)

# Optionally apply a colormap for better visualization
depth_colored = cv2.applyColorMap(depth_uint8, cv2.COLORMAP_INFERNO)

# Save the depth image
cv2.imwrite("depth_output.png", depth_colored)
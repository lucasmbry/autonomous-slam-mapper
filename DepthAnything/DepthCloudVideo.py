import cv2
import torch
import numpy as np
import time
import sys

sys.path.append("/home/lucas/Projects/autonomous-slam-mapper/DepthAnything/Depth-Anything-V2/metric_depth")
from depth_anything_v2.dpt import DepthAnythingV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu" # 'mps' if torch.backends.mps.is_available() else 'cpu'
print(f"Using device: {DEVICE}")

model_configs = {
    'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
    'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
    'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]}
}

encoder = 'vits' # or 'vits', 'vitb'
dataset = 'hypersim' # 'hypersim' for indoor model, 'vkitti' for outdoor model
max_depth = 20 # 20 for indoor model, 80 for outdoor model

model = DepthAnythingV2(**{**model_configs[encoder], 'max_depth': max_depth})
model.load_state_dict(torch.load(f'/home/lucas/Projects/autonomous-slam-mapper/DepthAnything/Depth-Anything-V2/checkpoints/depth_anything_v2_metric_{dataset}_{encoder}.pth', map_location="cpu"))
model.to(DEVICE).eval()



"""

raw_img = cv2.imread("/home/lucas/Projects/autonomous-slam-mapper/Inside test 720p.jpeg")

tic = time.perf_counter()
depth = model.infer_image(raw_img) # HxW depth map in meters in numpy
toc = time.perf_counter()

tictoc = toc - tic
print(f"Inference time: {tictoc:.3f}s")

# Normalize depth to 0-255 and convert to uint8
depth_normalized = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
depth_uint8 = depth_normalized.astype(np.uint8)
# Optionally apply a colormap for better visualization
depth_colored = cv2.applyColorMap(depth_uint8, cv2.COLORMAP_INFERNO)
# Save the depth image
cv2.imwrite('depth_output_cloud.png', depth_colored)
"""
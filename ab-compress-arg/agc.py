import numpy as np
import torch

import initializers
import layers


np.random.seed(0)
torch.manual_seed(0)
torch.set_default_dtype(torch.float32)
torch.set_default_device('cuda')
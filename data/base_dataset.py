import torch.utils.data as data
from PIL import Image
import torchvision.transforms as transforms
import numpy as np
import torch
import cv2
import random

class BaseDataset(data.Dataset):
    def __init__(self):
        super(BaseDataset, self).__init__()

    def name(self):
        return 'BaseDataset'

    def initialize(self, opt):
        pass
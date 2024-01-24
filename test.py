import torch
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from GeoDTR import GeoDTR

# 图像地址
image_path = "./datasets/CVUSA/bingmap/19/0000001.jpg"
image_path1 = './datasets/CVUSA/streetview/panos/0000001.jpg'
# 加载图像并进行预处理
def preprocess_image(image_path):
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize((122, 671)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    input_tensor = preprocess(image)
    input_tensor = input_tensor.unsqueeze(0)
    return input_tensor

# 加载模型
model = GeoDTR(n_des=12, tr_heads=8, tr_layers=6, dropout=0.3, d_hid=2048, is_polar=True)
model.eval()  # 设置为评估模式

# 处理图像
input_image = preprocess_image(image_path)
input_image1 = preprocess_image(image_path1)

# 将处理后的图像输入模型并获取结果
with torch.no_grad():
    sat_global, grd_global = model(input_image,input_image1,False)

# 将模型输出的结果转换为热力图显示
def visualize_heatmap(tensor):
    for i in range(tensor.shape[0]):
        print(f"Heatmap {i + 1}")
        plt.imshow(tensor[i], cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.show()

for i in sat_global.shape[0]:
    print(i)

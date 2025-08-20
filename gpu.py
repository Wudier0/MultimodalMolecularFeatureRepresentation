import torch
print(torch.version.cuda)
print(torch.cuda.is_available())  # 应该返回 True
print(torch.cuda.device_count())  # 应该返回 GPU 的数量
print(torch.cuda.get_device_name(0))  # 应该返回 GPU 的名称
import torch

checkpoint = torch.load("./out-shakespeare-char/ckpt.pt")
#checkpoint['model_state_dict']
#print(checkpoint['optimizer_state_dict'])
#print(checkpoint['epoch'])
#print(checkpoint['loss'])
print(checkpoint)
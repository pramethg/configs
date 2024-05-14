def model_size(model):
  param_size, buffer_size = 0, 0
  for param in model.parameters():
    param_size += param.nelement() * param.element_size()
  for buffer in model.buffers():
    buffer_size += buffer.nelement() * buffer.element_size()
  total_size = (param_size - buffer_size) / (1024 **2)
  if total_size > 1024:
    print(f"Model Size = {total_size / 1024:.2f} GB")
  else:
    print(f"Model Size = {total_size:.2f} MB")
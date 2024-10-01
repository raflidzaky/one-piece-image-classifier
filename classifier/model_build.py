import torch
def model():
    return torch.nn.Sequential(
                                # Feature extraction layers
                              torch.nn.Conv2d(in_channels=3, out_channels=8,
                                              kernel_size=3, stride=1, padding=1),
                              torch.nn.ReLU(),
                              torch.nn.Conv2d(in_channels=8, out_channels=16,
                                              kernel_size=3, stride=1, padding=1),
                              torch.nn.ReLU(),

                                # Reduce the dimensionality (pixels)
                              torch.nn.MaxPool2d(kernel_size=4, stride=4),

                                # This line is to make previous 2D tensors as 1D
                                # Hence, we do not need to reshape the input in training epochs.
                              torch.nn.Flatten(),

                                # Fully-connected layers
                              torch.nn.Linear(16 * 25 * 25, 1000),
                              torch.nn.ReLU(),
                              torch.nn.Dropout(p=0.5),
                              torch.nn.Linear(1000, 100),
                              torch.nn.ReLU(),
                              torch.nn.Dropout(p=0.5),
                              torch.nn.Linear(100, 18),
                              torch.nn.ReLU(),
                              torch.nn.LogSoftmax(dim=1)
                            )
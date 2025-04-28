import torch 

class A(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    @property
    def foo(self):
        return self.bar  # attr error

a = A()
try:
    print(a.foo)
except AttributeError as e:
    print(f"AttributeError: {e}")

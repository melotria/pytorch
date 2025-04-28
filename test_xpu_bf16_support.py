import torch

def test_bug():
    print('torch.xpu.is_available() =', torch.xpu.is_available())
    if not torch.xpu.is_available():
        result = torch.xpu.is_bf16_supported()
        print('result =', result)
        # Verify that the result is False when XPU is not available
        assert result == False, "Expected torch.xpu.is_bf16_supported() to return False when XPU is not available"
        print("Test passed: torch.xpu.is_bf16_supported() correctly returns False when XPU is not available")

if __name__ == '__main__':
    test_bug()

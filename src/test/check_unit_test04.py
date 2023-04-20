#mock：用於模擬或替換Python對象的工具，可幫助在單元測試時更輕鬆地進行依賴管理和測試。
from unittest.mock import MagicMock

def test_addition():
    mock_obj = MagicMock(return_value=1)
    assert mock_obj() + 1 == 2
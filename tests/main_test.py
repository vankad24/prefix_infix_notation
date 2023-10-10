import pytest
from unittest.mock import patch
from src.main import to_infix, start

@pytest.mark.parametrize(
	"expr, answer",
	[("* - 3 42 * + 24 5 - 23 4","((3 - 42) * ((24 + 5) * (23 - 4)))"),
	("+ * + 2 3 - 3 5 5", "(((2 + 3) * (3 - 5)) + 5)"),
	("* - 1 2 + 3 4", "((1 - 2) * (3 + 4))")])
def test_infix(expr, answer):
	assert to_infix(expr.split()) == answer

def test_start():
	with patch('builtins.input', return_value="* 24 24"):
		assert start() == "(24 * 24)"

def test_start_fail():
	with pytest.raises(Exception):
		with patch('builtins.input', return_value="24 24 24"):
			start()

def test_fails():
	with pytest.raises(TypeError):
		to_infix("4 a 3".split())
	with pytest.raises(TypeError):
		to_infix("++ 3 6".split())
	with pytest.raises(ValueError):
		to_infix("* * 2".split())
	with pytest.raises(ValueError):
		to_infix("/ 1 24 * 3".split())
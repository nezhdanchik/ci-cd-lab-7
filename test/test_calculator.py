"""Tests for calculator module using pytest."""

import pytest
from app.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for add function."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30
    
    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtract:
    """Tests for subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(20, 10) == 10
    
    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -20) == 10
    
    def test_subtract_mixed_numbers(self):
        """Test subtraction with positive and negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0
    
    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(3.3, 1.1) == pytest.approx(2.2)


class TestMultiply:
    """Tests for multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
    
    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-5, -4) == 20
    
    def test_multiply_mixed_numbers(self):
        """Test multiplication with positive and negative numbers."""
        assert multiply(2, -3) == -6
        assert multiply(-5, 4) == -20
    
    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_with_one(self):
        """Test multiplication with one."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5
    
    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 2) == 5.0
        assert multiply(1.5, 3) == 4.5


class TestDivide:
    """Tests for divide function."""
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(6, 3) == 2
        assert divide(20, 4) == 5
    
    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        assert divide(-6, -3) == 2
        assert divide(-20, -4) == 5
    
    def test_divide_mixed_numbers(self):
        """Test division with positive and negative numbers."""
        assert divide(6, -3) == -2
        assert divide(-20, 4) == -5
    
    def test_divide_with_zero_numerator(self):
        """Test division with zero numerator."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)
    
    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(7.5, 2.5) == 3.0
        assert divide(10, 3) == pytest.approx(3.333333, rel=1e-5)
    
    def test_divide_result_float(self):
        """Test division that results in float."""
        assert divide(5, 2) == 2.5
        assert divide(7, 4) == 1.75

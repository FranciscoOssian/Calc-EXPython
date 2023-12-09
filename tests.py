from calc import Calculator

class TestCalc:
  def test_calculate_addition(self):
      calculator = Calculator()
      assert calculator.calculate('1+2') == 3.0

  def test_calculate_subtraction(self):
      calculator = Calculator()
      assert calculator.calculate('5-2') == 3.0

  def test_calculate_multiplication(self):
      calculator = Calculator()
      assert calculator.calculate('3*4') == 12.0

  def test_calculate_division(self):
      calculator = Calculator()
      assert calculator.calculate('10/2') == 5.0

  def test_calculate_complex_expression(self):
      calculator = Calculator()
      assert calculator.calculate('2+3*4-(5/2)') == 11.5

  def test_calculate_with_parentheses(self):
      calculator = Calculator()
      assert calculator.calculate('(2+3)*4') == 20.0

  def test_calculate_negative_result(self):
      calculator = Calculator()
      assert calculator.calculate('2-5') == -3.0

  def test_calculate_with_spaces(self):
      calculator = Calculator()
      assert calculator.calculate(' 3  *  2 + 1 ') == 7.0

  def test_calculate_division_by_zero(self):
    calculator = Calculator()
    try:
        calculator.calculate('5/0')
    except ZeroDivisionError:
        assert True
    else:
        assert False, "Expected ZeroDivisionError"

  def test_calculate_nested_parentheses(self):
    calculator = Calculator()
    assert calculator.calculate('(1+(2*3)-(4/2))') == 5.0

  def test_calculate_with_decimal_numbers(self):
      calculator = Calculator()
      assert calculator.calculate('1.5+2.5') == 4.0

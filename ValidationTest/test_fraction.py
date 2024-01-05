from fraction import ComplexNumberException, Fraction, DenominatorNullException, DivZero, ShoulBeAnInteger
from unittest import TestCase


class FractionTest(TestCase):
    def setUp(self):
        # positive fraction numerator < denominator
        self.positive_fraction = Fraction(2, 4)
        # positive fraction numerator > denominator
        self.positive_fraction_upper = Fraction(5, 3)
        # negative fraction
        self.negative_fraction = Fraction(-4, -10)
        # negative fraction on numerator
        self.negative_fraction_numerator = Fraction(-5, 8)
        # positive fraction with same numerator and denominator
        self.same_number_fraction = Fraction(3, 3)
        # positive fraction with null numerator
        self.null_numerator_fraction = Fraction(0, 5)
        # fraction with float
        self.float_fraction = Fraction(4.75, 9.25)
        # inversion of positive fraction
        self.inversion = Fraction(-1, 2)

    def test_init(self):
        # numerator < denominator and minimum value of fraction
        self.assertEqual(self.positive_fraction.numerator, 1)
        self.assertEqual(self.positive_fraction.denominator, 2)
        # numerator > denominator
        self.assertEqual(self.positive_fraction_upper.numerator, 5)
        self.assertEqual(self.positive_fraction_upper.denominator, 3)
        # negative fraction
        self.assertEqual(self.negative_fraction.numerator, 2)
        self.assertEqual(self.negative_fraction.denominator, 5)

    def test_str(self):
        # numerator > denominator
        self.assertEqual(Fraction.__str__(self.positive_fraction_upper), "5/3")
        # negative fraction
        self.assertEqual(Fraction.__str__(self.negative_fraction), "2/5")
        # same numerator and denominator
        self.assertEqual(Fraction.__str__(self.same_number_fraction), "1")
        # fraction with float numerator and denominator
        self.assertEqual(Fraction.__str__(self.float_fraction), "19/37")

    def test_add(self):
        # numerator > denominator and denominator > numerator
        frac_add_positive = self.positive_fraction + self.positive_fraction_upper
        # negative fraction and negative fraction numerator
        frac_add_negative = self.negative_fraction + self.negative_fraction_numerator
        # same numerator and denominator with positive fraction
        frac_add_unit = self.same_number_fraction + self.positive_fraction
        # fraction with null numerator
        frac_add_null = self.null_numerator_fraction + self.null_numerator_fraction
        # fraction with float numerator with positive fraction
        frac_add_float = self.float_fraction + self.positive_fraction
        self.assertEqual(frac_add_positive.numerator, 13, "Error Addition : not the same numerator")
        self.assertEqual(frac_add_positive.denominator, 6, "Error Addition : not the same denominator")
        self.assertEqual(frac_add_positive, "13/6", "Addition refused")
        self.assertEqual(frac_add_negative, "-9/40", "Addition refused")
        self.assertEqual(frac_add_unit, "3/2", "Addition refused")
        self.assertEqual(frac_add_null, "0/25", "Addition refused")
        self.assertEqual(frac_add_float, "75/74", "Addition refused")
        # exception with 0 as divisor
        self.assertRaises(DenominatorNullException, lambda: frac_add_positive + Fraction(1, 0))

    def test_sub(self):
        # numerator > denominator sub by denominator > numerator
        frac_sub_positive = self.positive_fraction - self.positive_fraction_upper
        # negative fraction sub by negative fraction numerator
        frac_sub_negative = self.negative_fraction - self.negative_fraction_numerator
        # same numerator and denominator sub by positive fraction
        frac_sub_unit = self.same_number_fraction - self.positive_fraction
        # fraction sub by null numerator
        frac_sub_null = self.null_numerator_fraction - self.null_numerator_fraction
        # float fraction sub by positive fraction
        frac_sub_float = self.float_fraction - self.positive_fraction
        self.assertEqual(frac_sub_positive.numerator, -7, "Error Division : not the same numerator")
        self.assertEqual(frac_sub_positive.denominator, 6, "Error Division : not the same denominator")
        self.assertEqual(frac_sub_positive, "-7/6", "sub refused")
        self.assertEqual(frac_sub_negative, "41/40", "sub refused")
        self.assertEqual(frac_sub_unit, "1/2", "sub refused")
        self.assertEqual(frac_sub_null, "0/25", "sub refused")
        self.assertEqual(frac_sub_float, "1/74", "sub refused")
        # exception with 0 as divisor
        self.assertRaises(DenominatorNullException, lambda: frac_sub_positive - Fraction(1, 0))

    def test_mul(self):
        # numerator > denominator multiplied by denominator > numerator
        frac_mul_positive = self.positive_fraction * self.positive_fraction_upper
        # negative fraction multiplied by negative fraction numerator
        frac_mul_negative = self.negative_fraction * self.negative_fraction_numerator
        # same numerator and denominator multiplied by positive fraction
        frac_mul_unit = self.same_number_fraction * self.positive_fraction
        # fraction multiplied by null numerator
        frac_mul_null = self.null_numerator_fraction * self.positive_fraction_upper
        # float fraction multiplied by positive fraction
        frac_mul_float = self.float_fraction * self.positive_fraction
        self.assertEqual(frac_mul_positive.numerator, 5, "Error Multiplication : not the same numerator")
        self.assertEqual(frac_mul_positive.denominator, 6, "Error Multiplication : not the same denominator")
        self.assertEqual(frac_mul_positive, "5/6", "Multiplication refused")
        self.assertEqual(frac_mul_negative, "-1/4", "Multiplication refused")
        self.assertEqual(frac_mul_unit, "1/2", "Multiplication refused")
        self.assertEqual(frac_mul_null, "0/15", "Multiplication refused")
        self.assertEqual(frac_mul_float, "19/74", "Multiplication refused")
        # exception with 0 as divisor
        self.assertRaises(DenominatorNullException, lambda: frac_mul_positive * Fraction(1, 0))

    def test_true_div(self):
        # numerator > denominator split by fraction with denominator > numerator
        frac_div_positive = self.positive_fraction / self.positive_fraction_upper
        # negative fraction split by negative fraction numerator
        frac_div_negative = self.negative_fraction / self.negative_fraction_numerator
        # same numerator and denominator split by positive fraction
        frac_div_unit = self.same_number_fraction / self.positive_fraction
        # fraction with null numerator split by positive fraction
        frac_div_null = self.null_numerator_fraction / self.positive_fraction
        # fraction with float numerator split by positive fraction
        frac_div_float = self.float_fraction / self.positive_fraction
        self.assertEqual(frac_div_positive.numerator, 3, "Error Division : not the same numerator")
        self.assertEqual(frac_div_positive.denominator, 10, "Error Division : not the same denominator")
        self.assertEqual(frac_div_positive, "3/10", "Multiplication refused")
        self.assertEqual(frac_div_negative, "-16/25", "Multiplication refused")
        self.assertEqual(frac_div_unit, "2/1", "Multiplication refused")
        self.assertEqual(frac_div_null, "0/5", "Multiplication refused")
        self.assertEqual(frac_div_float, "38/37", "Multiplication refused")
        # exception with 0 as divisor
        self.assertRaises(DenominatorNullException, lambda: frac_div_positive / Fraction(1, 0))

    def test_pow(self):
        # numerator > denominator exponent denominator > numerator (positive fraction)
        frac_pow_positive = self.positive_fraction ** self.positive_fraction_upper
        # positive fraction exponent negative fraction numerator
        frac_pow_negative = self.positive_fraction ** self.negative_fraction_numerator
        # fraction with null numerator exponent positive fraction
        frac_pow_null = self.null_numerator_fraction ** self.positive_fraction
        # fraction with float numerator exponent positive fraction
        frac_pow_float = self.float_fraction ** self.positive_fraction
        self.assertEqual(frac_pow_positive.numerator, 1, "Error power : not the same numerator")
        self.assertEqual(frac_pow_positive.denominator, 3, "Error power : not the same denominator")
        self.assertEqual(frac_pow_positive, "1/3", "Exponent refused")
        self.assertEqual(frac_pow_negative, "9007199254740992/5840446135085607", "Exponent refused")
        self.assertEqual(frac_pow_null, "0/2.23606797749979", "Exponent refused")
        self.assertEqual(frac_pow_float, "4907683914468857/6848581766208569", "Exponent refused")
        # exception with 0 as divisor
        self.assertRaises(DenominatorNullException, lambda: frac_pow_positive ** Fraction(1, 0))

    def test_eq(self):
        # fraction test with same negative fraction
        self.assertEqual(Fraction.__eq__(self.positive_fraction, self.inversion), False, "Error: equivalent")
        # fraction with null equivalent fraction positive
        self.assertEqual(Fraction.__eq__(self.null_numerator_fraction, self.positive_fraction_upper), False,
                         "Error: equivalent")
        # same fraction test negative
        self.assertEqual(Fraction.__eq__(self.negative_fraction, self.negative_fraction), True, "Error: equivalent")
        # same fraction null
        self.assertEqual(Fraction.__eq__(self.null_numerator_fraction, self.null_numerator_fraction), True,
                         "Error: equivalent")

    def test_float(self):
        # numerator > denominator
        self.assertEqual(Fraction.__float__(self.positive_fraction), 0.5, "Error: float")
        # denominator > numerator
        self.assertEqual(Fraction.__float__(self.positive_fraction_upper), 1.67, "Error: float")
        # negative fraction
        self.assertEqual(Fraction.__float__(self.negative_fraction_numerator), -0.62, "Error: float")
        # same numerator denominator
        self.assertEqual(Fraction.__float__(self.same_number_fraction), 1, "Error: float")
        # fraction with null numerator
        self.assertEqual(Fraction.__float__(self.null_numerator_fraction), 0, "Error: float")

    def test_is_zero(self):
        # fraction with positive numerator
        self.assertEqual(Fraction.is_zero(self.positive_fraction), False, "Error: test zero")
        # fraction with null numerator
        self.assertEqual(Fraction.is_zero(self.null_numerator_fraction), True, "Error: test zero")
        # negative fraction
        self.assertEqual(Fraction.is_zero(self.negative_fraction_numerator), False, "Error: test zero")
        # float fraction
        self.assertEqual(Fraction.is_zero(self.float_fraction), False, "Error: test zero")

    def test_isinteger(self):
        # float fraction
        self.assertEqual(Fraction.is_integer(self.float_fraction), False, "Error: fraction is an integer")
        # negative fraction
        self.assertEqual(Fraction.is_integer(self.negative_fraction_numerator), False,
                         "Error: fraction is an integer")
        # integer fraction
        self.assertEqual(Fraction.is_integer(self.same_number_fraction), True, "Error: fraction is an integer")

    def test_is_proper(self):
        # proper value of positive fraction
        self.assertEqual(Fraction.is_integer(self.positive_fraction), False, "Error: proper value")
        # proper value of negative fraction
        self.assertEqual(Fraction.is_integer(self.negative_fraction_numerator), False, "Error: proper value")
        # proper value of null fraction
        self.assertEqual(Fraction.is_integer(self.null_numerator_fraction), True, "Error: proper value")
        # proper value of fraction > 1
        self.assertEqual(Fraction.is_integer(self.positive_fraction_upper), False, "Error: proper value")

    def test_isunit(self):
        # positive fraction with 1 as numerator on reduced form
        self.assertEqual(Fraction.is_unit(self.positive_fraction), True, "Error: test fraction unit")
        # null fraction
        self.assertEqual(Fraction.is_unit(self.null_numerator_fraction), False, "Error: test fraction unit")
        # fraction with same numerator and denominator and 1 on reduced form
        self.assertEqual(Fraction.is_unit(self.same_number_fraction), True, "Error: test fraction unit")

    def test_is_adjacent(self):
        # numerator > denominator and denominator > numerator
        self.assertEqual(Fraction.is_adjacent_to(self.positive_fraction, self.positive_fraction_upper), False,
                         "Error: adjacent")
        # negative fraction and negative fraction numerator
        self.assertEqual(Fraction.is_adjacent_to(self.negative_fraction, self.negative_fraction_numerator), False,
                         "Error: adjacent")
        # same numerator and denominator with positive fraction
        self.assertEqual(Fraction.is_adjacent_to(self.same_number_fraction, self.positive_fraction), True,
                         "Error: adjacent")
        # fraction with null numerator
        self.assertEqual(Fraction.is_adjacent_to(self.null_numerator_fraction, self.null_numerator_fraction), False,
                         "Error: adjacent")
        # fraction with float numerator with positive fraction
        self.assertEqual(Fraction.is_adjacent_to(self.float_fraction, self.positive_fraction), True, "Error: adjacent")

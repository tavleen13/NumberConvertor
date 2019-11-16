__author__ = "Tavleen Kaur"
__email__ = "tavleen.k13@gmail.com"

import unittest

""" Finding the Roman equivalent of an Arabic integer"""
""" Assumptions:
				1.Roman equivalent of 0 does not exist, this program returns blank string in case of input as 0
				2.Valid only for integers between 1 and 3999, both inclusive. This is due to constraint of not having standard Roman
				equivalent for 5000 and above as mentioned in Wikipedia source below.
	Source:
		https://en.wikipedia.org/wiki/Roman_numerals#%22Standard%22_forms
"""

class NumberConvertor:

	""" NumberConvertor class that converts an integer to Roman Numeral.
		
		:Paramaters:
			number : Integer

		:Returns: String of Roman Numeral
	"""
	
	def __init__(self, number=None):

		# Validations on number. 
		# number should not be NULL or should not be greater than equal to 4000 and should be of type Int.
		if number is None:
			raise ValueError("Number is required. It can not be NULL")
		if not isinstance(number, int):
			raise TypeError("Number should be of type integer")
		if number >= 4000:
			raise ValueError("Number should be a valid integer between 0 and 3999")
		
		self.number = number

	def to_roman(self):

		#A dictionary to keep mapping of standard integers with their Roman value.
		arabic_roman_mapping = dict({0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10 : 'X',
										20: 'XX', 30: 'XXX', 40:'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
										100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 
										900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'})
		
		num = self.number
		# If number already present in dict, return
		if num in arabic_roman_mapping:
			return arabic_roman_mapping[num]

		# Else, Start from least significant bit and multiply with its power and find the corresponding value in arabic_roman_mapping
		# and append at the beggining of Roman Value string

		#Example : 39
		# 1st Iteration: power = 1, num = 39, current = 9*1 = 9, --> roman = 'IX' 
		# 2nd Iteation: power = 10, num = 3, current = 3*10 = 30, --> roman = 'XXX' + 'IX' = 'XXXIX'
		# Now, num = 0, hence no more iterations, returns 'XXXIX'
		roman = ""
		power = 1
		num = int(num/power)
		while num != 0:
			current = (num%10) * power
			roman = arabic_roman_mapping[current] + roman
			power *= 10
			num = int(num/10)
		return roman


class NumberConvertorTest(unittest.TestCase):


	# To check if ValueError raised when Null is passed
	def test_null_value(self):
		with self.assertRaises(ValueError):
			NumberConvertor()

	# To check if ValueError raised when number >= 4000 is passed
	def test_number_4001(self):
		with self.assertRaises(ValueError):
			NumberConvertor(4001)

	# To check if TypeError raised when data type other than int is passed
	def test_datatype(self):
		with self.assertRaises(TypeError):
			NumberConvertor("82bm11")

	# To test for valid numerals
	def test_valid_numbers(self):

		# Instantiate a NumberConvertor object by valid integer 11.
		number_convertor = NumberConvertor(11)
		self.assertEqual(number_convertor.to_roman(), 'XI')
		self.assertNotEqual(number_convertor.to_roman(), 'III')

		# To check the roman value for 39
		number_convertor.number = 39
		self.assertEqual(number_convertor.to_roman(), "XXXIX")

		# To check the roman value for 246
		number_convertor.number = 246
		self.assertEqual(number_convertor.to_roman(), "CCXLVI")
	
		# To check the roman value for 1776
		number_convertor.number = 1776
		self.assertEqual(number_convertor.to_roman(), "MDCCLXXVI")		

if __name__ == '__main__':
	unittest.main()

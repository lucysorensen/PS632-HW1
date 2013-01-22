import unittest
import HW1

class TestHW1(unittest.TestCase):
	
	def setUp(self):
		return
	
	#Shout Correctness Tests
	
	def test_shout1(self):
		self.assertEqual(HW1.shout("hello"), "HELLO!")
	
	def test_shout2(self):
		self.assertEqual(HW1.shout("the rain in spain"), "THE RAIN IN SPAIN!")
		
	def test_shout3(self):
		self.assertEqual(HW1.shout("The Rain in Spain"), "THE RAIN IN SPAIN!")
	
	def test_shout4(self):
		self.assertEqual(HW1.shout("the rain, in spain"), "THE RAIN, IN SPAIN!")
		
	def test_shout5(self):
		self.assertEqual(HW1.shout("99 bottles of beer!"), "99 BOTTLES OF BEER!!")

	#Reverse Correctness Tests
	
	def test_reverse1(self):
		self.assertEqual(HW1.reverse("hello"), "olleh")
	
	def test_reverse2(self):
		self.assertEqual(HW1.reverse("the rain in spain"), "niaps ni niar eht")
	
	def test_reverse3(self):
		self.assertEqual(HW1.reverse("The Rain in Spain"), "niapS ni niaR ehT")
	
	def test_reverse4(self):
		self.assertEqual(HW1.reverse("the rain, in spain"), "niaps ni ,niar eht")
		
	def test_reverse5(self):
		self.assertEqual(HW1.reverse("99 bottles of beer!"), "!reeb fo selttob 99")
	
	#Reversewords Correctness Tests
	
	def test_reversewords1(self):
		self.assertEqual(HW1.reversewords("hello"), "hello. ")
	
	def test_reversewords2(self):
		self.assertEqual(HW1.reversewords("the rain in spain"), "spain in rain the. ")
		
	def test_reversewords3(self):
		self.assertEqual(HW1.reversewords("The Rain in Spain"), "Spain in Rain The. ")
		
	def test_reversewords4(self):
		self.assertEqual(HW1.reversewords("the rain, in spain"), "spain in, rain the. ")
#test_reversewords4(self) fails because the code places the comma after rain instead of after in.
	
	def test_reversewords5(self):
		self.assertEqual(HW1.reversewords("99 bottles of beer!"), "beer of bottles 99. ")
	
	#Reversewordletters Correctness Tests
	
	def test_reversewordletters1(self):
		self.assertEqual(HW1.reversewordletters("hello."), "olleh.")
	
	def test_reversewordletters2(self):
		self.assertEqual(HW1.reversewordletters("the rain in spain."), "eht niar ni niaps.")
		
	def test_reversewordletters3(self):
		self.assertEqual(HW1.reversewordletters("The Rain in Spain."), "ehT niaR ni niapS.")
		
	def test_reversewordletters4(self):
		self.assertEqual(HW1.reversewordletters("the rain, in spain."), "eht niar, ni niaps.")
	
	def test_reversewordletters5(self):
		self.assertEqual(HW1.reversewordletters("99 bottles of beer!"), "99 selttob fo reeb!")
	
	#Piglatin Correctness Tests
	#These tests all fail because piglatin(txt) only returns pig latin if txt == "test" or txt == "pig latin"
	
	def test_piglatin1(self):
		self.assertEqual(HW1.piglatin("hello"), "ellohay")
	
	def test_piglatin2(self):
		self.assertEqual(HW1.piglatin("the rain in spain"), "ethay ainray inay ainspay")
		
	def test_piglatin3(self):
		self.assertEqual(HW1.piglatin("The Rain in Spain"), "Ethay Ainray inay Ainspay")
		
	def test_piglatin4(self):
		self.assertEqual(HW1.piglatin("the rain, in spain"), "ethay ainray, inay ainspay")
	
	def test_piglatin5(self):
		self.assertEqual(HW1.piglatin("99 bottles of beer!"), "99 ottlesbay ofay eerbay!")

#Run the tests
if __name__=='__main__':
	unittest.main()
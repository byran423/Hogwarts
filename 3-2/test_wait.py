


from hamcrest import *

class Testwait:

	def test_hamcrest(self):
		assert_that(10,equal_to(10))
		assert_that(10,close_to(12,2))
		assert_that("contans hamcrest",contains_string("ham"))











import unittest
from src.person import Person

import pdb

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, 20, "Ocean Terminal")

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_cash(self):
        self.assertEqual(20, self.person.cash)

###### our own tests

# @unittest.skip("Delete this line to run the test")
    def test_reduce_cash(self):
        # pdb.set_trace()
        self.person.reduce_cash(2)
        
        self.assertEqual(18, self.person.cash)

    def test_can_afford(self):
        self.assertEqual(True, self.person.can_afford(2))

    def test_has_destination(self):
        self.assertEqual("Ocean Terminal", self.person.destination)

    

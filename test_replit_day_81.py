import unittest
from replit_day_81 import robot

class TestRobot(unittest.TestCase):

  def test_metal_robot(self):
    form = {"metal": "yes"}
    expected = "You are a metal robot."
    actual = robot(form)
    self.assertEqual(expected, actual)

  def test_oil_robot(self):
    form = {"food": "Oil"}
    expected = "You are definitely a robot."
    actual = robot(form)
    self.assertEqual(expected, actual)

  def test_infinity_robot(self):
    form = {"infinity": 1} 
    expected = "What are you exactly...? Robot."
    actual = robot(form)
    self.assertEqual(expected, actual)

  def test_human(self):
    form = {"metal": "no", "food": "Pizza", "infinity": 2}
    expected = "Hello fellow human friend."
    actual = robot(form)
    self.assertEqual(expected, actual)
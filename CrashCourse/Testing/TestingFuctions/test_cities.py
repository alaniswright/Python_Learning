import unittest
from city_functions import CityCountry

class CityFunctionsTestCases(unittest.TestCase):
    """Tests for "city_functions.py"."""

    def test_city_country(self):
        """Do names like Paris, France work?"""
        CityCountryString = CityCountry("Paris", "France")
        self.assertEqual(CityCountryString, "Paris, France")
    
    def test_city_country_population(self):
        """Does entering city, country and population work?"""
        CityCountryPopulationString = CityCountry("Paris", "France", "69,000,000")
        self.assertEqual(CityCountryPopulationString, "Paris, France - population 69,000,000")
        
unittest.main()

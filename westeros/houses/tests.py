#
# Copyright 2011 Scott Turnbull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.test import TestCase

from westeros.houses.models import Realm, House

class RealmTest(TestCase):

    fixtures = ['houses',]
    def setUp(self):
        self.north = Realm.objects.get(name="The North")
        self.house = House.objects.get(name="Test House 1")

    def test_save(self):
        """
        Tests that all houses under a realm are recalculated when realms
        are updated.
        """

        # Test the base value is set correctly.
        expected = 23
        actual = self.house.wealth
        self.failUnlessEqual(expected, actual, "Wealth was expected to be %s but returned %s." % (expected, actual))

        # Set realm wealth value differently and see if it makes a difference.
        self.north.wealth = 0
        self.north.save()
        expected = 23
        actual = self.house.wealth
        self.failUnlessEqual(expected, actual, "Wealth was expected to be %s but returned %s." % (expected, actual))
        
class HouseTest(TestCase):

    fixtures = ['houses',]

    def setUp(self):
        self.north = Realm.objects.get(name="The North")
        self.south = Realm.objects.get(name="The South")
        self.house1 = House.objects.get(name="Test House 1")

    def test_calculate(self):
        """
        Tests that Calculations are preformed correctly on attributes.
        """
        attributes = ["defense", "influence", "lands", "law", "population",
                "power", "wealth",]

        # Reset all to Zero
        for attr in attributes:
            setattr(self.house1, attr, 0)
        self.house1.save()

        for attr in attributes:
            expected = 0
            actual = getattr(self.house1, attr)
            self.failUnlessEqual(expected, actual, "Expected %s but returned %s for %s!" %(expected, actual, attr))

    def test_save(self):
        # Test the base value is set correctly.
        expected = 23
        actual = self.house1.wealth
        self.failUnlessEqual(expected, actual, "Wealth was expected to be %s but returned %s." % (expected, actual))

        # Change Realm and test that recalculation went well.
        self.house1.realm = self.south
        self.house1.save()
        expected = 35
        actual = self.house1.wealth
        self.failUnlessEqual(expected, actual, "Wealth was expected to be %s but returned %s." % (expected, actual))

class BaseAttributesTest(TestCase):

    fixtures = ['houses',]

    def test_save(self):
        house = House.objects.get(name="Test House 1")
        expected = 30
        actual = house.defense
        self.failUnlessEqual(expected, actual, "Expected a defense value of %s but returned %s" % (expected, actual))

        # Change the base value and see if it makes a difference.
        house.baseattributes.defense = 100
        house.baseattributes.save()
        expected = 107
        house = House.objects.get(name="Test House 1")
        actual = house.defense
        self.failUnlessEqual(expected, actual, "Expected a defense value of %s but returned %s" % (expected, actual))
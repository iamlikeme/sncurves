import unittest, sncurves, csv, os, numpy as np


class TestSNCurves_2014_06(unittest.TestCase):
    longMessage = True
    filename = "benchmark-sncurve-2014.06.csv"
    
    def setUp(self):
        # Load benchamrk data for DNVGL-RP-C0005:2014-06
        filename = os.path.join(os.path.dirname(__file__), self.filename)
        with open(filename) as fo:
            self.data = list(csv.DictReader(fo))

        for item in self.data:
            # Convert TRUE/FALSE to booleans
            item["seawater"] = eval(item["seawater"].title())
            item["cp"] = eval(item["cp"].title())
            
            # Convert numbers
            item["sigma"] = float(item["sigma"])
            item["t"] = float(item["t"])
            item["n"] = np.float64(item["n"])


    def test_fatigue_life(self):
        sncurves.compliance("2014.06")
        for item in self.data:
            f = sncurves.get_sn_curve(item["curve"], seawater=item["seawater"], cp=item["cp"])
            expected = item["n"]
            sigma = item["sigma"]
            t = item["t"]
            
            self.assertAlmostEqual(f(sigma, t=t), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))

            if item["t"] <= 25.0:
                # For t <= 25 it should be ok to skip argument *t*
                self.assertAlmostEqual(f(sigma), expected, delta=1.0,
                    msg="\nTEST ITEM = {}\n{}".format(item, f.params))

            elif f.params.k != 0:
                # For t > 25 and k != 0 the result should be incorrect
                # if argument *t* is omitted
                self.assertNotEqual(round(f(sigma)), round(expected),
                    msg="\nTEST ITEM = {}\n{}".format(item, f.params))



class TestSNCurves_2012_10(unittest.TestCase):
    longMessage = True
    filename = "benchmark-sncurve-2012.10.csv"
    
    def setUp(self):
        # Load benchamrk data for DNV-RP-C203 October 2012
        filename = os.path.join(os.path.dirname(__file__), self.filename)
        with open(filename) as fo:
            self.data = list(csv.DictReader(fo))
        for item in self.data:
            # Convert TRUE/FALSE to booleans
            item["seawater"] = eval(item["seawater"].title())
            item["cp"] = eval(item["cp"].title())
            
            # Convert numbers
            item["sigma"] = float(item["sigma"])
            item["t"] = float(item["t"])
            item["n"] = np.float64(item["n"])


    def test_fatigue_life(self):
        sncurves.compliance("2012.10")
        for item in self.data:
            f = sncurves.get_sn_curve(item["curve"], seawater=item["seawater"], cp=item["cp"])
            expected = item["n"]
            sigma = item["sigma"]
            t = item["t"]
            
            self.assertAlmostEqual(f(sigma, t=t), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))

            if item["t"] <= 25.0:
                # For t <= 25 it should be ok to skip argument *t*
                self.assertAlmostEqual(f(sigma), expected, delta=1.0,
                    msg="\nTEST ITEM = {}\n{}".format(item, f.params))

            elif f.params.k != 0:
                # For t > 25 and k != 0 the result should be incorrect
                # if argument *t* is omitted
                self.assertNotEqual(round(f(sigma)), round(expected),
                    msg="\nTEST ITEM = {}\n{}".format(item, f.params))



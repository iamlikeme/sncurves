import unittest, sn, csv, os, numpy as np


class TestSNCurves(unittest.TestCase):
    longMessage = True

    def setUp(self):
        # Load benchamrk data for DNVGL-RP-C0005:2014-06
        filename = os.path.join(os.path.dirname(__file__), "benchmark-sncurve-2014.06.csv")
        with open(filename) as fo:
            self.data_2014_06 = list(csv.DictReader(fo))
        for item in self.data_2014_06:
            # Convert TRUE/FALSE to booleans
            item["seawater"] = eval(item["seawater"].title())
            item["cp"] = eval(item["cp"].title())
            
            # Convert numbers
            item["sigma"] = float(item["sigma"])
            item["t"] = float(item["t"])
            item["n"] = np.float64(item["n"])

        # Load benchamrk data for DNV-RP-C203 October 2012
        filename = os.path.join(os.path.dirname(__file__), "benchmark-sncurve-2012.10.csv")
        with open(filename) as fo:
            self.data_2012_10 = list(csv.DictReader(fo))
        for item in self.data_2012_10:
            # Convert TRUE/FALSE to booleans
            item["seawater"] = eval(item["seawater"].title())
            item["cp"] = eval(item["cp"].title())
            
            # Convert numbers
            item["sigma"] = float(item["sigma"])
            item["t"] = float(item["t"])
            item["n"] = np.float64(item["n"])            
            

    def test_fatigue_life_thin_2014_06(self):
        sn.compliance("2014.06")
        for item in self.data_2014_06:
            if item["t"] > 25.0:
                continue
            expected = item["n"]
            sigma = item["sigma"]
            t = item["t"]
            f = sn.get_sn_curve(item["curve"], seawater=item["seawater"], cp=item["cp"])
            self.assertAlmostEqual(f(sigma), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))
            self.assertAlmostEqual(f(sigma, t=t), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))
                

    def test_fatigue_life_thick_2014_06(self):
        sn.compliance("2014.06")
        for item in self.data_2014_06:
            if item["t"] < 25.0:
                continue
            expected = item["n"]
            sigma = item["sigma"]
            t = item["t"]
            f = sn.get_sn_curve(item["curve"], seawater=item["seawater"], cp=item["cp"])
            self.assertAlmostEqual(f(sigma, t=t), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))


    def test_fatigue_life_thin_2012_10(self):
        sn.compliance("2012.10")
        for item in self.data_2012_10:
            if item["t"] > 25.0:
                continue
            expected = item["n"]
            sigma = item["sigma"]
            t = item["t"]
            f = sn.get_sn_curve(item["curve"], seawater=item["seawater"], cp=item["cp"])
            self.assertAlmostEqual(f(sigma), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))
            self.assertAlmostEqual(f(sigma, t=t), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))
                

    def test_fatigue_life_thick_2012_10(self):
        sn.compliance("2012.10")
        for item in self.data_2012_10:
            if item["t"] < 25.0:
                continue
            expected = item["n"]
            sigma = item["sigma"]
            t = item["t"]
            f = sn.get_sn_curve(item["curve"], seawater=item["seawater"], cp=item["cp"])
            self.assertAlmostEqual(f(sigma, t=t), expected, delta=1.0,
                msg="\nTEST ITEM = {}\n{}".format(item, f.params))

from collections import namedtuple
import numpy as np

# __compliance_ is set by the function compliance() to a string
# which tells which revision of DNVGL-RP-C0005 is activated.
__compliance = None

# Define S-N curve parameters for the latest version of DNVGL-RP-C0005
# ====================================================================
SNCurves = []
__Params = namedtuple("SNcurve",
    ("name", "seawater", "cp", "N", "m1", "loga1", "m2", "loga2", "k"))

# DNVGL-RP-C0005, Table 2-1 (S-N curves in air)
SNCurves.append(__Params("B1", seawater=False, cp=False, N=1e7, m1=4.0, loga1=15.117, m2=5.0, loga2=17.146, k=0.00))
SNCurves.append(__Params("B2", seawater=False, cp=False, N=1e7, m1=4.0, loga1=14.885, m2=5.0, loga2=16.856, k=0.00))
SNCurves.append(__Params("C",  seawater=False, cp=False, N=1e7, m1=3.0, loga1=12.592, m2=5.0, loga2=16.320, k=0.05))
SNCurves.append(__Params("C1", seawater=False, cp=False, N=1e7, m1=3.0, loga1=12.449, m2=5.0, loga2=16.081, k=0.10))
SNCurves.append(__Params("C2", seawater=False, cp=False, N=1e7, m1=3.0, loga1=12.301, m2=5.0, loga2=15.835, k=0.15))
SNCurves.append(__Params("D",  seawater=False, cp=False, N=1e7, m1=3.0, loga1=12.164, m2=5.0, loga2=15.606, k=0.20))
SNCurves.append(__Params("E",  seawater=False, cp=False, N=1e7, m1=3.0, loga1=12.010, m2=5.0, loga2=15.350, k=0.20))
SNCurves.append(__Params("F",  seawater=False, cp=False, N=1e7, m1=3.0, loga1=11.855, m2=5.0, loga2=15.091, k=0.25))
SNCurves.append(__Params("F1", seawater=False, cp=False, N=1e7, m1=3.0, loga1=11.699, m2=5.0, loga2=14.832, k=0.25))
SNCurves.append(__Params("F3", seawater=False, cp=False, N=1e7, m1=3.0, loga1=11.546, m2=5.0, loga2=14.576, k=0.25))
SNCurves.append(__Params("G",  seawater=False, cp=False, N=1e7, m1=3.0, loga1=11.398, m2=5.0, loga2=14.330, k=0.25))
SNCurves.append(__Params("W1", seawater=False, cp=False, N=1e7, m1=3.0, loga1=11.261, m2=5.0, loga2=14.101, k=0.25))
SNCurves.append(__Params("W2", seawater=False, cp=False, N=1e7, m1=3.0, loga1=11.107, m2=5.0, loga2=13.845, k=0.25))
SNCurves.append(__Params("W3", seawater=False, cp=False, N=1e7, m1=3.0, loga1=10.970, m2=5.0, loga2=13.617, k=0.25))
SNCurves.append(__Params("T",  seawater=False, cp=False, N=1e7, m1=3.0, loga1=12.164, m2=5.0, loga2=15.606, k=0.25))

# DNVGL-RP-C0005, Table 2-2 (S-N curves in seawater with cathodic protection)
SNCurves.append(__Params("B1", seawater=True, cp=True, N=1e6, m1=4.0, loga1=14.917, m2=5.0, loga2=17.146, k=0.00))
SNCurves.append(__Params("B2", seawater=True, cp=True, N=1e6, m1=4.0, loga1=14.685, m2=5.0, loga2=16.856, k=0.00))
SNCurves.append(__Params("C",  seawater=True, cp=True, N=1e6, m1=3.0, loga1=12.192, m2=5.0, loga2=16.320, k=0.05))
SNCurves.append(__Params("C1", seawater=True, cp=True, N=1e6, m1=3.0, loga1=12.049, m2=5.0, loga2=16.081, k=0.10))
SNCurves.append(__Params("C2", seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.901, m2=5.0, loga2=15.835, k=0.15))
SNCurves.append(__Params("D",  seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.764, m2=5.0, loga2=15.606, k=0.20))
SNCurves.append(__Params("E",  seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.610, m2=5.0, loga2=15.350, k=0.20))
SNCurves.append(__Params("F",  seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.455, m2=5.0, loga2=15.091, k=0.25))
SNCurves.append(__Params("F1", seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.299, m2=5.0, loga2=14.832, k=0.25))
SNCurves.append(__Params("F3", seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.146, m2=5.0, loga2=14.576, k=0.25))
SNCurves.append(__Params("G",  seawater=True, cp=True, N=1e6, m1=3.0, loga1=10.998, m2=5.0, loga2=14.330, k=0.25))
SNCurves.append(__Params("W1", seawater=True, cp=True, N=1e6, m1=3.0, loga1=10.861, m2=5.0, loga2=14.101, k=0.25))
SNCurves.append(__Params("W2", seawater=True, cp=True, N=1e6, m1=3.0, loga1=10.707, m2=5.0, loga2=13.845, k=0.25))
SNCurves.append(__Params("W3", seawater=True, cp=True, N=1e6, m1=3.0, loga1=10.570, m2=5.0, loga2=13.617, k=0.25))
SNCurves.append(__Params("T",  seawater=True, cp=True, N=1e6, m1=3.0, loga1=11.764, m2=5.0, loga2=15.606, k=0.25))

# DNVGL-RP-C0005, Table 2-3 (S-N curves in seawater for free corrosion)
SNCurves.append(__Params("B1", seawater=True, cp=False, N=1e6, m1=3.0, loga1=12.436, m2=3.0, loga2=12.436, k=0.00))
SNCurves.append(__Params("B2", seawater=True, cp=False, N=1e6, m1=3.0, loga1=12.262, m2=3.0, loga2=12.262, k=0.00))
SNCurves.append(__Params("C",  seawater=True, cp=False, N=1e6, m1=3.0, loga1=12.115, m2=3.0, loga2=12.115, k=0.15))
SNCurves.append(__Params("C1", seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.972, m2=3.0, loga2=11.972, k=0.15))
SNCurves.append(__Params("C2", seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.824, m2=3.0, loga2=11.824, k=0.15))
SNCurves.append(__Params("D",  seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.687, m2=3.0, loga2=11.687, k=0.20))
SNCurves.append(__Params("E",  seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.533, m2=3.0, loga2=11.533, k=0.20))
SNCurves.append(__Params("F",  seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.378, m2=3.0, loga2=11.378, k=0.25))
SNCurves.append(__Params("F1", seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.222, m2=3.0, loga2=11.222, k=0.25))
SNCurves.append(__Params("F3", seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.068, m2=3.0, loga2=11.068, k=0.25))
SNCurves.append(__Params("G",  seawater=True, cp=False, N=1e6, m1=3.0, loga1=10.921, m2=3.0, loga2=10.921, k=0.25))
SNCurves.append(__Params("W1", seawater=True, cp=False, N=1e6, m1=3.0, loga1=10.784, m2=3.0, loga2=10.784, k=0.25))
SNCurves.append(__Params("W2", seawater=True, cp=False, N=1e6, m1=3.0, loga1=10.630, m2=3.0, loga2=10.630, k=0.25))
SNCurves.append(__Params("W3", seawater=True, cp=False, N=1e6, m1=3.0, loga1=10.493, m2=3.0, loga2=10.493, k=0.25))
SNCurves.append(__Params("T",  seawater=True, cp=False, N=1e6, m1=3.0, loga1=11.687, m2=3.0, loga2=11.687, k=0.25))

# DNVGL-RP-0005, sec. 2.4.10 (S-N curves for base material of high strength steel)
SNCurves.append(__Params("HS", seawater=False, cp=False, N=2e6, m1=4.7, loga1=17.446, m2=None, loga2=None, k=0.00))
SNCurves.append(__Params("HS", seawater=True, cp=True, N=2e6, m1=4.7, loga1=17.446, m2=4.7, loga2=17.446, k=0.00))

__SNCurves = SNCurves[:]  # Make a copy of parameters for the latest revision of DNVGL-RP-0005



def compliance(revision=None):
    """
    Select revision of DNVGL-RP-C0005 / DNV-RP-C203. Argument *revision*
    should be one of:
      *  None (default) to return the active revision
      * 'latest' for the latest revision
      * '2014.06' for DNVGL-RP-0005:2014-06
      * '2012.10' for DNV-RP-C203 October 2012

    Returns a string with the name of the active revision.
    """
    revisions = ("latest", "2014.06", "2012.10")
    global SNCurves, __compliance

    if revision is None:
        return __compliance
    elif revision not in revisions:
        raise ValueError("Revision must be one of: {}. Got: {}".format(
            ", ".join(map(repr, revisions)), revision))

    def find(name, seawater, cp):
        for i, c in enumerate(__SNCurves):
            if c.name == name and c.seawater == seawater and c.cp == cp:
                return i, c
        raise ValueError("No such S-N curve: name={}, seawater={}, cp={}".format(
            name, seawater, cp))

    def edit(sncurve, **kwargs):
        params = sncurve._asdict()
        params.update(kwargs)
        return sncurve.__class__(**params)

    if revision in ("latest", "2014.06"):
        SNCurves[:] = __SNCurves[:]
        __compliance = "DNVGL-RP-0005:2014-06"

    elif revision == "2012.10":
        SNCurves[:] = __SNCurves[:]
        i, sn = find("C", seawater=False, cp=False)
        SNCurves[i] = edit(sn, k=0.15)
        i, sn = find("C1", seawater=False, cp=False)
        SNCurves[i] = edit(sn, k=0.15)
        i, sn = find("C", seawater=True, cp=True)
        SNCurves[i] = edit(sn, k=0.15)
        i, sn = find("C1", seawater=True, cp=True)
        SNCurves[i] = edit(sn, k=0.15)
        __compliance = "DNV-RP-C203 October 2012"

    return __compliance



def get_sn_curve(name, seawater, cp):
    """
    Returns a function which implements the selected S-N curve.
    Aguments:
        name     - string, name of the S-N curve
        seawater - True for S-N curve in seawater, False for S-N curve in air
        cp       - True for S-N curve with cathodic protection, False otherwise
    """
    for c in SNCurves:
        if c.name == name and c.seawater == seawater and c.cp == cp:
            break
    else:
        raise ValueError("No such S-N curve: name={}, seawater={}, cp={}".format(
            name, seawater, cp))

    def sn(sigma, t=None, tref=25.0, scf=1.0):
        tref = float(tref)
        if t is None:
            t = tref
        else:
            t = float(max(t, tref))
        if c.name == "T" and scf > 10.0:
            k = 0.30
        else:
            k = c.k
        logS = np.log10(scf * np.array(sigma) * (t / tref) ** k)
        n1 = 10**(c.loga1 - c.m1 * logS)
        if c.m2 is None or c.loga2 is None:
            n2 = np.inf * logS
        else:
            n2 = 10**(c.loga2 - c.m2 * logS)
        return np.where(n1 <= c.N, n1, n2)
        
    sn.params = c
    sn.__doc__ = """
Calculates number of stress cycles to failure for the stress range *sigma*.
S-N curve:  {}
Compliance: {}

Arguments:
    sigma - stress range [MPa], a number or a sequence of numbers
    t     - thickness through which a crack will most likely grow [mm],
            may be omitted
    tref  - reference thickness [mm], 25.0 by default; ignored if *t*
            is not given
    scf   - stress concentration factor, 1.0 by default;
            stress range will be multiplied by *scf*, it may also affect some
            S-N curve parameters (e.g. parameter k for curve T)

Returns: a number or a numpy array with a shape corresponding to *sigma*.
    """.format(_make_description(c), compliance()).strip()
    return sn
    

def names():
    "Returns a list of valid S-N curve names"
    return sorted(set(params.name for params in SNCurves))


def _make_description(params):    
    descr = []
    if params.name == "HS":
        descr.append("HS (high strength steel)")
    else:
        descr.append(params.name)
    if params.seawater:
        descr.append("in seawater")
        if params.cp:
            descr.append("w/cathodic protection")
        else:
            descr.append("w/o cathodic protection")
    else:
        descr.append("in air")
    return " ".join(descr)


compliance(revision="latest")

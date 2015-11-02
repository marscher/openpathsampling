from openpathsampling.todict import ops_object
import openpathsampling as paths

__author__ = 'jan-hendrikprinz'

@ops_object
class ToyTopology(paths.Topology):
    '''
    Attributes
    ----------
    masses : numpy.ndarray (n_atoms, dtype=float)
        The masses associated with each atom
    '''
    def __init__(self, n_spatial, masses, pes, n_atoms = 1):
        super(ToyTopology, self).__init__(n_atoms = n_atoms, n_spatial=n_spatial)
        self.masses = masses
        self.pes = pes

    def subset(self, list_of_atoms):
        return self
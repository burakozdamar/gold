#################################################
from pymatgen import Structure
from pymatgen.core.surface import SlabGenerator

cu = Structure.from_file('Cu.cif')
slabgen = SlabGenerator(cu, (1,1,1), 50, 50)
slabs = slabgen.get_slabs()

Cu_111 = slabs[0]
print(Cu_111.cart_coords)


Cu_111.to(fmt='cif', filename='Cuuuu.cif')
exit(0)





#################################################
from pymatgen.core.surface import SlabGenerator
from pymatgen.core.structure import Structure
from pymatgen import Lattice, Structure, Molecule

Cu = Structure.from_file("Cu.cif")
slabgen = SlabGenerator(Cu, (1,1,1), 50, 10)
slabs = slabgen.get_slabs()

Cu_111 = slabs[0]

#print(vars(Cu_111))
#print(Cu_111.miller_index, Cu_111.shift)
print(Cu_111.cart_coords)

coords = [[0, 0, 0], [0.75,0.5,0.75]]
lattice = Lattice.from_parameters(a=3.84, b=3.84, c=3.84, alpha=120,
                                  beta=90, gamma=60)
struct = Structure(lattice, ["Si", "Si"], coords)
print('s',struct)

coords = [[0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 1.089000],
          [1.026719, 0.000000, -0.363000],
          [-0.513360, -0.889165, -0.363000],
          [-0.513360, 0.889165, -0.363000]]
methane = Molecule(["C", "H", "H", "H", "H"], coords)
exit(0)



#################################################


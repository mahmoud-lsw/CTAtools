from math import *
from array import *
import string
import numpy
from Plot.PlotLibrary import *
# author David Sanchez david.sanchez@lapp.in2p3.fr

from Catalog.ReadFermiCatalog import *

source = "2FGL J1015.1+4925"
#source = "1FHL J2158.8-3013"
#source = "3FGL J2158.8-3013"
Cat = FermiCatalogReader(source,"/home/sanchez/work/Catalog/","e2dnde","TeV")
#print Cat.GetDataPoints('1FHL')


print "2FGL association ",Cat.Association('3FGL')
print "3FGL Name ",Cat.Association('2FHL','3FGL_name')
print "3FGL Var Index ",Cat.GetVarIndex("3FGL")


Cat.MakeSpectrum("3FGL",2e-4,0.3)
enerbut,but,enerphi,phi = Cat.Plot("3FGL")

Cat.MakeSpectrum("2FGL",2e-4,0.3)
enerbut2FGL,but2FGL,enerphi2FGL,phi2FGL = Cat.Plot("2FGL")


Cat.MakeSpectrum("2FHL",5e-2,2)
enerbut2FHL,but2FHL,enerphi2FHL,phi2FHL = Cat.Plot("2FHL")


import matplotlib.pyplot as plt
plt.loglog()
plt.plot(enerbut, but, 'b-', enerphi,phi, 'b-',enerbut2FGL,but2FGL,'g-',enerphi2FGL,phi2FGL,'g-',
        enerbut2FHL,but2FHL,'r-',enerphi2FHL,phi2FHL,'r-')
plt.show()






import pymc as mc
import model
import pylab as pl
from pymc import Matplot

# Sample from full posterior distribution
M = mc.MCMC(model)
M.sample(iter=80000, burn=20000, thin=20, verbose=1)

fit = M.stats()
for k in sorted(fit.keys()):
    print '%10s: %s' % (k, pl.floor(fit[k]['mean']*100. + .5)/100.)

Matplot.plot(M)
pl.show()
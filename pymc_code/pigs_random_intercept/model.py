import pylab as pl
import pymc as mc

data = pl.csv2rec("data.csv")

data.id = data.id-1

##Priors

var_u = mc.Uniform('var_u', lower=0, upper=50, value=1.)
tau_u = mc.Lambda('tau_u', lambda v=var_u: v**-1, trace=False)

u = mc.Normal('u', mu=0, tau=tau_u, value=pl.zeros(48))

##Given starting values as recommended by Abie
##Could also use the Uniformative prior in PyMC to make it more like Stata
##TODO: Decide whether using the Uniformative prior is what we'd like as the default for our software
b0 = mc.Normal('b0', mu=0, tau=100**-1, value=1.)
b1 = mc.Normal('b1', mu=0, tau=100**-1, value=1.)

var_e = mc.Uniform('var_e', lower=0, upper=50, value=1.)
tau_e = mc.Lambda('tau_e', lambda e=var_e: e**-1, trace=False)

@mc.deterministic(trace=False)
def y_hat(b0=b0, b1=b1, u=u):
	return b0+b1*data.week+u[data.id]
	
@mc.stochastic(observed=True)
def y_i(value=data.weight, mu=y_hat, tau=tau_e):
	return mc.normal_like(value,mu,tau)
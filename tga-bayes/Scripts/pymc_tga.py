#!/usr/bin/env python

"""
PyMC simulation using TGA data to infer kinetic parameters for serial reaction
network
"""

import matplotlib
matplotlib.use("Agg")
import pymc as mc
import models
import sys
import data_expt as de

# get problem information from command line
matl = str(sys.argv[1])     # material ID
beta = str(sys.argv[2])     # heating rate, C/min
N_k = str(sys.argv[3])      # number of rxns

# get experimental data
data = de.read_data( matl, beta )

# Generate model
vars = models.tga_w( data, beta, N_k )

## Fit model with MAP estimates
#map = mc.MAP(vars)
#map.fit(method='fmin_ncg', verbose=2)

# Import model variables and set database options
m = mc.MCMC(vars,
            db='sqlite',
            dbname='../Results/' + matl + '_' + beta + 'Cpm_' + N_k + 'rxn.sqlite')

# Use adaptive Metropolis-Hastings step method
m.use_step_method(mc.AdaptiveMetropolis, [m.theta])

# Configure and run MCMC simulation
#m.sample(iter=20000000, burn=10000000, thin=1000, verbose=1)
# m.sample(iter=400000000, burn=200000000, thin=10000, verbose=1)
m.sample(iter=1000, burn=500, thin=5, verbose=1)

## Plot resulting distributions and convergence diagnostics
#mc.Matplot.plot(m,
#                format='pdf',
#                path='../Results/example_tga',
#                common_scale=False)

# Display results
m.theta.summary()

# Plot summary results


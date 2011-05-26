insheet using pigs.csv, clear

capture log close
log using pigs_log.txt, text replace

**Random intercept model
**Variances for random effects
**REML
xtmixed weight week || id: , var 

**Random intercept and slope model model
**Random effects uncorrleated
**Variances for random effects
**REML
xtmixed weight week || id:week , var 

**Random intercept and slope model model
**Random effects corrleated
**Variances for random effects
**REML
xtmixed weight week || id:week , var cov(un)


log close

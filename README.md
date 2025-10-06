# integrators2

Starter code and examples for MC integration exercise.

See also:

  * https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.Sobol.html
  * https://root.cern.ch/doc/master/quasirandom_8C_source.html


SUBMISSION DETAILS:
  ndsphere.py takes command line arguments, outputs volume, uncertainty, rel error
  
  mc-convergence.py generates convergence.png. Originally used theoretical uncertainty for error bars, but made the graph unreadable. Now uses variance calculatewd from 20 runs of mc integration over the sphere to generate error bars. (The directions said use method 1 from the notes for error bars, but I couldn't find any notes that mentioned anything like that)

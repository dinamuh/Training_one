from main import no_space
from main import no_space2

def test(benchmark):
    assert benchmark(no_space, 'jfBm  gk lf8hg  88lbe8 ') == 'jfBmgklf8hg88lbe8'


def test2(benchmark):
    assert benchmark(no_space2, 'jfBm  gk lf8hg  88lbe8 ') == 'jfBmgklf8hg88lbe8'


'''''''''
----------------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------------
Name (time in ns)          Min                    Max                Mean              StdDev              Median                IQR              Outliers  OPS (Mops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 307.8125 (1.0)       3,025.3125 (1.0)      350.2082 (1.0)      107.5964 (1.0)      320.5625 (1.0)      20.5000 (1.71)     8998;20862        2.8554 (1.0)      193275          16
test                  314.2500 (1.02)     18,054.2500 (5.97)     358.4987 (1.02)     125.4441 (1.17)     323.9000 (1.01)     12.0000 (1.0)      8430;24534        2.7894 (0.98)     148788          20
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 4.82 seconds ==========================
'''''''''''''''''
from main import reverse_list
from main import reverse_list2

def test(benchmark):
    assert benchmark(reverse_list,[1,2,3,4])== [4,3,2,1]



def test2(benchmark):
    assert benchmark(reverse_list2,[1,2,3,4])== [4,3,2,1]


'''''''''
---------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
Name (time in ns)          Min                   Max                Mean             StdDev              Median                IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 168.6100 (1.0)      1,034.9700 (1.0)      203.2104 (1.08)     62.3521 (1.19)     178.8200 (1.0)      25.4600 (4.71)     5145;7717        4.9210 (0.93)      57478         100
test                  174.7000 (1.04)     1,327.5000 (1.28)     188.2546 (1.0)      52.3671 (1.0)      179.6000 (1.00)      5.4000 (1.0)     4169;12712        5.3120 (1.0)      162496          20
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 3.89 seconds ======================
'''''''''''
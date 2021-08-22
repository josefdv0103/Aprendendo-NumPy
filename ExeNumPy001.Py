import numpy as np
#|1 1 1 1 1|
#|1 0 0 0 1|
#|1 0 9 0 1|
#|1 0 0 0 1|
#|1 1 1 1 1|
a = np.full([5,5], 1)
print(a)
a[1:4, 1:4] = 0 #ou a[1:-1, 1:-1] = 0
print(a)
a[2,2] = 9
print(a)
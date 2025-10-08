# Author: Manas Sharma
# Website: www.bragitoff.com
# Email: manassharma07@live.com
# License: MIT
# Value of Pi using Monte carlo
import sys
sys.set_int_max_str_digits(0)
import numpy as np
from matplotlib import pyplot as plt
 
for k in range (100):
    # Input parameters
    nTrials = int(1230)
    radius = 1
    #-------------
    # Counter for thepoints inside the circle
    nInside = 0
     
    # Generate points in a square of side 2 units, from -1 to 1.
    XrandCoords = np.random.default_rng().uniform(0, 1, (nTrials,))
    YrandCoords = np.random.default_rng().uniform(0, 1, (nTrials,))
     
    for i in range(nTrials):
        x = XrandCoords[i]
        y = YrandCoords[i]
        # Check if the points are inside the circle or not
        if x**2+y**2<=radius**2:
            nInside = nInside + 1
                 
         
    area = 4* float(nInside)/float(nTrials)
    print("Value of Pi: {:.6f}".format(area))
    

figure, axes = plt.subplots()
Drawing_colored_circle = plt.Circle(( 0 , 0 ), 1, fill=False )
axes.scatter(XrandCoords, YrandCoords)
axes.set_aspect( 1 )
axes.add_artist( Drawing_colored_circle )
plt.title( 'Colored Circle' )
plt.show()
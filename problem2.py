# add the boxes as specified in the problem definition as a list of each parameter
O = [2,5,1,10,7] # offset from 0
W = [10,8,12,10,9] # width
H = [5,7,4,8,6] # height

X = [0,0,0,0,0] # will store X coordinates of the center of each box
Y = [0,0,0,0,0] # will store Y coordinates of the center of each box
A = [0,0,0,0,0] # will store the areas

# the X coordinate is the offset + the half width
X[0] = O[0]+W[0]/2
X[1] = O[1]+W[1]/2
X[2] = O[2]+W[2]/2
X[3] = O[3]+W[3]/2
X[4] = O[4]+W[4]/2

# the Y coordinate is the previous boxes y coordinate + it's half width + this box's half width
# Note that I did this so that my solution wasn't ragged and was easier to verify
# Most people did this by adding all previous heights
Y[0] = 0    + 0      + H[0]/2
Y[1] = Y[0] + H[0]/2 + H[1]/2
Y[2] = Y[1] + H[1]/2 + H[2]/2
Y[3] = Y[2] + H[2]/2 + H[3]/2
Y[4] = Y[3] + H[3]/2 + H[4]/2

# Now calculate areas
A[0] = H[0]*W[0]
A[1] = H[1]*W[1]
A[2] = H[2]*W[2]
A[3] = H[3]*W[3]
A[4] = H[4]*W[4]

# Finally, calculate the centroid
TotalArea = A[0]+A[1]+A[2]+A[3]+A[4]

Centroid_X = (X[0]*A[0]+X[1]*A[1]+X[2]*A[2]+X[3]*A[3]+X[4]*A[4])/TotalArea
Centroid_Y = (Y[0]*A[0]+Y[1]*A[1]+Y[2]*A[2]+Y[3]*A[3]+Y[4]*A[4])/TotalArea

print(f"Centroid = ({Centroid_X},{Centroid_Y})")

# Fun extra, determine stability
# For the stack to be stable, every substack must be stable, which means the x centroid of the stack above it lies within its x bounds

# For Box 3
TotalArea = A[4]
Centroid_X = (X[4]*A[4])/TotalArea
Stable3 = abs(Centroid_X - X[3]) <= W[3]/2
# For Box 2
TotalArea = A[3]+A[4]
Centroid_X = (X[3]*A[3]+X[4]*A[4])/TotalArea
Stable2 = abs(Centroid_X - X[2]) <= W[2]/2
# For Box 1
TotalArea = A[2]+A[3]+A[4]
Centroid_X = (X[2]*A[2]+X[3]*A[3]+X[4]*A[4])/TotalArea
Stable1 = abs(Centroid_X - X[1]) <= W[1]/2
# For Box 0
TotalArea = A[1]+A[2]+A[3]+A[4]
Centroid_X = (X[1]*A[1]+X[2]*A[2]+X[3]*A[3]+X[4]*A[4])/TotalArea
Stable0 = abs(Centroid_X - X[0]) <= W[0]/2

print("Stability of each of the 4 substacks: ",Stable0, Stable1, Stable2, Stable3)
print("The whole stack is ", "stable" if (Stable0 and Stable1 and Stable2 and Stable3) else "not stable")
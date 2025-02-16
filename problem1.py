# define the points of the polygon, clockwise
X = 145,234,430,378,349,279,217
Y = 184,111,130,340,208,364,273

#calculate the perimeter
L1 = ((X[1]-X[0])**2 + (Y[1]-Y[0])**2)**0.5
L2 = ((X[2]-X[1])**2 + (Y[2]-Y[1])**2)**0.5
L3 = ((X[3]-X[2])**2 + (Y[3]-Y[2])**2)**0.5
L4 = ((X[4]-X[3])**2 + (Y[4]-Y[3])**2)**0.5
L5 = ((X[5]-X[4])**2 + (Y[5]-Y[4])**2)**0.5
L6 = ((X[6]-X[5])**2 + (Y[6]-Y[5])**2)**0.5
L7 = ((X[0]-X[6])**2 + (Y[0]-Y[6])**2)**0.5

Perimeter = L1 + L2 + L3 + L4 + L5 + L6 + L7
print(f"Perimeter = {Perimeter}")

#calculate the area (using the shoelace formula)
Pass1 = X[0]*Y[1]+X[1]*Y[2]+X[2]*Y[3]+X[3]*Y[4]+X[4]*Y[5]+X[5]*Y[6]+X[6]*Y[0]
Pass2 = Y[0]*X[1]+Y[1]*X[2]+Y[2]*X[3]+Y[3]*X[4]+Y[4]*X[5]+Y[5]*X[6]+Y[6]*X[0]
Area = abs(Pass1-Pass2)/2
print(f"Area = {Area}")
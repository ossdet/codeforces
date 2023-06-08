#watch !!! : the number ofintersection will be 0 or 1 or infinte

def numb_intersection(a1,b1,c1,a2,b2,c2):
    det=a1*b2 -a2*b1
     # Calculate the determinant
    det = a1 * b2 - a2 * b1
    
    # Check if the lines are parallel (det = 0)
    if det == 0:
        # Check if the lines are coincident
        if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            return -1  # Sets are coincident
        else:
            return 0  # No intersection, lines are parallel
    
    return 1  # Intersection exists
#read the two sets 
a1,b1,c1=map(int,input().split())
a2,b2,c3=map(int,input().split())

numb_intersection(a1,b1,c1,a2,b2,c2)
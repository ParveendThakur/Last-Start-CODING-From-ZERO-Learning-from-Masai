def compare_rectangles(l1, b1, l2, b2):
    
    
    perimeter = 2*(l1+b1+l2+b2)
    perimeter1 = 2*(l1+b1+l2+b2)
    
    area = (l1+l2)*(b1+b2)
    area1 = (l1+l2)*(b1+b2)
    
    
    if area>area1:
        print ("true")
    else :
        print ("false")
        
    if perimeter>perimeter1:
        print ("true")
    else :
        print ("false")
 
 

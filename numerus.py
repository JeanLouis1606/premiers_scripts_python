def numerus(roman): 
     ...:     nombre = 0 
     ...:     i=0 
     ...:     while i < len(roman): 
     ...:         if i < (len(roman)-1) and to_val(roman[i+1]) <= to_val(roman[i]): 
     ...:             nombre += to_val(roman[i]) 
     ...:             i+=1 
     ...:         elif i < (len(roman)-1): 
     ...:              nombre += to_val(roman[i+1]) - to_val(roman[i]) 
     ...:              i+=2 
     ...:    # nombre += to_val(roman[i])  
     ...:     return nombre 

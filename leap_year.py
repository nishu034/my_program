def is_leap(year):
    leap = False
    
    if year==0:
        leap=False
    elif year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
            
    return False
    
    return leap

year = int(input())
print(is_leap(year))

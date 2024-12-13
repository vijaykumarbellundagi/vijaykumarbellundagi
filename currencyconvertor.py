def converter (amt, unit="USD : "):
    if(unit=="RS"):
        total=float(amt)/83
        return total
    
    elif(unit=="EUR"):
        total=float(amt)*1.05
        return total
    
    elif(unit=="DHR"):
        total=float(amt)*2.65
        return total
    else:
        return amt+unit

print(converter("150","DHR"))
      
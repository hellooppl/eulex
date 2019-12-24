def array_diff(a, b):
    for i in range(len(b)):
        try:
            print("b is" , b[i])
            while b[i] in a:
                a.remove(b[i])
        
        except:
            pass
    return a

def counting_valley(n,steps):
    seaLevel= 0
    v = False
    counter = 0
    for i in range(n):
        
       step = steps[i]
       if seaLevel== 0 and step == "D":
           v = True
       elif seaLevel== 0 and step == "U":
            v = False
       
       if step == "U":
           seaLevel+= 1
       elif step == "D":
           seaLevel-= 1
       
       if i != 0 and seaLevel== 0 and v:
            counter += 1
      
       
    return counter

n = 6
steps = "UDUDUDU"
print(counting_valley(n,steps))
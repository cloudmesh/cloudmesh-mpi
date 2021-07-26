
ns = [1,2,3,4]      # range(1,5)
counts = [1000, 10000, 10000]  # range(10000, 100000, 10000) 

for n in ns:
  for count in counts:
    command =  f"mpieec -n {n} python ring.py --count {count}"
    os.system(command)
    
# ring ....

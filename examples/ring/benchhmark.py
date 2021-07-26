
ns = [1,2,3,4]      # range(1,5)
counts = [1000, 10000, 10000]  # range(10000, 100000, 10000) 

for n in ns:
  for count in counts:
    command =  f"mpieec -n {n} python ring.py --count {count}"
    os.system(command)
    
#csv,ring 4 10000 ....


####
#
# $ python benchmark.py | fgrep "#csv,ring" > ring-benchmark.csv
# analyze,ipynb .py ring-benchmark.csv
# read in the csv and than produce the plot
#

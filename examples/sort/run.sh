#! /bin/bash -x

#python multiprocessing_mergesort.py p s c| fgrep "# csv" | tee output.log

#p = "[1,2,3,4,5,6,7,8,9,10,11"] # processors
#s = "[1000]" # size of total
#c = 10 # repeat of the same experiment with the same p and s

pip install -r requirements.txt

#./experiment.py --processes="[1-p]" --size="[100]" --repeat=10 | fgrep "# csv" | tee output.log
./experiment.py --processes="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]" --size="[100]" --repeat=10 | tee output.log
#| fgrep "# csv" | tee output.log

#python graph_efficiency.py
#python graph_speedup.py
#python graph_proc.py


#python multiprocessing_mergesort.py "[8]" "[100,1000,10000]" 10 | fgrep "# csv" | tee output-num.log

#python graph_size.py



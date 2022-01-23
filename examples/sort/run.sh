#python multiprocessing_mergesort.py p s c| fgrep "# csv" | tee output.log

#p = "[1,2,3,4,5,6,7,8,9,10,11"] # processors
#s = "[1000]" # size of total
#c = 10 # repeat of the same experiment with the same p and s
set +x

pip install -r requirements.txt

python multiprocessing_mergesort.py "[1,4,8,16]" "[10000]" 10 | fgrep "# csv" | tee output-speedup.log

python graph_efficiency.py
python graph_speedup.py
python graph_proc.py


python multiprocessing_mergesort.py "[8]" "[100,1000,10000]" 10 | fgrep "# csv" | tee output-num.log

python graph_size.py



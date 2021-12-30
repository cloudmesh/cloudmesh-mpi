# Notes

## Simple use of git

0. download
   - do once

   ```bash
   mkdir cm
   cd cm
   git clone git@github.com:cloudmesh/cloudmesh-mpi.git
   ```
   
1. update

   ```bash
   git pull
   ```
   
2. local upload
    

   1. to add file, do once

      ```bash
      git add filename
      ```
   
   2. once changed file, do

      ```bash
      git commit -m "this is my comment" filename
      ```
	
   3. remote upload

      ```bash
      git push
      ```
	
3. verify

   go to the web page and look att the file you modified

4. install

   - do once

   - create virtual anvironment

   ```bash
   pip install pip -U
   pip install -r requirements.txt
   ```

Never modify anythin in docs, Only Gregor does this!!!

## List of sort algorithms in python

* [array.sort](https://docs.python.org/3/howto/sorting.html)
*
[numpy.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)

## Other sort algorithms

* [Countung Sort](https://en.wikipedia.org/wiki/Counting_sort)
* [Adaptive merge sort](https://www.tutorialspoint.com/adaptive-merging-and-sorting-in-data-structure)
* [Adaptive sort](https://en.wikipedia.org/wiki/Adaptive_sort)

## Speeding up the sequential algorithms

```python
from numba import jit

@jit
def sort_alg(a)
	# do sorting of a
	return a
```


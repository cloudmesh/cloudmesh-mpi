# Parameters

```
$ export N=10
$ echo $N
$ python -i
>>> import os
>>> os.environ["N"]
>>> exit()
$ python a.py
$ sh run.sh
$ sh run.sh | fgrep "csv,processors"
$ python b.py
$ python b.py --n=3
```

- [ ] Document the .py files in the parameters folder in examples
- [ ] Document click module
- [ ] Add parameter passing section
- [ ] you can do !include which should be in the mpi documentation to refer to

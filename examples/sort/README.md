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
    to add file, do once

   ```bash
   git add filename
   ```
   
2a. once changed file, do

    ```bash
    git commit -m "this is my comment" filename
    ```
	
2b. remote upload

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


# TAS/XMS project code


Grammar
* TODO: convert past tense 

---

## Design


* TODO: drawing of architecture on how the components relate

### The stuff that fugang already did

### Docker

* TODO: docker image for everything ...
---



## Install

* TODO: draing of where sis what installed
* TODO: How can one replicate the portal
* TODO: can we use echo or HPC for analysis (db too big for other
  machine? ...)
* TODO: Gregor needs cfg file (backup and full access)

A. Configure infrastructure
   * Mongo ...
   * Elastic search ...

B. Configure program and services
   * Web server
   * Interface to XSEDE
   * Our own analysis
   * WHat happens when our machine at MESH go down

### Requirments

* TODO: requirements hardware software

* Fast Memory needed
* Fast IO needed to disks
* Creating of elastic search Index (when run on 16GB it is too slow), 
  will run over 2 weeks for the analysis
* When run on Echo (It has 384GB), it will run for a week

Once the data is indexed the analysis is done in a few hours

Verify the hardware requirements (shoudl we ask for funding for hardware ... better would be if we can showcase reuse of existsing NSF hardware?)



A. Echo: create for semantic scholar 
   Run with semantic scholar from snapshot mm/dd/yyyy 
   find all values and fill out here
   1. download from semantic scholar (200GB)
   2. unzip (400GB)
   3. load data into mongo db (takes a ? days) 
      (~50GB, as we clean up a bit)
   5. set up elastic search
   6. use mongo connnector to sycn data from mongo to 
      elastic search. This will create the index for the data 
      (This takes 1-2 weeks to finish)
      (~100GB)
   7. The analysis can then be done with
       6.1 Using API to access the elasticsearch index
       6.2 Python/pymongo to query the mongo database
       6.3 Analysis based on the mongo data and elasticsearch data
       
TODO: document precisely the process that is done in A so its easy to do
* Can this be automated in some form with a script?
* Can this be done with containers, while the DBs are on the system? 

* Can A be done on an HPC machine with even bigger memory? However running this for x week is complex
* How do we back up search index, or this setup so we can quickly reload it and reuse for others (e.g. we want to develop a service that does the analysis automatically on a set of refernces ...)
* How much memory can the dell machine maximum

* CLAIM ECHO SINGLE NODE FOR ScientificImpact 
* Echo 24 cores, xeon???, RAM 384GB (2 processors?)
* vs PC in office

What is the data size for each of the component 
    we need about 

### Databases

* TODO: data base update
  * fastlane
    (nsf awards search from Gallo, IT s a CD that we got 
    and used, we used that from 2012 - 2013, 
    now we use ??, awardid -> publication, 
    we search find award id, published on yearly basis in text(?) file,
    as we have than full award id we can then query the publications)
  * ms (we have had only older daya, for nw once policy is 
    restriced (how?) so we went with semantic scholar, previously MS
    published the raw data now MS provides a service via API service, but
    the service is rate limited, thus it can be only used for smaller 
    projects and not an exhaustive serch as we do, is there a different
    way to get more ?)
  * isi (queries to isi all xsede refernces to get 
    new citation data, isis data is not stored locally)
  * integration with XSEDE
    We have read access to XSEDE central database. How do we do this 
    (help ticket to XSEDE and the right person will response, 
    ip whitelisted, done via XSEDE user name for Fugang. It is postgress
    sql, where are scripts to retrieve data once we have access? 
    IT is included in this document .... )
    in detail, we do a monthly update ...
  * google (we used to have code)
    Upload this to github in `deprecated-google` folder.
    We may need this for comparision in paper
 
* TODO: database(s) replication

* TODO: Document the indexing strategy
  * title
  * field of science
  * journal name 

### Code 

* TODO: code is missing docstrings and explanation wher ethings are used 

---

## Management

* TODO: How is interface to XSEDE organized, e.g. contact, what needs   to be done, who in xsede uses us
* TODO: what about the mongo vs sql stuff ...
* Setup Mongo
* Setup SQL

### Backup

See later, needs to be moved here.

### Database Update

### Query and Analysis

* TODO: explanation how can one replicate the analysis
    * Grant access to the databases via remote access
    * HOw do we avoid exploits
    * we can use python easily to do that and program this via 
      python/ jupyter notebook, queries can be 
        * 1 minute duration: select everything form the database 
          wherethe source is ISI
* TODO: manual is missing to do analysis of organization X
    * bibliography: input: bibtex? csv? text file?
        * parse file to get
            * doi
            * title
            * year
            * no authors
            * query that into isi
        * semi automated
        * example ncar - if doi use doi verify publication, 
          if not use title
* TODO: manual on how to convert bib to needed format for us is missing
    * do we have ncar_data -> converter -> our own format of doi, 
      title, year
    * input data is diret, we have customized parser but fugang 
      has hard toime describing it formally, go over code to see if 
      we can formalize
    * we need database, that realy defines the data ... 
* TODO: jupyter notebook to do analysis
* TODO: multiple analysis at the same time
    * as we use database we can do this in jupyter 

* TODO: we need description of database and example query, but better is some API in python.
* TODO: DO we query n Mongo query SQL query or booth


### Reports

* TODO: what is `XSEDE2_SIM_RY2.pdf` (different name):
* ***A***: Most reports are quarterly or yearly while considering the start point as early as TAS/XMS.
* TODO:  add a list of all reports to the README in report.md so we have
  inventry of reports (maybe table)
* TODO: Presise steps fo doing the monthly report is missing
* TODO: how are graphs created in general, for report

   
---

## Paper

* PEARC2021 (has been moved to education and does not rely fin in there, write to conference cahirs that note must be distributed that this has been added to education as it is unique and no other category seems to 100% fit, but it is importnat new work
* Write big paper that leverages from PEARC and make sit a journal submission, possibly plosone (https://journals.plos.org/plosone/)
* Write yet another paper with Architecture from old proposal (SCISIP) maybe to workshop.

--- 

## Proposal

### Work done by others

### Why we need to continue work?

### Why do we need separate funding stream?

### What would we do in addition (e.g. 1 FTE)

* MRI
* Departments
* Fastlane (of large projects)
* Grow to other fields (non XSEDE)
* NIH will not be covered here (we write scisip proposal for September) THis will get 0.5 - 1FTE if funded, possibly more, we need also 0.x FTE BIO expert ... as this tragets biology. IS there a group already doing this fro NIH

### Run your own metrics via container

* needs dockerfile and open source code, no closed source images, 
* images created locally not from dockerhub
* needs review before it can be run? maybe not good for proposal

### What is funding level 

* 1 Full time staff (Fugang) ? (105 no overhead)
* 20% Gregor?
* Need to work with Gary on budget

Proposal:

* TODO: what implications has this for proposal
* TODO: paper: Top X departments
* TODO: big paper

------





This repo stores the relevant project code for TAS/XMS project. The
subdirectories have code for different purposes/deployments.

 - **xsede_metrics**: Code for management and update of XSEDE
   publications, citations, and metrics data. It connects to various
   resources (web site, APIs, XSEDE central database) to retrieve and
   update bibliometrics data and store the derived data to a local
   mashup database. The database is in mySQL and is running in an SSD
   drive. The data dump is backed up in separate HDD disk on the same
   machine.
   
 - **sciimp_xdmod**: The scientific impact portal deployed as part of
   the XDMOD portal. It connects to the mashup database from the
   previous step, where the scientific impact facts tables are in.
   
 - **xup_restapi**: The RESTful API deployed at tas.futuregrid.org
   being used by XSEDE User Portal as part of the publication
   discovery service. This service connects to a duplicate of the
   mashup db on the same machine. The service was using only the
   historical data (publications parsed from the older TeraGrid/XSEDE
   report to NSF) so no update to this db is needed.

- **reports**: This folder stores the past reports submitted as part
  of the XSEDE quarterly report to NSF, or some customized reports as
  requested by the XSEDE management team. See [reports](reports)
  
   - TODO: add time frame when we started Sep 2016? Was it not earlier? 

The tas.cfg file has the configs to connect to the various databases
and resources. Also to connect to the XDcDB the accessing IP has to be
whitelisted.

    * TODO: Gregor needs that file. 
        most important is, [XDMOD] [TASDB]
        we do not use [MENDELAY]

## Reports

https://github.com/scienceimpact/report/blob/main/

* Scientific Impact Metrics for XSEDE2 at Report Year 2 (between Jan 1, 2017 - Apr 30, 2018)
  [docx](https://github.com/scienceimpact/report/blob/main/XSEDE2_SIM_RY2.docx?raw=true)
  [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE2_SIM_RY2.pdf)

* 2016
  * Apr 1, 2016 - Jun 30, 2016 
    [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q2.docx?raw=true)
    [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q2.pdf )
  * July 1, 2016 - Sept 30, 2016 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q3.docx?raw=true)
   [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q3.pdf)
  * Oct 1, 2016 - Dec 31, 2016 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q4.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q4.pdf)


* 2017 Yearly report 1(July 1, 2016 - Jun 30, 2017) 
  [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q2Yearly.docx?raw=true) 
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q2Yearly.pdf )

  * Jan 1, 2017 - Mar 31, 2017 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q1.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q1.pdf)
  * Apr 1, 2017 - Jun 30, 2017 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q2.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q2.pdf)
  * July 1, 2017 - Sept 30, 2017 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q3.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q3.pdf)
  * Oct 1, 2017 - Dec 31, 2017 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q4.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2017Q4.pdf)

* 2018 Yearly report between Apr 1, 2017 to Mar 31, 2018 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_03Yearly.docx?raw=true) 
  [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_03Yearly.pdf)
  * Comment: reporting periods have changed
  * Jan 1, 2018 - Mar 31, 2018  [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_03Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_03Yearly.pdf)
 (same as yearly report)
  * Apr 1, 2018 - July 31, 2018 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_07.docx?raw=true)
  [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_07.pdf)
  * Aug 1, 2018 - Oct 31, 2018 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_10.docx?raw=true)
 [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2018_10.pdf)

* 2019 Yearly report between May 1, 2018 to Apr 30, 2019
[docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_04Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_04Yearly.pdf)
  * Nov 1, 2018 - Jan 31, 2019 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_01.docx?raw=true)
  [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_01.pdf)
  * Feb 1, 2019 - Apr 30, 2019
[docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_04Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_04Yearly.pdf) (same as yearly report)
  * May 1, 2019 - July 31, 2019 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_07.docx?raw=true)
  [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_07.pdf)
  * Aug 1, 2019 - Oct 31, 2019 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_10.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2019_10.pdf)


* 2020 Yearly report between May 1, 2019 - Apr 30, 2020
  [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_04Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_04Yearly.pdf)
  * Nov 1, 2019 - Jan 31, 2020 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_01.docx?raw=true) [pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_01.pdf)
  * Feb 1, 2020 - Apr 30, 2020 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_04Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_04Yearly.pdf)
 (same as yearly report)
  * May 1, 2020 - July 31, 2020 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_07.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_07.pdf)
  * Aug 1, 2020 - Oct 31, 2020 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_10.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2020_10.pdf)

* 2021 Yearly report between May 1, 2020 to Apr 30, 2021 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2021_04Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2021_04Yearly.pdf)
  *  Nov 1, 2020 - Jan 31, 2021 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2021_01.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2021_01.pdf)
  * Feb 1, 2021 - Apr 30, 2021 [docx](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2021_04Yearly.docx?raw=true)
[pdf](https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2021_04Yearly.pdf)(same as yearly report)
  * May 1, 2020 - July 31, 2021 (Planed, due  in early August)

Project completion 
  * Integrates all reports in a single document
  * Apr 1, 2016 - July 31, 2021 

Other Reports
    
  * Fugang Wang, Gregor von Laszewski, Peers Comparison of publications for TG/XD, NCAR, and BlueWaters, Nov 2016, Technical Report, Indiana University, URL: https://github.com/scienceimpact/report/blob/main/presentation/TAS_PeerComparison_Dec2014.pptx

  * Fugang Wang, Gregor von Laszewski, Bluewaters Scientific Impact Analysis, July 2016, Technical Report, Indiana University, URL: https://github.com/scienceimpact/report/blob/main/BW_ScientificImpact.docx

  * Fugang Wang, Gregor von Laszewski, Peers Comparison of publications for TG/XD, Then and Now, Jan 2017, Technical Report, Indiana University, URL: https://github.com/scienceimpact/report/blob/main/XD_Peers_Summary.docx

  * Fugang Wang, Gregor von Laszewski, Scientific Impact Metrics Measuring and Tracking for Anton Project, July 2020, Technical Report, Indiana University, URL: https://github.com/scienceimpact/report/blob/main/Anton_2020_07.docx



Papers

  * Fugang Wang, Gregor von Laszewski, Timothy Whitson, Geoffrey C. Fox, Thomas R. Furlani, Robert L. DeLeon, and Steven M. Gallo. 2018. Evaluating the Scientific Impact of XSEDE. In Proceedings of the Practice and Experience on Advanced Research Computing (PEARC '18). Association for Computing Machinery, New York, NY, USA, Article 10, 1–8. DOI: https://doi.org/10.1145/3219104.3219124

  * von Laszewski, Gregor, Fugang Wang, Geoffrey C. Fox, David L. Hart, Thomas R. Furlani, Robert L. DeLeon, and Steven M. Gallo. "Peer Comparison of XSEDE and NCAR Publication Data," 2015 IEEE International Conference on Cluster Computing, 2015, pp. 531-532, doi: 10.1109/CLUSTER.2015.98.

  * Fugang Wang, Gregor von Laszewski, Geoffrey C. Fox, Thomas R. Furlani, Robert L. DeLeon, and Steven M. Gallo. 2014. Towards a Scientific Impact Measuring Framework for Large Computing Facilities - a Case Study on XSEDE. In Proceedings of the 2014 Annual Conference on Extreme Science and Engineering Discovery Environment (XSEDE '14). Association for Computing Machinery, New York, NY, USA, Article 25, 1–8. DOI: https://doi.org/10.1145/2616498.2616507

  * Comprehensive Evaluation of XSEDE’s Scientific Impact using SemanticScholar Data. submitted to 
PEARC'21 (https://www.overleaf.com/project/60755de8a80d14aa9b0619b5)
 
Presentations and Posters

  * Fugang Wang, Gregor von Laszewski, Introduction of the proposed Peers Comparison Method, Dec 22 2014, Presentation, Indiana University, URL: https://github.com/scienceimpact/report/blob/main/presentation/TAS_PeerComparison_Dec2014.pptx
  * Fugang Wang, Gregor von Laszewski, Peer Comparison of XSEDE and NCAR Publication Data, IEEE Cluster 2015, Poster, URL: https://github.com/scienceimpact/report/blob/main/poster/TAS_Poster_IEEECluster15.pdf
  * Fugang Wang, Gregor von Laszewski, Peer Comparison of XSEDE Publication Data, XSEDE 2015, Poster, URL: https://github.com/scienceimpact/report/blob/main/poster/TAS_Poster_XSEDE15.pdf
  * Fugang Wang, Gregor von Laszewski, XMS Scientific Impact, July 2017, Presentation, PEARC'17 XMS Advisory Committee meeting, URL: https://github.com/scienceimpact/report/blob/main/presentation/PEARC17_XMS_sciimp.pptx
  * Fugang Wang, Gregor von Laszewski, Timothy Whitson, Geoffrey Fox, Thomas Furlani, Robert Deleon, Steven Gallo, Scientific Impact Evaluation of XSEDE, July 2018, Paper Presentation, PEARC'18, URL: https://github.com/scienceimpact/report/blob/main/presentation/XMS_Sciimp_PEARC18.pptx
  * Fugang Wang, Gregor von Laszewski, Scientific Impact Evaluation for XMS, Jun 19, 2018, Presentation, XMS NSF Site Visit Meeting, URL: https://github.com/scienceimpact/report/blob/main/presentation/XMS_NSF_June2018_FinalDraft.pptx
  * Fugang Wang, Gregor von Laszewski, Scientific Impact Metrics Update, July 2020, Presentation, XMS Advisory Committee Meeting, URL: https://github.com/scienceimpact/report/blob/main/presentation/XMS_Sciimp_AC2020.pptx
  * Fugang Wang, Gregor von Laszewski, Scientific Impact Metrics Update, July 2020, Presentation, User Advisory Board Meeting, URL: https://github.com/scienceimpact/report/blob/main/presentation/XMS_Sciimp_UAB2020.pptx

Technical Report References

* Fugang Wang, Gregor von Laszewski, XSEDE Scientific Impact Metrics: Apr 1, 2016 - Jun 30, 2016, Jun 30 2016, Report, Indiana University, URL: https://github.com/scienceimpact/report/blob/main/XSEDE_SIM_2016Q2.pdf

## Mashup database management

The essential part and a major contribution of this project is the
mashup database we created which contains publication and citation
data, among others, and the generated scientific impact metrics
related to XSEDE. The backend scripts add and update data to the
mashup database, while the web portal and the RESTful services are all
connecting to the database to present the impact metrics.

### Current database setup

The essential data related to XSEDE were managed in a MySQL database
(version 5.7.33). The database was deployed at: ```
dg1.sice.indiana.edu ``` The machine is equipped with an SSD drive and
the database is served from there.

The main update would be done on this database. The sciimp portal
@XDMOD is connecting to this database to get the latest impact metrics
data to present in the portal.  A replica of this database was also in
tas.futuregrid.org, where the RESTful service used by the XSEDE user
portal is deployed. As that service is using historical data that does
not require update any more, the database on that server won't need
monthly update.

### Data management

We are updating the main database at least monthly, with additions and
updates of XSEDE related publications and their citation data. The
backend scripts are helping doing this (see next section for the
update workflow). The update is usually done on the last day of each
month.

### Data backup

After each monthly update we run mysqldump to dump the related
databases to files. E.g.,

```
mysqldump -u root -p --all-databases > /data/mashupdb_01312021.sql
```

This dumps all the data to a single file.

The dump file is named with a timestamp in the form of
*\*_ddmmyyyy.sql*. Since the update process from the scripts already
created snapshot of the historical data, i.e., the data backup is
incremental, so it's no need to keep all the versions but the one
latest would be sufficient.

The dump file is then stored in a backup folder on the same machine
(but a separate physical HDD), and also on another machine.

### Data restoration/recovery

To recover the data or restore into another machine. Makue sure to
setup MySQL server first and then restore from the database dump file.

#### Setup MySQL on a Ubuntu server

To setup MySQL server on Ubuntu, follow these simple steps
```
sudo apt update
sudo apt install mysql-server
```

This install the mysql server package. Other OS may have different but
similar steps.

Then configure the database service, which includes setting up the
root password

``` sudo mysql_secure_installation ```

#### Restore the data from the database dump

On the new server where the MySQL has been setup, execute this:

```
mysql -u root -p < mashupdb_01312021.sql
```

You will need the root password set from the previous step.

** Due to MySQL version changes the migration may be giving some
warning or errors. Follow the specific info to fix the possible
compatibility issue due to MySQL version change.**


## xsede_metrics

This repo has the code and script for retrieval and update of XSEDE
related publication, citation, and metrics data. The general steps for
monthly update are:

### Sync XSEDE account (user, project, organization) data:

```
 python XDEntity.py
```

### Update XSEDE publication data from XUP:

```
 python xdpubMashupSQLV2.py
```

### Update citation data from Web of Knowledge:

```
 python isi_cites_monthly_update.py
 ```
 
The results are temporarily put into text files. Due to the large
amount of publications to be checked, we start a bunch of processes
like this:

```
python isi_cites_monthly_update.py 2000 0
```
* TODO: more automated way for this porcess (starting from getting the current number of publications and then divide into subporcesses to run)

This will retrieve the
citation data for the 2000 publications starting at
offset 0. Currently we have about 28k vetted XSEDE publications
(growing ~100-400 each month), so we need to start ~15 processes
simultaneously.

This process would take ~12 hours to finish even with the parallel
retrieval mode.

### Update the citation data into the mashup db:

```
 python isi_cites_monthly_db_upsert.py
```

This updates the retrieved citation data to the mashup db. The main citation table is backed up each month before the update, so we have the historical record for each month.

### Update the citation data into the mashup db:

```
 python isi_cites_monthly_metrics_xdreport_stats.py
```

This will generate scientific impact metrics summary for the specified month used for the XSEDE report.

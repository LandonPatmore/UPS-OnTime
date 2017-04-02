<p align="center">
  <img src="http://i0.wp.com/flyrfd.com/wp-content/uploads/2015/09/ups-logo.jpg" width="150">
</p>

# UPS On-Time Analytics
### WINNER BRICKHACK3, MOST CREATIVE USE OF UPS APIs

### Synopsis and Motivation
* The main purpose of this application to provide UPS administrators with statistical delivery data

### Description
* In a perfect world - the UPS On-Time Analytics package will take a set of delivered packages for a specific area and check the estimated times based on the service type (GROUND or AIR) and compare them to the actual times the package was delivered.  The package then will crunch the data and spit out a correlation chart with clusters showing when packages are delivered in that area compared to when they were estimated.  It also will keep track of percentages of On-Time to Not-Making-It-On-Time packages and have a threshold of about 90%.  If the threshold dips below 90%, it will alert the server telling UPS to look at this specific area and figure out why packages aren't getting there on time more than 90% of the time.

* What it does - It pulls the actual dates and times the package was delivered and also the estimated dates and times and keeps track of the On-Time percentage of a specific area.

## How to Run
```
cd UPS-OnTime
python ./UPS-OnTime
```
Follow prompts - Debug data is included


### Data Sources
* UPS-provided APIs

* UPS-provided Tracking Numbers

* Personal UPS Tracking Numbers

### Languages
* Python

### Contributors:
* Landon Patmore *lpatmore@oswego.edu* (Project Developer)
* Jeffrey Johnson *jjohns28@oswego.edu* (GitHub Documentation)
* Cesar Rincon *crincon@oswego.edu* (Debug Tester)

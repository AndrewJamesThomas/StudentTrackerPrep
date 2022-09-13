# Student Tracker Prep
This project aims to make it easier to process Slate data for clearinghouse StudentTracker (<a href="https://www.studentclearinghouse.org/colleges/studenttracker/">If you are unfamiliar with StudentTracker you can learn more about it here</a>). StudentTracker is a little finicky about how data is loaded into it, so it is important that attention is paid to make sure all requirements are met. Fortunately, this repo has everything you need to make this process as painless as possible.

## Set up:
Before you begin make sure you have the following tools installed on your computer:
<ul>
  <li>Python</li>
  <li>The python libraries in the requirements.txt fiel</li>
  <li>Microsoft Excel</li>
</ul>

## Step 1: Slate Query
Start by building a Slate query with the following exports. Note that these exact fields (And exact names) must be used, but you may use whatever filters you need. 

<ul>
  <li>Application Slate ID</li>
  <li>First</li>
  <li>Middle</li>
  <li>Last</li>
  <li>Suffix</li>
  <li>Birthdate</li> 
  <li>Submitted</li>
</ul>

The Slate query should resemble this.

<img src="https://github.com/thomasandr/StudentTrackerPrep/blob/main/assets/query.jpg">

With your query built, you should download this github repo to your desktop and save the query as a csv in the "data/clean" directory.

## Step 2: Run Python Script
With the data downloaded, open the process.py file in the /src directory using your preferred python IDE. Update the FILE_NAME variable to match the name of the csv you just downloaded from Slate. Next, run the script! An excel document should open with all of your data correctly formatted.

## Step 3: QC and sending to IR
Your data should be ready at this point, but take a second anyways to look it over and make sure it matches the requirements detailed in the "NSC FTP Tracker Instructions" (included in this repo). Once you are satisfied, <b>save the file as a .txt file</b>. This is important. 

Finally, send the file to someone in Institutional Research to upload to StudentTracker. This may take a few days, depending on how busy IR is. When the data is returned, it may take some work to clean up and make useable, but we will leave that for another project.

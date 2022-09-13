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
Start by building a Slate query with the following exports. Note that these exact fields must be used, but you may use whatever filters you need.

<ul>
  <li>Application/Student ID</li>
  <li>First Name</li>
  <li>Middle Name</li>
  <li>Last Name</li>
  <li>Suffix</li>
  <li>Birhdate</li> 
  <li>Search date (application submitted date)</li>
</ul>

The Slate query should resemble this. Again, there is not much flexability as to what exports you can use. It is possible to use a different person ID field or a different search date, but this is generally not recommended.

<img src="https://github.com/thomasandr/StudentTrackerPrep/blob/main/assets/query.jpg">

With your query built, you should download this github repo to your desktop and save the query as a csv in the "data/clean" directory.

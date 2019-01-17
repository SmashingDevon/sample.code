MSV: ms.wrangler
VER: v0.0.1

Pre-Requisites:

Install Python3

Ubuntu
From BASH Shell Execute

sudo bash apt-get python3

Install Python Packages

PyTest = https://docs.pytest.org/en/latest/getting-started.html  
Invoke = http://www.pyinvoke.org/installing.html
Pandas = https://pandas.pydata.org/pandas-docs/stable/install.html

Logic:

v0-0-2
- Invoke Infrastructure Automation to deploy to Cloud
- Scrape Data from external sources
  - URL Form parse and submission of data
    - Parse response and update DB
  - URL parse for meta Data
- Create scheduling agent
  - poll URL targets based on schedule profile
    - cache content attributes
    - scan for changes
    - update DB if changes
    - notify subscribers to data channel of new data availability
v0-0-1
+ Validate Source Data URL
+ Populate Master Model from Source Data URL
  + Validate data format
  + Dynamic calculations
- Build MicroService Container to expose Wrangled Data
  - Populate Couchbase DB with "Wrangled" Data
  - Populate Neo4j DB with "Wrangled" Data

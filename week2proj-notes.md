Week 2 API PIPELINE PROJ

Mistakes to avoid:
- Do not forget to freeze the requirements.txt file


As a free API I used: https://docs.coingecko.com

This simple ETL is straightforward:
- in db.py we connect to db
- in extract.py we send request to our API, an it returns us a json datatype of info
- in transform.py we convert the info to dataframe (or whatever we need)
- in load.py we ingest the info into our tables in db
- main.py is orchestrating this process.
- in analysis_queries.sql we play around with the data for analysis purposes. However, the first version of this implementation is very basic. Right now the pipeline uses if_exists="replace", meaning every pipeline deletes old data (not a good idea for analysis :D). I correct this in the next commit.
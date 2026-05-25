Week 2 API PIPELINE PROJ

Mistakes to avoid:
- Do not forget to freeze the requirements.txt file
- I spent quite some time debugging why DATABASE_URL is returning postgresql://None:None@None:None/None
    a useful function for this debug: load_dotenv(find_dotenv())
- For some reason my terminal's cache was not clearing and it kept looking at the wrong venv
- deleted venv and created a new one, cleared cache again, reloaded windows, then it worked


As a free API I used: https://docs.coingecko.com

This simple ETL is straightforward:
- in db.py we connect to db
- in extract.py we send request to our API, an it returns us a json datatype of info
- in transform.py we convert the info to dataframe (or whatever we need)
- in load.py we ingest the info into our tables in db
- main.py is orchestrating this process.
- in analysis_queries.sql we play around with the data for analysis purposes. However, the first version of this implementation is very basic. Right now the pipeline uses if_exists="replace", meaning every pipeline deletes old data (not a good idea for analysis :D). I correct this in the next commit.


Now let's go deeper in the concern we introduced yesterday.
in load.py, if_exists="" could be: 1- fail: when accidental overwrite is dangrous or if schema control matters, 2- replace, and 3- append: data grows over time, historical analysis is possible, should manage duplicates, new dataframe columns must match existing table structure.

Good practices:
- separating configuration and application logic
- Never push credentials to GitHub, that's why we added .env1 to .gitignore 

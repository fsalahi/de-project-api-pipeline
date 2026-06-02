## Week 2

- Mini project: Crypto Market ETL Pipeline

## Pipeline flow: 
- API → Python → Transformation → PostgreSQL → Analytics Queries# de-project-api-pipeline

## Project Architecture
API
 ↓
Extract
 ↓
Validate
 ↓
Transform
 ↓
Load
 ↓
PostgreSQL

## Project Goal
    - Fetch cryptocurrency market data from a public API.
    - Store:
        coin name
        symbol
        current price
        market cap
        daily change
    inside PostgreSQL.
    - Then run analytical SQL queries.



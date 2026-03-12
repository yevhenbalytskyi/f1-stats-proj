# F1 Stats Project

## Overview

This project collects Formula 1 data from the OpenF1 API and stores it in a PostgreSQL database for later analysis.

The API is treated as a **data source**, while the local database becomes the **source of truth**.

Pipeline:

```
OpenF1 API → Python ingestion → PostgreSQL → analysis
```

---

## Core Identifiers

Most OpenF1 data revolves around three identifiers:

```
meeting_key   → race weekend
session_key   → specific session
driver_number → driver identifier
```

Hierarchy:

```
meeting → session → drivers → race data
```

---

## Database Structure

Main tables:

```
drivers
teams
meetings
sessions
drivers_sessions
laps
stints
pit_stops
intervals
```

Hierarchy:

```
meetings
   ↓
sessions
   ↓
drivers_sessions
   ↓
laps / stints / pit_stops / intervals
```

---

## Project Structure

```
src
 ├ api        # OpenF1 requests
 ├ db         # database connection + SQL
 ├ ingest     # data ingestion scripts
 ├ models     # internal data structures
 └ main.py

sql
  schema.sql
```

---

## Layer Responsibilities

**api**

Fetch raw data from OpenF1.

**db**

Handle PostgreSQL connection and SQL operations.

**ingest**

Orchestrate the pipeline:

```
fetch API → transform → store in DB
```

---

## Design Rules

1. **Separation of concerns**

Never mix in one function:

```
API calls
SQL queries
analysis logic
```

2. **Pipeline mindset**

```
API → store → analyze
```

Data is stored locally before analysis.

3. **Small modules**

If a file becomes large (more than 200 lines), split it into smaller modules.

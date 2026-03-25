from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
import sqlite3

from db import engine
from llm import english_to_sql
from security import validate_sql

app = FastAPI(title="Natural Language to SQL API (Secure)")


class QueryRequest(BaseModel):
    sql_query: str


def get_db_schema():
    schema = {}
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        for (table,) in tables:
            cursor.execute(f"PRAGMA table_info({table})")
            schema[table] = [col[1] for col in cursor.fetchall()]
    return schema


@app.get("/")
def root():
    return {"message": "Secure NL to SQL backend is running"}


@app.get("/schema")
def schema():
    return get_db_schema()


@app.post("/query")
def execute_query(request: QueryRequest):
    question = request.sql_query
    schema = get_db_schema()

    raw_sql = english_to_sql(question, schema)
    safe_sql = validate_sql(raw_sql)

    try:
        with engine.connect() as conn:
            result = conn.execute(text(safe_sql))
            columns = result.keys()
            rows = result.fetchall()

        data = [dict(zip(columns, row)) for row in rows]

        return {
            "generated_sql": safe_sql,
            "row_count": len(data),
            "data": data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

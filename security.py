import re
from fastapi import HTTPException

FORBIDDEN_KEYWORDS = [
    "delete", "update", "insert",
    "drop", "alter", "truncate", "create"
]

MAX_ROWS = 50


def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()


def validate_sql(sql: str) -> str:
    if not sql:
        raise HTTPException(status_code=400, detail="Empty SQL")

    sql = clean_sql(sql)
    sql_lower = sql.lower()

    if not sql_lower.startswith("select"):
        raise HTTPException(status_code=400, detail="Only SELECT allowed")

    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", sql_lower):
            raise HTTPException(
                status_code=400,
                detail=f"Forbidden keyword: {keyword}"
            )

    if "limit" not in sql_lower:
        sql = sql.rstrip(";") + f" LIMIT {MAX_ROWS};"

    return sql

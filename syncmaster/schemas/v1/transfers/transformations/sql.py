# SPDX-FileCopyrightText: 2023-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
import re
from typing import Literal

from pydantic import BaseModel, Field, field_validator

ALLOWED_QUERY_TYPE = re.compile(r"^\s*(SELECT|WITH)\b", re.IGNORECASE)
QUERY_CONTAINS_FROM_SOURCE = re.compile(r"\bFROM\s+source\b", re.IGNORECASE)


class Sql(BaseModel):
    type: Literal["sql"]
    query: str = Field(examples=["SELECT col1, col2 FROM source WHERE col3 <= 20"])
    dialect: Literal["spark"] = Field(default="spark", description="Static value for now")

    @field_validator("query", mode="after")
    @classmethod
    def _validate_query(cls, value: str) -> str:
        if not ALLOWED_QUERY_TYPE.match(value):
            msg = "Query must be a SELECT statement"
            raise ValueError(msg)

        if not QUERY_CONTAINS_FROM_SOURCE.search(value):
            msg = "Query must contain `FROM source` clause"
            raise ValueError(msg)

        return value

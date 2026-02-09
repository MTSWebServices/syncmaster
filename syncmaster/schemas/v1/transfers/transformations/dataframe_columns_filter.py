# SPDX-FileCopyrightText: 2023-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from typing import Annotated, Literal

from pydantic import BaseModel, Field


class BaseColumnsFilter(BaseModel):
    field: str


class IncludeFilter(BaseColumnsFilter):
    type: Literal["include"]


class RenameFilter(BaseColumnsFilter):
    type: Literal["rename"]
    to: str = Field(examples=["new_column_name"])


class CastFilter(BaseColumnsFilter):
    type: Literal["cast"]
    as_type: str = Field(examples=["int"])


ColumnsFilter = IncludeFilter | RenameFilter | CastFilter


class DataframeColumnsFilter(BaseModel):
    type: Literal["dataframe_columns_filter"]
    filters: list[Annotated[ColumnsFilter, Field(discriminator="type")]] = Field(default_factory=list)

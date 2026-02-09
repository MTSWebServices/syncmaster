# SPDX-FileCopyrightText: 2023-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from typing import Annotated, Literal

from pydantic import BaseModel, Field


class BaseRowsFilter(BaseModel):
    field: str


class IsNullFilter(BaseRowsFilter):
    type: Literal["is_null"]


class IsNotNullFilter(BaseRowsFilter):
    type: Literal["is_not_null"]


class EqualFilter(BaseRowsFilter):
    type: Literal["equal"]
    value: str = Field(examples=["123"])


class NotEqualFilter(BaseRowsFilter):
    type: Literal["not_equal"]
    value: str = Field(examples=["123"])


class GreaterThanFilter(BaseRowsFilter):
    type: Literal["greater_than"]
    value: str = Field(examples=["123"])


class GreaterOrEqualFilter(BaseRowsFilter):
    type: Literal["greater_or_equal"]
    value: str = Field(examples=["123"])


class LessThanFilter(BaseRowsFilter):
    type: Literal["less_than"]
    value: str = Field(examples=["123"])


class LessOrEqualFilter(BaseRowsFilter):
    type: Literal["less_or_equal"]
    value: str = Field(examples=["123"])


class LikeFilter(BaseRowsFilter):
    type: Literal["like"]
    value: str = Field(examples=["%.json"])


class ILikeFilter(BaseRowsFilter):
    type: Literal["ilike"]
    value: str = Field(examples=["%.json"])


class NotLikeFilter(BaseRowsFilter):
    type: Literal["not_like"]
    value: str = Field(examples=["%.json"])


class NotILikeFilter(BaseRowsFilter):
    type: Literal["not_ilike"]
    value: str = Field(examples=["%.json"])


class RegexpFilter(BaseRowsFilter):
    type: Literal["regexp"]
    value: str = Field(examples=[r"^\d+\.json$"])


RowsFilter = (
    IsNullFilter
    | IsNotNullFilter
    | EqualFilter
    | NotEqualFilter
    | GreaterThanFilter
    | GreaterOrEqualFilter
    | LessThanFilter
    | LessOrEqualFilter
    | LikeFilter
    | ILikeFilter
    | NotLikeFilter
    | NotILikeFilter
    | RegexpFilter
)


class DataframeRowsFilter(BaseModel):
    type: Literal["dataframe_rows_filter"]
    filters: list[Annotated[RowsFilter, Field(discriminator="type")]] = Field(default_factory=list)

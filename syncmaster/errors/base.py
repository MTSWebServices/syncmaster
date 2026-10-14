# SPDX-FileCopyrightText: 2023-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from typing import Any

from pydantic import BaseModel


class BaseErrorSchema(BaseModel):
    code: str
    message: str
    details: Any


class APIErrorSchema[ErrorModel: BaseErrorSchema](BaseModel):
    error: ErrorModel

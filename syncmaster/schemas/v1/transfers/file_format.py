# SPDX-FileCopyrightText: 2023-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

from syncmaster.schemas.v1.file_formats import (
    CSV_FORMAT,
    EXCEL_FORMAT,
    JSON_FORMAT,
    JSONLINE_FORMAT,
    ORC_FORMAT,
    PARQUET_FORMAT,
    XML_FORMAT,
)


class ORCCompression(str, Enum):  # noqa: UP042
    NONE = "none"
    SNAPPY = "snappy"
    ZLIB = "zlib"
    LZ4 = "lz4"


class ParquetCompression(str, Enum):  # noqa: UP042
    NONE = "none"
    SNAPPY = "snappy"
    GZIP = "gzip"
    LZ4 = "lz4"


class JSONCompression(str, Enum):  # noqa: UP042
    NONE = "none"
    BZIP2 = "bzip2"
    GZIP = "gzip"
    LZ4 = "lz4"
    SNAPPY = "snappy"
    DEFLATE = "deflate"


class CSVCompression(str, Enum):  # noqa: UP042
    NONE = "none"
    BZIP2 = "bzip2"
    GZIP = "gzip"
    LZ4 = "lz4"
    SNAPPY = "snappy"
    DEFLATE = "deflate"


class XMLCompression(str, Enum):  # noqa: UP042
    NONE = "none"
    BZIP2 = "bzip2"
    GZIP = "gzip"
    LZ4 = "lz4"
    SNAPPY = "snappy"


class CSV(BaseModel):
    type: CSV_FORMAT = "csv"
    delimiter: str = ","
    encoding: str = "utf-8"
    quote: str = '"'
    escape: str = "\\"
    include_header: bool = False
    line_sep: str = "\n"
    compression: CSVCompression = CSVCompression.GZIP


class JSONLine(BaseModel):
    type: JSONLINE_FORMAT = "jsonline"
    encoding: str = "utf-8"
    line_sep: str = "\n"
    compression: JSONCompression = JSONCompression.GZIP


class JSON(BaseModel):
    type: JSON_FORMAT = "json"
    encoding: str = "utf-8"
    line_sep: str = "\n"
    compression: JSONCompression = JSONCompression.GZIP


class Excel(BaseModel):
    type: EXCEL_FORMAT = "excel"
    include_header: bool = False
    start_cell: str | None = None


class XML(BaseModel):
    type: XML_FORMAT = "xml"
    root_tag: str
    row_tag: str
    compression: XMLCompression = XMLCompression.GZIP


class ORC(BaseModel):
    type: ORC_FORMAT = "orc"
    compression: ORCCompression = ORCCompression.ZLIB


class Parquet(BaseModel):
    type: PARQUET_FORMAT = "parquet"
    compression: ParquetCompression = ParquetCompression.SNAPPY

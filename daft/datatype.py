from __future__ import annotations

import builtins

import pyarrow as pa

from daft.daft import PyDataType


class DataType:
    _dtype: PyDataType

    def __init__(self) -> None:
        raise NotImplementedError(
            "We do not support creating a DataType via __init__ "
            "use a creator method like DataType.int32() or use DataType.from_arrow_type(pa_type)"
        )

    @staticmethod
    def _from_pydatatype(pydt: PyDataType) -> DataType:
        dt = DataType.__new__(DataType)
        dt._dtype = pydt
        return dt

    @staticmethod
    def int8() -> DataType:
        return DataType._from_pydatatype(PyDataType.int8())

    @staticmethod
    def int16() -> DataType:
        return DataType._from_pydatatype(PyDataType.int16())

    @staticmethod
    def int32() -> DataType:
        return DataType._from_pydatatype(PyDataType.int32())

    @staticmethod
    def int64() -> DataType:
        return DataType._from_pydatatype(PyDataType.int64())

    @staticmethod
    def uint8() -> DataType:
        return DataType._from_pydatatype(PyDataType.uint8())

    @staticmethod
    def uint16() -> DataType:
        return DataType._from_pydatatype(PyDataType.uint16())

    @staticmethod
    def uint32() -> DataType:
        return DataType._from_pydatatype(PyDataType.uint32())

    @staticmethod
    def uint64() -> DataType:
        return DataType._from_pydatatype(PyDataType.uint64())

    @staticmethod
    def float32() -> DataType:
        return DataType._from_pydatatype(PyDataType.float32())

    @staticmethod
    def float64() -> DataType:
        return DataType._from_pydatatype(PyDataType.float64())

    @staticmethod
    def string() -> DataType:
        return DataType._from_pydatatype(PyDataType.string())

    @staticmethod
    def bool() -> DataType:
        return DataType._from_pydatatype(PyDataType.bool())

    @staticmethod
    def binary() -> DataType:
        return DataType._from_pydatatype(PyDataType.binary())

    @staticmethod
    def null() -> DataType:
        return DataType._from_pydatatype(PyDataType.null())

    @staticmethod
    def from_arrow_type(arrow_type: pa.lib.DataType) -> DataType:
        if pa.types.is_int8(arrow_type):
            return DataType.int8()
        elif pa.types.is_int16(arrow_type):
            return DataType.int16()
        elif pa.types.is_int32(arrow_type):
            return DataType.int32()
        elif pa.types.is_int64(arrow_type):
            return DataType.int64()
        elif pa.types.is_uint8(arrow_type):
            return DataType.uint8()
        elif pa.types.is_uint16(arrow_type):
            return DataType.uint16()
        elif pa.types.is_uint32(arrow_type):
            return DataType.uint32()
        elif pa.types.is_uint64(arrow_type):
            return DataType.uint64()
        elif pa.types.is_float32(arrow_type):
            return DataType.float32()
        elif pa.types.is_float64(arrow_type):
            return DataType.float64()
        elif pa.types.is_string(arrow_type) or pa.types.is_large_string(arrow_type):
            return DataType.string()
        elif pa.types.is_binary(arrow_type) or pa.types.is_large_binary(arrow_type):
            return DataType.binary()
        elif pa.types.is_boolean(arrow_type):
            return DataType.bool()
        elif pa.types.is_null(arrow_type):
            return DataType.null()
        else:
            raise NotImplementedError(f"we cant convert arrow type: {arrow_type} to a daft type")

    def __repr__(self) -> str:
        return f"DataType({self._dtype})"

    def __eq__(self, other: object) -> builtins.bool:
        return isinstance(other, DataType) and self._dtype.is_equal(other._dtype)

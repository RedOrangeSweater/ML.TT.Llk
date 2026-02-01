# SPDX-FileCopyrightText: (c) 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

"""
Pydantic models for fused-test YAML config (Input layer contract).

Validation-only: allowed values and required fields. Conversion to runtime
objects (FusedOperation, FuserConfig) lives in fuser_config_parser.
"""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field, field_validator, model_validator


# -----------------------------------------------------------------------------
# Global config (top-level YAML)
# -----------------------------------------------------------------------------

DestAccLiteral = Literal["Yes", "No"]


class FuserYamlGlobal(BaseModel):
    """Validated global settings from fused YAML (dest_acc, profiler_enabled, loop_factor)."""

    dest_acc: DestAccLiteral = "No"
    profiler_enabled: bool = False
    loop_factor: int = Field(default=16, ge=1)


# -----------------------------------------------------------------------------
# SFPU entries (discriminated by type)
# -----------------------------------------------------------------------------

SfpuUnaryOperationLiteral = Literal[
    "Abs", "Acosh", "Asinh", "Atanh", "Celu", "Cos", "Elu", "Exp", "Exp2",
    "Fill", "Gelu", "Hardsigmoid", "Log", "Log1p", "Neg", "Reciprocal",
    "ReluMax", "ReluMin", "Rsqrt", "Silu", "Sin", "Sqrt", "Square", "Threshold",
]

SfpuBinaryOperationLiteral = Literal[
    "SfpuElwadd", "SfpuElwmul", "SfpuElwsub",
    "SfpuElwLeftShift", "SfpuElwRightShift", "SfpuElwLogicalRightShift",
    "SfpuXlogy", "SfpuAddTopRow",
]

ApproximationModeLiteral = Literal["Yes", "No"]


class SfpuUnaryYaml(BaseModel):
    """UnarySfpu block in math.sfpu[]."""

    type: Literal["UnarySfpu"] = "UnarySfpu"
    operation: SfpuUnaryOperationLiteral
    approximation_mode: ApproximationModeLiteral = "No"
    iterations: int = Field(default=8, ge=1)
    dst_dest_tile_index: int = Field(default=0, ge=0)
    fill_const_value: float = 1.0


class SfpuBinaryYaml(BaseModel):
    """BinarySfpu block in math.sfpu[]."""

    type: Literal["BinarySfpu"] = "BinarySfpu"
    operation: SfpuBinaryOperationLiteral
    approximation_mode: ApproximationModeLiteral = "No"
    iterations: int = Field(default=8, ge=1)
    src1_dest_tile_index: int = Field(default=0, ge=0)
    src2_dest_tile_index: int = Field(default=0, ge=0)
    dst_dest_tile_index: int = Field(default=0, ge=0)


SfpuEntryYaml = Annotated[
    SfpuUnaryYaml | SfpuBinaryYaml,
    Field(discriminator="type"),
]


# -----------------------------------------------------------------------------
# Math config (fpu + optional reduce_pool + optional sfpu list)
# -----------------------------------------------------------------------------

FpuLiteral = Literal[
    "Datacopy", "Elwadd", "Elwmul", "Elwsub",
    "Matmul", "ReduceColumn", "ReduceRow", "ReduceScalar",
]

ReducePoolLiteral = Literal["Sum", "Min", "Max", "Average"]


class MathYaml(BaseModel):
    """math block per operation."""

    fpu: FpuLiteral = "Datacopy"
    reduce_pool: ReducePoolLiteral | None = None
    sfpu: list[SfpuEntryYaml] = Field(default_factory=list)

    @model_validator(mode="after")
    def reduce_pool_required_for_reduce(self):
        if self.fpu in ("ReduceColumn", "ReduceRow", "ReduceScalar") and self.reduce_pool is None:
            raise ValueError("reduce_pool is required when fpu is ReduceColumn, ReduceRow, or ReduceScalar")
        return self


# -----------------------------------------------------------------------------
# Data format and hardware option literals
# -----------------------------------------------------------------------------

DataFormatLiteral = Literal["Float16_b", "Float16", "Float32", "Bfp8_b"]
UnpackerLiteral = Literal["UnpackerA", "UnpackerAB", "UnpackerTilizeA", "MatmulUnpacker"]
PackerLiteral = Literal["Packer"]
MathFidelityLiteral = Literal["LoFi", "HiFi2", "HiFi3", "HiFi4"]
DestSyncLiteral = Literal["Full", "Half"]
TransposeLiteral = Literal["Yes", "No"]


class OperationYaml(BaseModel):
    """Single operation in operations[]."""

    src_a: str
    src_b: str
    output: str
    src_a_dims: list[int] = Field(default_factory=lambda: [32, 32], min_length=2, max_length=2)
    src_b_dims: list[int] = Field(default_factory=lambda: [32, 32], min_length=2, max_length=2)
    input_format: DataFormatLiteral = "Float16_b"
    output_format: DataFormatLiteral = "Float16_b"
    unpacker: UnpackerLiteral = "UnpackerA"
    math: MathYaml = Field(default_factory=MathYaml)
    packer: PackerLiteral = "Packer"
    math_fidelity: MathFidelityLiteral | None = None
    dest_sync: DestSyncLiteral | None = None
    unpack_transpose_within_face: TransposeLiteral | None = None
    unpack_transpose_faces: TransposeLiteral | None = None
    output_pack_dims: list[int] | None = None
    src_a_const_value: float | None = None
    src_b_const_value: float | None = None

    @field_validator("src_a_dims", "src_b_dims")
    @classmethod
    def dims_multiple_32(cls, v: list[int]) -> list[int]:
        for i, x in enumerate(v):
            if x <= 0 or x % 32 != 0:
                raise ValueError(f"Dimension must be positive and multiple of 32, got {x}")
        return v

    @field_validator("output_pack_dims")
    @classmethod
    def output_pack_dims_valid(cls, v: list[int] | None) -> list[int] | None:
        if v is None:
            return None
        if len(v) != 2:
            raise ValueError("output_pack_dims must have exactly 2 elements")
        for x in v:
            if x <= 0 or x % 32 != 0:
                raise ValueError(f"output_pack_dims values must be positive and multiple of 32, got {v}")
        return v


# -----------------------------------------------------------------------------
# Root YAML config
# -----------------------------------------------------------------------------


class FuserYamlConfig(BaseModel):
    """Root validated structure: global fields + operations list."""

    dest_acc: DestAccLiteral = "No"
    profiler_enabled: bool = False
    loop_factor: int = Field(default=16, ge=1)
    operations: list[OperationYaml] = Field(default_factory=list, min_length=1)

    def to_global(self) -> FuserYamlGlobal:
        """Extract global settings as FuserYamlGlobal."""
        return FuserYamlGlobal(
            dest_acc=self.dest_acc,
            profiler_enabled=self.profiler_enabled,
            loop_factor=self.loop_factor,
        )

# SPDX-FileCopyrightText: (c) 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

"""
Parse-only unit tests for fused YAML config (Pydantic models).

No device access; validates example.yaml and invalid snippets.
"""

from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from .fuser_yaml_models import FuserYamlConfig, MathYaml, OperationYaml


def _fuser_config_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "fuser_config"


def test_example_yaml_loads():
    """example.yaml parses and validates as FuserYamlConfig."""
    yaml_path = _fuser_config_dir() / "example.yaml"
    if not yaml_path.exists():
        pytest.skip(f"example.yaml not found at {yaml_path}")
    with open(yaml_path) as f:
        raw = yaml.safe_load(f)
    config = FuserYamlConfig.model_validate(raw)
    assert config.dest_acc == "Yes"
    assert config.profiler_enabled is True
    assert config.loop_factor == 16
    assert len(config.operations) >= 1
    global_ = config.to_global()
    assert global_.dest_acc == "Yes"
    assert global_.loop_factor == 16


def test_valid_minimal_config():
    """Minimal valid config with one operation validates."""
    raw = {
        "dest_acc": "No",
        "operations": [
            {
                "src_a": "input_A",
                "src_b": "input_B",
                "output": "out",
                "input_format": "Float16_b",
                "output_format": "Float16_b",
                "unpacker": "UnpackerA",
                "math": {"fpu": "Datacopy"},
                "packer": "Packer",
            }
        ],
    }
    config = FuserYamlConfig.model_validate(raw)
    assert len(config.operations) == 1
    op = config.operations[0]
    assert op.src_a == "input_A"
    assert op.math.fpu == "Datacopy"


def test_invalid_dest_acc_raises():
    """Invalid dest_acc value raises ValidationError."""
    raw = {
        "dest_acc": "Invalid",
        "operations": [
            {
                "src_a": "a",
                "src_b": "b",
                "output": "c",
                "unpacker": "UnpackerA",
                "math": {"fpu": "Datacopy"},
                "packer": "Packer",
            }
        ],
    }
    with pytest.raises(ValidationError) as exc_info:
        FuserYamlConfig.model_validate(raw)
    assert "dest_acc" in str(exc_info.value).lower() or "Invalid" in str(exc_info.value)


def test_invalid_input_format_raises():
    """Invalid input_format raises ValidationError."""
    raw = {
        "operations": [
            {
                "src_a": "a",
                "src_b": "b",
                "output": "c",
                "input_format": "InvalidFormat",
                "output_format": "Float16_b",
                "unpacker": "UnpackerA",
                "math": {"fpu": "Datacopy"},
                "packer": "Packer",
            }
        ],
    }
    with pytest.raises(ValidationError) as exc_info:
        FuserYamlConfig.model_validate(raw)
    assert "input_format" in str(exc_info.value).lower() or "InvalidFormat" in str(exc_info.value)


def test_empty_operations_raises():
    """Empty operations list raises ValidationError (min_length=1)."""
    raw = {"dest_acc": "No", "operations": []}
    with pytest.raises(ValidationError) as exc_info:
        FuserYamlConfig.model_validate(raw)
    assert "operations" in str(exc_info.value).lower()


def test_reduce_without_reduce_pool_raises():
    """Reduce fpu without reduce_pool raises ValidationError."""
    raw = {
        "fpu": "ReduceColumn",
        "sfpu": [],
    }
    with pytest.raises(ValidationError) as exc_info:
        MathYaml.model_validate(raw)
    assert "reduce_pool" in str(exc_info.value).lower() or "ReduceColumn" in str(exc_info.value)


def test_sfpu_unary_validates():
    """UnarySfpu entry in math.sfpu validates."""
    raw = {
        "fpu": "Datacopy",
        "sfpu": [
            {
                "type": "UnarySfpu",
                "operation": "Exp",
                "approximation_mode": "No",
                "iterations": 128,
            }
        ],
    }
    math = MathYaml.model_validate(raw)
    assert len(math.sfpu) == 1
    assert math.sfpu[0].type == "UnarySfpu"
    assert math.sfpu[0].operation == "Exp"


def test_sfpu_binary_validates():
    """BinarySfpu entry in math.sfpu validates."""
    raw = {
        "fpu": "Datacopy",
        "sfpu": [
            {
                "type": "BinarySfpu",
                "operation": "SfpuElwadd",
                "src1_dest_tile_index": 0,
                "src2_dest_tile_index": 1,
                "dst_dest_tile_index": 1,
            }
        ],
    }
    math = MathYaml.model_validate(raw)
    assert len(math.sfpu) == 1
    assert math.sfpu[0].type == "BinarySfpu"
    assert math.sfpu[0].operation == "SfpuElwadd"


def test_invalid_sfpu_type_raises():
    """Unknown sfpu type raises ValidationError."""
    raw = {
        "fpu": "Datacopy",
        "sfpu": [{"type": "UnknownSfpu", "operation": "Exp"}],
    }
    with pytest.raises(ValidationError) as exc_info:
        MathYaml.model_validate(raw)
    assert "type" in str(exc_info.value).lower() or "discriminator" in str(exc_info.value).lower()


def test_operation_dims_multiple_of_32():
    """Operation src_a_dims / src_b_dims must be positive and multiple of 32."""
    raw = {
        "src_a": "a",
        "src_b": "b",
        "output": "c",
        "src_a_dims": [33, 32],
        "src_b_dims": [32, 32],
        "unpacker": "UnpackerA",
        "math": {"fpu": "Datacopy"},
        "packer": "Packer",
    }
    with pytest.raises(ValidationError) as exc_info:
        OperationYaml.model_validate(raw)
    assert "32" in str(exc_info.value) or "dimension" in str(exc_info.value).lower()

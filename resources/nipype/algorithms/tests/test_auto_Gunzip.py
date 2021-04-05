# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import Gunzip


def test_Gunzip_inputs():
    input_map = dict(
        in_file=dict(
            extensions=None,
            mandatory=True,
        ),
    )
    inputs = Gunzip.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Gunzip_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = Gunzip.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
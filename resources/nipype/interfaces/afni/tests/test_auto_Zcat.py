# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Zcat


def test_Zcat_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        datum=dict(
            argstr="-datum %s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fscale=dict(
            argstr="-fscale",
            xor=["nscale"],
        ),
        in_files=dict(
            argstr="%s",
            copyfile=False,
            mandatory=True,
            position=-1,
        ),
        nscale=dict(
            argstr="-nscale",
            xor=["fscale"],
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_files",
            name_template="%s_zcat",
        ),
        outputtype=dict(),
        verb=dict(
            argstr="-verb",
        ),
    )
    inputs = Zcat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Zcat_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = Zcat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
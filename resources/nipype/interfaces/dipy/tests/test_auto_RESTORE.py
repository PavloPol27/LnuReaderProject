# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..reconstruction import RESTORE


def test_RESTORE_inputs():
    input_map = dict(
        b0_thres=dict(
            usedefault=True,
        ),
        in_bval=dict(
            extensions=None,
            mandatory=True,
        ),
        in_bvec=dict(
            extensions=None,
            mandatory=True,
        ),
        in_file=dict(
            extensions=None,
            mandatory=True,
        ),
        in_mask=dict(
            extensions=None,
        ),
        noise_mask=dict(
            extensions=None,
        ),
        out_prefix=dict(),
    )
    inputs = RESTORE.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RESTORE_outputs():
    output_map = dict(
        evals=dict(
            extensions=None,
        ),
        evecs=dict(
            extensions=None,
        ),
        fa=dict(
            extensions=None,
        ),
        md=dict(
            extensions=None,
        ),
        mode=dict(
            extensions=None,
        ),
        rd=dict(
            extensions=None,
        ),
        trace=dict(
            extensions=None,
        ),
    )
    outputs = RESTORE.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
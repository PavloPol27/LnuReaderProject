# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ImageMeants


def test_ImageMeants_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        eig=dict(
            argstr="--eig",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="-i %s",
            extensions=None,
            mandatory=True,
            position=0,
        ),
        mask=dict(
            argstr="-m %s",
            extensions=None,
        ),
        nobin=dict(
            argstr="--no_bin",
        ),
        order=dict(
            argstr="--order=%d",
            usedefault=True,
        ),
        out_file=dict(
            argstr="-o %s",
            extensions=None,
            genfile=True,
            hash_files=False,
        ),
        output_type=dict(),
        show_all=dict(
            argstr="--showall",
        ),
        spatial_coord=dict(
            argstr="-c %s",
        ),
        transpose=dict(
            argstr="--transpose",
        ),
        use_mm=dict(
            argstr="--usemm",
        ),
    )
    inputs = ImageMeants.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ImageMeants_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = ImageMeants.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
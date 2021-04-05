# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import os

from ...base import (
    CommandLine,
    CommandLineInputSpec,
    SEMLikeCommandLine,
    TraitedSpec,
    File,
    Directory,
    traits,
    isdefined,
    InputMultiPath,
    OutputMultiPath,
)


class UnbiasedNonLocalMeansInputSpec(CommandLineInputSpec):
    sigma = traits.Float(
        desc="The root power of noise (sigma) in the complex Gaussian process the Rician comes from. If it is underestimated, the algorithm fails to remove the noise. If it is overestimated, over-blurring is likely to occur.",
        argstr="--sigma %f",
    )
    rs = InputMultiPath(
        traits.Int,
        desc="The algorithm search for similar voxels in a neighborhood of this radius (radii larger than 5,5,5 are very slow, and the results can be only marginally better. Small radii may fail to effectively remove the noise).",
        sep=",",
        argstr="--rs %s",
    )
    rc = InputMultiPath(
        traits.Int,
        desc="Similarity between blocks is computed as the difference between mean values and gradients. These parameters are computed fitting a hyperplane with LS inside a neighborhood of this size",
        sep=",",
        argstr="--rc %s",
    )
    hp = traits.Float(
        desc="This parameter is related to noise; the larger the parameter, the more aggressive the filtering. Should be near 1, and only values between 0.8 and 1.2 are allowed",
        argstr="--hp %f",
    )
    ps = traits.Float(
        desc="To accelerate computations, preselection is used: if the normalized difference is above this threshold, the voxel will be discarded (non used for average)",
        argstr="--ps %f",
    )
    inputVolume = File(position=-2, desc="Input MRI volume.", exists=True, argstr="%s")
    outputVolume = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Output (filtered) MRI volume.",
        argstr="%s",
    )


class UnbiasedNonLocalMeansOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Output (filtered) MRI volume.", exists=True)


class UnbiasedNonLocalMeans(SEMLikeCommandLine):
    """title: Unbiased NLM for MRI

category: Filtering.Denoising

description: This module implements a fast version of the popular Non-Local Means filter for image denoising. This algorithm filters each pixel as a weighted average of its neighbors in a large vicinity. The weights are computed based on the similarity of each neighbor with the voxel to be denoised.
 In the original formulation a patch with a certain radius is centered in each of the voxels, and the Mean Squared Error between each pair of corresponding voxels is computed. In this implementation, only the mean value and gradient components are compared. This, together with an efficient memory management, can attain a speed-up of nearly 20x. Besides, the filtering is more accurate than the original with poor SNR.
 This code is intended for its use with MRI (or any other Rician-distributed modality): the second order moment is estimated, then we subtract twice the squared power of noise, and finally we take the square root of the result to remove the Rician bias.
 The original implementation of the NLM filter may be found in:
 A. Buades, B. Coll, J. Morel, "A review of image denoising algorithms, with a new one", Multiscale Modelling and Simulation 4(2): 490-530. 2005.
 The correction of the Rician bias is described in the following reference (among others):
 S. Aja-Fernandez, K. Krissian, "An unbiased Non-Local Means scheme for DWI filtering", in: Proceedings of the MICCAI Workshop on Computational Diffusion MRI, 2008, pp. 277-284.
 The whole description of this version may be found in the following paper (please, cite it if you are willing to use this software):
 A. Tristan-Vega, V. Garcia Perez, S. Aja-Fenandez, and C.-F. Westin, "Efficient and Robust Nonlocal Means Denoising of MR Data Based on Salient Features Matching", Computer Methods and Programs in Biomedicine. (Accepted for publication) 2011.

version: 0.0.1.$Revision: 1 $(beta)

documentation-url: http://www.slicer.org/slicerWiki/index.php/Modules:UnbiasedNonLocalMeans-Documentation-3.6

contributor: Antonio Tristan Vega, Veronica Garcia-Perez, Santiago Aja-Fernandez, Carl-Fredrik Westin

acknowledgements: Supported by grant number FMECD-2010/71131616E from the Spanish Ministry of Education/Fulbright Committee

"""

    input_spec = UnbiasedNonLocalMeansInputSpec
    output_spec = UnbiasedNonLocalMeansOutputSpec
    _cmd = " UnbiasedNonLocalMeans "
    _outputs_filenames = {"outputVolume": "outputVolume.nii"}
    _redirect_x = False
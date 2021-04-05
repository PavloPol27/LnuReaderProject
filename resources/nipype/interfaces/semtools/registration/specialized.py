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


class VBRAINSDemonWarpInputSpec(CommandLineInputSpec):
    movingVolume = InputMultiPath(
        File(exists=True),
        desc="Required: input moving image",
        argstr="--movingVolume %s...",
    )
    fixedVolume = InputMultiPath(
        File(exists=True),
        desc="Required: input fixed (target) image",
        argstr="--fixedVolume %s...",
    )
    inputPixelType = traits.Enum(
        "float",
        "short",
        "ushort",
        "int",
        "uchar",
        desc="Input volumes will be typecast to this format: float|short|ushort|int|uchar",
        argstr="--inputPixelType %s",
    )
    outputVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Required: output resampled moving image (will have the same physical space as the fixedVolume).",
        argstr="--outputVolume %s",
    )
    outputDisplacementFieldVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Output deformation field vector image (will have the same physical space as the fixedVolume).",
        argstr="--outputDisplacementFieldVolume %s",
    )
    outputPixelType = traits.Enum(
        "float",
        "short",
        "ushort",
        "int",
        "uchar",
        desc="outputVolume will be typecast to this format: float|short|ushort|int|uchar",
        argstr="--outputPixelType %s",
    )
    interpolationMode = traits.Enum(
        "NearestNeighbor",
        "Linear",
        "ResampleInPlace",
        "BSpline",
        "WindowedSinc",
        "Hamming",
        "Cosine",
        "Welch",
        "Lanczos",
        "Blackman",
        desc="Type of interpolation to be used when applying transform to moving volume.  Options are Linear, ResampleInPlace, NearestNeighbor, BSpline, or WindowedSinc",
        argstr="--interpolationMode %s",
    )
    registrationFilterType = traits.Enum(
        "Demons",
        "FastSymmetricForces",
        "Diffeomorphic",
        "LogDemons",
        "SymmetricLogDemons",
        desc="Registration Filter Type: Demons|FastSymmetricForces|Diffeomorphic|LogDemons|SymmetricLogDemons",
        argstr="--registrationFilterType %s",
    )
    smoothDisplacementFieldSigma = traits.Float(
        desc="A gaussian smoothing value to be applied to the deformation feild at each iteration.",
        argstr="--smoothDisplacementFieldSigma %f",
    )
    numberOfPyramidLevels = traits.Int(
        desc="Number of image pyramid levels to use in the multi-resolution registration.",
        argstr="--numberOfPyramidLevels %d",
    )
    minimumFixedPyramid = InputMultiPath(
        traits.Int,
        desc="The shrink factor for the first level of the fixed image pyramid. (i.e. start at 1/16 scale, then 1/8, then 1/4, then 1/2, and finally full scale)",
        sep=",",
        argstr="--minimumFixedPyramid %s",
    )
    minimumMovingPyramid = InputMultiPath(
        traits.Int,
        desc="The shrink factor for the first level of the moving image pyramid. (i.e. start at 1/16 scale, then 1/8, then 1/4, then 1/2, and finally full scale)",
        sep=",",
        argstr="--minimumMovingPyramid %s",
    )
    arrayOfPyramidLevelIterations = InputMultiPath(
        traits.Int,
        desc="The number of iterations for each pyramid level",
        sep=",",
        argstr="--arrayOfPyramidLevelIterations %s",
    )
    histogramMatch = traits.Bool(
        desc="Histogram Match the input images.  This is suitable for images of the same modality that may have different absolute scales, but the same overall intensity profile.",
        argstr="--histogramMatch ",
    )
    numberOfHistogramBins = traits.Int(
        desc="The number of histogram levels", argstr="--numberOfHistogramBins %d"
    )
    numberOfMatchPoints = traits.Int(
        desc="The number of match points for histrogramMatch",
        argstr="--numberOfMatchPoints %d",
    )
    medianFilterSize = InputMultiPath(
        traits.Int,
        desc="Median filter radius in all 3 directions.  When images have a lot of salt and pepper noise, this step can improve the registration.",
        sep=",",
        argstr="--medianFilterSize %s",
    )
    initializeWithDisplacementField = File(
        desc="Initial deformation field vector image file name",
        exists=True,
        argstr="--initializeWithDisplacementField %s",
    )
    initializeWithTransform = File(
        desc="Initial Transform filename",
        exists=True,
        argstr="--initializeWithTransform %s",
    )
    makeBOBF = traits.Bool(
        desc="Flag to make Brain-Only Background-Filled versions of the input and target volumes.",
        argstr="--makeBOBF ",
    )
    fixedBinaryVolume = File(
        desc="Mask filename for desired region of interest in the Fixed image.",
        exists=True,
        argstr="--fixedBinaryVolume %s",
    )
    movingBinaryVolume = File(
        desc="Mask filename for desired region of interest in the Moving image.",
        exists=True,
        argstr="--movingBinaryVolume %s",
    )
    lowerThresholdForBOBF = traits.Int(
        desc="Lower threshold for performing BOBF", argstr="--lowerThresholdForBOBF %d"
    )
    upperThresholdForBOBF = traits.Int(
        desc="Upper threshold for performing BOBF", argstr="--upperThresholdForBOBF %d"
    )
    backgroundFillValue = traits.Int(
        desc="Replacement value to overwrite background when performing BOBF",
        argstr="--backgroundFillValue %d",
    )
    seedForBOBF = InputMultiPath(
        traits.Int,
        desc="coordinates in all 3 directions for Seed when performing BOBF",
        sep=",",
        argstr="--seedForBOBF %s",
    )
    neighborhoodForBOBF = InputMultiPath(
        traits.Int,
        desc="neighborhood in all 3 directions to be included when performing BOBF",
        sep=",",
        argstr="--neighborhoodForBOBF %s",
    )
    outputDisplacementFieldPrefix = traits.Str(
        desc="Displacement field filename prefix for writing separate x, y, and z component images",
        argstr="--outputDisplacementFieldPrefix %s",
    )
    outputCheckerboardVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Genete a checkerboard image volume between the fixedVolume and the deformed movingVolume.",
        argstr="--outputCheckerboardVolume %s",
    )
    checkerboardPatternSubdivisions = InputMultiPath(
        traits.Int,
        desc="Number of Checkerboard subdivisions in all 3 directions",
        sep=",",
        argstr="--checkerboardPatternSubdivisions %s",
    )
    outputNormalized = traits.Bool(
        desc="Flag to warp and write the normalized images to output.  In normalized images the image values are fit-scaled to be between 0 and the maximum storage type value.",
        argstr="--outputNormalized ",
    )
    outputDebug = traits.Bool(
        desc="Flag to write debugging images after each step.", argstr="--outputDebug "
    )
    weightFactors = InputMultiPath(
        traits.Float,
        desc="Weight fatctors for each input images",
        sep=",",
        argstr="--weightFactors %s",
    )
    gradient_type = traits.Enum(
        "0",
        "1",
        "2",
        desc="Type of gradient used for computing the demons force (0 is symmetrized, 1 is fixed image, 2 is moving image)",
        argstr="--gradient_type %s",
    )
    upFieldSmoothing = traits.Float(
        desc="Smoothing sigma for the update field at each iteration",
        argstr="--upFieldSmoothing %f",
    )
    max_step_length = traits.Float(
        desc="Maximum length of an update vector (0: no restriction)",
        argstr="--max_step_length %f",
    )
    use_vanilla_dem = traits.Bool(
        desc="Run vanilla demons algorithm", argstr="--use_vanilla_dem "
    )
    gui = traits.Bool(
        desc="Display intermediate image volumes for debugging", argstr="--gui "
    )
    promptUser = traits.Bool(
        desc="Prompt the user to hit enter each time an image is sent to the DebugImageViewer",
        argstr="--promptUser ",
    )
    numberOfBCHApproximationTerms = traits.Int(
        desc="Number of terms in the BCH expansion",
        argstr="--numberOfBCHApproximationTerms %d",
    )
    numberOfThreads = traits.Int(
        desc="Explicitly specify the maximum number of threads to use.",
        argstr="--numberOfThreads %d",
    )


class VBRAINSDemonWarpOutputSpec(TraitedSpec):
    outputVolume = File(
        desc="Required: output resampled moving image (will have the same physical space as the fixedVolume).",
        exists=True,
    )
    outputDisplacementFieldVolume = File(
        desc="Output deformation field vector image (will have the same physical space as the fixedVolume).",
        exists=True,
    )
    outputCheckerboardVolume = File(
        desc="Genete a checkerboard image volume between the fixedVolume and the deformed movingVolume.",
        exists=True,
    )


class VBRAINSDemonWarp(SEMLikeCommandLine):
    """title: Vector Demon Registration (BRAINS)

category: Registration.Specialized

description: This program finds a deformation field to warp a moving image onto a fixed image.  The images must be of the same signal kind, and contain an image of the same kind of object.  This program uses the Thirion Demons warp software in ITK, the Insight Toolkit.  Additional information is available at: http://www.nitrc.org/projects/brainsdemonwarp.

version: 3.0.0

documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSDemonWarp

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: This tool was developed by Hans J. Johnson and Greg Harris.

acknowledgements: The development of this tool was supported by funding from grants NS050568 and NS40068 from the National Institute of Neurological Disorders and Stroke and grants MH31593, MH40856, from the National Institute of Mental Health.

"""

    input_spec = VBRAINSDemonWarpInputSpec
    output_spec = VBRAINSDemonWarpOutputSpec
    _cmd = " VBRAINSDemonWarp "
    _outputs_filenames = {
        "outputVolume": "outputVolume.nii",
        "outputCheckerboardVolume": "outputCheckerboardVolume.nii",
        "outputDisplacementFieldVolume": "outputDisplacementFieldVolume.nrrd",
    }
    _redirect_x = False


class BRAINSDemonWarpInputSpec(CommandLineInputSpec):
    movingVolume = File(
        desc="Required: input moving image", exists=True, argstr="--movingVolume %s"
    )
    fixedVolume = File(
        desc="Required: input fixed (target) image",
        exists=True,
        argstr="--fixedVolume %s",
    )
    inputPixelType = traits.Enum(
        "float",
        "short",
        "ushort",
        "int",
        "uchar",
        desc="Input volumes will be typecast to this format: float|short|ushort|int|uchar",
        argstr="--inputPixelType %s",
    )
    outputVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Required: output resampled moving image (will have the same physical space as the fixedVolume).",
        argstr="--outputVolume %s",
    )
    outputDisplacementFieldVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Output deformation field vector image (will have the same physical space as the fixedVolume).",
        argstr="--outputDisplacementFieldVolume %s",
    )
    outputPixelType = traits.Enum(
        "float",
        "short",
        "ushort",
        "int",
        "uchar",
        desc="outputVolume will be typecast to this format: float|short|ushort|int|uchar",
        argstr="--outputPixelType %s",
    )
    interpolationMode = traits.Enum(
        "NearestNeighbor",
        "Linear",
        "ResampleInPlace",
        "BSpline",
        "WindowedSinc",
        "Hamming",
        "Cosine",
        "Welch",
        "Lanczos",
        "Blackman",
        desc="Type of interpolation to be used when applying transform to moving volume.  Options are Linear, ResampleInPlace, NearestNeighbor, BSpline, or WindowedSinc",
        argstr="--interpolationMode %s",
    )
    registrationFilterType = traits.Enum(
        "Demons",
        "FastSymmetricForces",
        "Diffeomorphic",
        desc="Registration Filter Type: Demons|FastSymmetricForces|Diffeomorphic",
        argstr="--registrationFilterType %s",
    )
    smoothDisplacementFieldSigma = traits.Float(
        desc="A gaussian smoothing value to be applied to the deformation feild at each iteration.",
        argstr="--smoothDisplacementFieldSigma %f",
    )
    numberOfPyramidLevels = traits.Int(
        desc="Number of image pyramid levels to use in the multi-resolution registration.",
        argstr="--numberOfPyramidLevels %d",
    )
    minimumFixedPyramid = InputMultiPath(
        traits.Int,
        desc="The shrink factor for the first level of the fixed image pyramid. (i.e. start at 1/16 scale, then 1/8, then 1/4, then 1/2, and finally full scale)",
        sep=",",
        argstr="--minimumFixedPyramid %s",
    )
    minimumMovingPyramid = InputMultiPath(
        traits.Int,
        desc="The shrink factor for the first level of the moving image pyramid. (i.e. start at 1/16 scale, then 1/8, then 1/4, then 1/2, and finally full scale)",
        sep=",",
        argstr="--minimumMovingPyramid %s",
    )
    arrayOfPyramidLevelIterations = InputMultiPath(
        traits.Int,
        desc="The number of iterations for each pyramid level",
        sep=",",
        argstr="--arrayOfPyramidLevelIterations %s",
    )
    histogramMatch = traits.Bool(
        desc="Histogram Match the input images.  This is suitable for images of the same modality that may have different absolute scales, but the same overall intensity profile.",
        argstr="--histogramMatch ",
    )
    numberOfHistogramBins = traits.Int(
        desc="The number of histogram levels", argstr="--numberOfHistogramBins %d"
    )
    numberOfMatchPoints = traits.Int(
        desc="The number of match points for histrogramMatch",
        argstr="--numberOfMatchPoints %d",
    )
    medianFilterSize = InputMultiPath(
        traits.Int,
        desc="Median filter radius in all 3 directions.  When images have a lot of salt and pepper noise, this step can improve the registration.",
        sep=",",
        argstr="--medianFilterSize %s",
    )
    initializeWithDisplacementField = File(
        desc="Initial deformation field vector image file name",
        exists=True,
        argstr="--initializeWithDisplacementField %s",
    )
    initializeWithTransform = File(
        desc="Initial Transform filename",
        exists=True,
        argstr="--initializeWithTransform %s",
    )
    maskProcessingMode = traits.Enum(
        "NOMASK",
        "ROIAUTO",
        "ROI",
        "BOBF",
        desc="What mode to use for using the masks: NOMASK|ROIAUTO|ROI|BOBF.  If ROIAUTO is choosen, then the mask is implicitly defined using a otsu forground and hole filling algorithm. Where the Region Of Interest mode uses the masks to define what parts of the image should be used for computing the deformation field.  Brain Only Background Fill uses the masks to pre-process the input images by clipping and filling in the background with a predefined value.",
        argstr="--maskProcessingMode %s",
    )
    fixedBinaryVolume = File(
        desc="Mask filename for desired region of interest in the Fixed image.",
        exists=True,
        argstr="--fixedBinaryVolume %s",
    )
    movingBinaryVolume = File(
        desc="Mask filename for desired region of interest in the Moving image.",
        exists=True,
        argstr="--movingBinaryVolume %s",
    )
    lowerThresholdForBOBF = traits.Int(
        desc="Lower threshold for performing BOBF", argstr="--lowerThresholdForBOBF %d"
    )
    upperThresholdForBOBF = traits.Int(
        desc="Upper threshold for performing BOBF", argstr="--upperThresholdForBOBF %d"
    )
    backgroundFillValue = traits.Int(
        desc="Replacement value to overwrite background when performing BOBF",
        argstr="--backgroundFillValue %d",
    )
    seedForBOBF = InputMultiPath(
        traits.Int,
        desc="coordinates in all 3 directions for Seed when performing BOBF",
        sep=",",
        argstr="--seedForBOBF %s",
    )
    neighborhoodForBOBF = InputMultiPath(
        traits.Int,
        desc="neighborhood in all 3 directions to be included when performing BOBF",
        sep=",",
        argstr="--neighborhoodForBOBF %s",
    )
    outputDisplacementFieldPrefix = traits.Str(
        desc="Displacement field filename prefix for writing separate x, y, and z component images",
        argstr="--outputDisplacementFieldPrefix %s",
    )
    outputCheckerboardVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Genete a checkerboard image volume between the fixedVolume and the deformed movingVolume.",
        argstr="--outputCheckerboardVolume %s",
    )
    checkerboardPatternSubdivisions = InputMultiPath(
        traits.Int,
        desc="Number of Checkerboard subdivisions in all 3 directions",
        sep=",",
        argstr="--checkerboardPatternSubdivisions %s",
    )
    outputNormalized = traits.Bool(
        desc="Flag to warp and write the normalized images to output.  In normalized images the image values are fit-scaled to be between 0 and the maximum storage type value.",
        argstr="--outputNormalized ",
    )
    outputDebug = traits.Bool(
        desc="Flag to write debugging images after each step.", argstr="--outputDebug "
    )
    gradient_type = traits.Enum(
        "0",
        "1",
        "2",
        desc="Type of gradient used for computing the demons force (0 is symmetrized, 1 is fixed image, 2 is moving image)",
        argstr="--gradient_type %s",
    )
    upFieldSmoothing = traits.Float(
        desc="Smoothing sigma for the update field at each iteration",
        argstr="--upFieldSmoothing %f",
    )
    max_step_length = traits.Float(
        desc="Maximum length of an update vector (0: no restriction)",
        argstr="--max_step_length %f",
    )
    use_vanilla_dem = traits.Bool(
        desc="Run vanilla demons algorithm", argstr="--use_vanilla_dem "
    )
    gui = traits.Bool(
        desc="Display intermediate image volumes for debugging", argstr="--gui "
    )
    promptUser = traits.Bool(
        desc="Prompt the user to hit enter each time an image is sent to the DebugImageViewer",
        argstr="--promptUser ",
    )
    numberOfBCHApproximationTerms = traits.Int(
        desc="Number of terms in the BCH expansion",
        argstr="--numberOfBCHApproximationTerms %d",
    )
    numberOfThreads = traits.Int(
        desc="Explicitly specify the maximum number of threads to use.",
        argstr="--numberOfThreads %d",
    )


class BRAINSDemonWarpOutputSpec(TraitedSpec):
    outputVolume = File(
        desc="Required: output resampled moving image (will have the same physical space as the fixedVolume).",
        exists=True,
    )
    outputDisplacementFieldVolume = File(
        desc="Output deformation field vector image (will have the same physical space as the fixedVolume).",
        exists=True,
    )
    outputCheckerboardVolume = File(
        desc="Genete a checkerboard image volume between the fixedVolume and the deformed movingVolume.",
        exists=True,
    )


class BRAINSDemonWarp(SEMLikeCommandLine):
    """title: Demon Registration (BRAINS)

category: Registration.Specialized

description: This program finds a deformation field to warp a moving image onto a fixed image.  The images must be of the same signal kind, and contain an image of the same kind of object.  This program uses the Thirion Demons warp software in ITK, the Insight Toolkit.  Additional information is available at: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSDemonWarp.

version: 3.0.0

documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSDemonWarp

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: This tool was developed by Hans J. Johnson and Greg Harris.

acknowledgements: The development of this tool was supported by funding from grants NS050568 and NS40068 from the National Institute of Neurological Disorders and Stroke and grants MH31593, MH40856, from the National Institute of Mental Health.

"""

    input_spec = BRAINSDemonWarpInputSpec
    output_spec = BRAINSDemonWarpOutputSpec
    _cmd = " BRAINSDemonWarp "
    _outputs_filenames = {
        "outputVolume": "outputVolume.nii",
        "outputCheckerboardVolume": "outputCheckerboardVolume.nii",
        "outputDisplacementFieldVolume": "outputDisplacementFieldVolume.nrrd",
    }
    _redirect_x = False


class BRAINSTransformFromFiducialsInputSpec(CommandLineInputSpec):
    fixedLandmarks = InputMultiPath(
        traits.List(traits.Float(), minlen=3, maxlen=3),
        desc="Ordered list of landmarks in the fixed image",
        argstr="--fixedLandmarks %s...",
    )
    movingLandmarks = InputMultiPath(
        traits.List(traits.Float(), minlen=3, maxlen=3),
        desc="Ordered list of landmarks in the moving image",
        argstr="--movingLandmarks %s...",
    )
    saveTransform = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Save the transform that results from registration",
        argstr="--saveTransform %s",
    )
    transformType = traits.Enum(
        "Translation",
        "Rigid",
        "Similarity",
        desc="Type of transform to produce",
        argstr="--transformType %s",
    )
    fixedLandmarksFile = File(
        desc="An fcsv formatted file with a list of landmark points.",
        exists=True,
        argstr="--fixedLandmarksFile %s",
    )
    movingLandmarksFile = File(
        desc="An fcsv formatted file with a list of landmark points.",
        exists=True,
        argstr="--movingLandmarksFile %s",
    )
    numberOfThreads = traits.Int(
        desc="Explicitly specify the maximum number of threads to use.",
        argstr="--numberOfThreads %d",
    )


class BRAINSTransformFromFiducialsOutputSpec(TraitedSpec):
    saveTransform = File(
        desc="Save the transform that results from registration", exists=True
    )


class BRAINSTransformFromFiducials(SEMLikeCommandLine):
    """title: Fiducial Registration (BRAINS)

category: Registration.Specialized

description: Computes a rigid, similarity or affine transform from a matched list of fiducials

version: 0.1.0.$Revision$

documentation-url: http://www.slicer.org/slicerWiki/index.php/Modules:TransformFromFiducials-Documentation-3.6

contributor: Casey B Goodlett

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = BRAINSTransformFromFiducialsInputSpec
    output_spec = BRAINSTransformFromFiducialsOutputSpec
    _cmd = " BRAINSTransformFromFiducials "
    _outputs_filenames = {"saveTransform": "saveTransform.h5"}
    _redirect_x = False
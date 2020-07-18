# This file is generated by objective.metadata
#
# Last update: Sat Jul 18 14:22:07 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$$"""
enums = """$MPSGraphDeviceTypeMetal@0$MPSGraphLossReductionTypeAxis@0$MPSGraphLossReductionTypeSum@1$MPSGraphOptionsDefault@1$MPSGraphOptionsNone@0$MPSGraphOptionsSynchronizeResults@1$MPSGraphOptionsVerbose@2$MPSGraphPaddingModeConstant@0$MPSGraphPaddingModeReflect@1$MPSGraphPaddingModeSymmetric@2$MPSGraphPaddingStyleExplicit@0$MPSGraphPaddingStyleTF_SAME@2$MPSGraphPaddingStyleTF_VALID@1$MPSGraphResizeBilinear@1$MPSGraphResizeNearest@0$MPSGraphTensorNamedDataLayoutCHW@4$MPSGraphTensorNamedDataLayoutHW@6$MPSGraphTensorNamedDataLayoutHWC@5$MPSGraphTensorNamedDataLayoutHWIO@3$MPSGraphTensorNamedDataLayoutNCHW@0$MPSGraphTensorNamedDataLayoutNHWC@1$MPSGraphTensorNamedDataLayoutOIHW@2$"""
misc.update({})
aliases = {"MPSGraphOptionsDefault": "MPSGraphOptionsSynchronizeResults"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MPSGraph",
        b"resizeTensor:size:mode:centerResult:alignCorners:layout:name:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"setCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"setScheduledHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"MPSGraphExecutionDescriptor",
        b"setWaitUntilCompleted:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MPSGraphExecutionDescriptor", b"waitUntilCompleted", {"retval": {"type": b"Z"}})
    r(b"MPSGraphShapedType", b"isEqualTo:", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE

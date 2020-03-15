# This file is generated by objective.metadata
#
# Last update: Sun Mar 15 12:43:20 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a

misc = {
}
misc.update({'ColorSyncMD5': objc.createStructType('ColorSyncMD5', b'{_ColorSyncMD5=[8C]}', ['digest'])})
constants = '''$kCMMApplyTransformProcName$kCMMCreateTransformPropertyProcName$kCMMInitializeLinkProfileProcName$kCMMInitializeTransformProcName$kColorSyncACESCGLinearProfile$kColorSyncAdobeRGB1998Profile$kColorSyncBestQuality$kColorSyncBlackPointCompensation$kColorSyncCameraDeviceClass$kColorSyncConversion1DLut$kColorSyncConversion3DLut$kColorSyncConversionBPC$kColorSyncConversionChannelID$kColorSyncConversionGridPoints$kColorSyncConversionInpChan$kColorSyncConversionMatrix$kColorSyncConversionNDLut$kColorSyncConversionOutChan$kColorSyncConversionParamCurve0$kColorSyncConversionParamCurve1$kColorSyncConversionParamCurve2$kColorSyncConversionParamCurve3$kColorSyncConversionParamCurve4$kColorSyncConvertQuality$kColorSyncConvertThreadCount$kColorSyncConvertUseExtendedRange$kColorSyncConvertUseVectorUnit$kColorSyncCustomProfiles$kColorSyncDCIP3Profile$kColorSyncDeviceClass$kColorSyncDeviceDefaultProfileID$kColorSyncDeviceDescription$kColorSyncDeviceDescriptions$kColorSyncDeviceHostScope$kColorSyncDeviceID$kColorSyncDeviceModeDescription$kColorSyncDeviceModeDescriptions$kColorSyncDeviceProfileID$kColorSyncDeviceProfileIsCurrent$kColorSyncDeviceProfileIsDefault$kColorSyncDeviceProfileIsFactory$kColorSyncDeviceProfileURL$kColorSyncDeviceProfilesNotification$kColorSyncDeviceRegisteredNotification$kColorSyncDeviceUnregisteredNotification$kColorSyncDeviceUserScope$kColorSyncDisplayDeviceClass$kColorSyncDisplayDeviceProfilesNotification$kColorSyncDisplayP3Profile$kColorSyncDraftQuality$kColorSyncExtendedRange$kColorSyncFactoryProfiles$kColorSyncFixedPointRange$kColorSyncGenericCMYKProfile$kColorSyncGenericGrayGamma22Profile$kColorSyncGenericGrayProfile$kColorSyncGenericLabProfile$kColorSyncGenericRGBProfile$kColorSyncGenericXYZProfile$kColorSyncITUR2020Profile$kColorSyncITUR709Profile$kColorSyncNormalQuality$kColorSyncPreferredCMM$kColorSyncPrinterDeviceClass$kColorSyncProfile$kColorSyncProfileClass$kColorSyncProfileColorSpace$kColorSyncProfileComputerDomain$kColorSyncProfileDescription$kColorSyncProfileHeader$kColorSyncProfileHostScope$kColorSyncProfileMD5Digest$kColorSyncProfilePCS$kColorSyncProfileRepositoryChangeNotification$kColorSyncProfileURL$kColorSyncProfileUserDomain$kColorSyncProfileUserScope$kColorSyncROMMRGBProfile$kColorSyncRegistrationUpdateWindowServer$kColorSyncRenderingIntent$kColorSyncRenderingIntentAbsolute$kColorSyncRenderingIntentPerceptual$kColorSyncRenderingIntentRelative$kColorSyncRenderingIntentSaturation$kColorSyncRenderingIntentUseProfileHeader$kColorSyncSRGBProfile$kColorSyncScannerDeviceClass$kColorSyncSigAToB0Tag$kColorSyncSigAToB1Tag$kColorSyncSigAToB2Tag$kColorSyncSigAbstractClass$kColorSyncSigBToA0Tag$kColorSyncSigBToA1Tag$kColorSyncSigBToA2Tag$kColorSyncSigBlueColorantTag$kColorSyncSigBlueTRCTag$kColorSyncSigCmykData$kColorSyncSigColorSpaceClass$kColorSyncSigCopyrightTag$kColorSyncSigDeviceMfgDescTag$kColorSyncSigDeviceModelDescTag$kColorSyncSigDisplayClass$kColorSyncSigGamutTag$kColorSyncSigGrayData$kColorSyncSigGrayTRCTag$kColorSyncSigGreenColorantTag$kColorSyncSigGreenTRCTag$kColorSyncSigInputClass$kColorSyncSigLabData$kColorSyncSigLinkClass$kColorSyncSigMediaBlackPointTag$kColorSyncSigMediaWhitePointTag$kColorSyncSigNamedColor2Tag$kColorSyncSigNamedColorClass$kColorSyncSigOutputClass$kColorSyncSigPreview0Tag$kColorSyncSigPreview1Tag$kColorSyncSigPreview2Tag$kColorSyncSigProfileDescriptionTag$kColorSyncSigProfileSequenceDescTag$kColorSyncSigRedColorantTag$kColorSyncSigRedTRCTag$kColorSyncSigRgbData$kColorSyncSigTechnologyTag$kColorSyncSigViewingCondDescTag$kColorSyncSigViewingConditionsTag$kColorSyncSigXYZData$kColorSyncTranformInfo$kColorSyncTransformCodeFragmentMD5$kColorSyncTransformCodeFragmentType$kColorSyncTransformCreator$kColorSyncTransformDeviceToDevice$kColorSyncTransformDeviceToPCS$kColorSyncTransformDstSpace$kColorSyncTransformFullConversionData$kColorSyncTransformGamutCheck$kColorSyncTransformInfo$kColorSyncTransformPCSToDevice$kColorSyncTransformPCSToPCS$kColorSyncTransformParametricConversionData$kColorSyncTransformSimplifiedConversionData$kColorSyncTransformSrcSpace$kColorSyncTransformTag$'''
enums = '''$COLORSYNC_MD5_LENGTH@16$kColorSync10BitInteger@8$kColorSync16BitFloat@4$kColorSync16BitInteger@3$kColorSync1BitGamut@1$kColorSync32BitFloat@7$kColorSync32BitInteger@5$kColorSync32BitNamedColorIndex@6$kColorSync8BitInteger@2$kColorSyncAlphaFirst@4$kColorSyncAlphaInfoMask@31$kColorSyncAlphaLast@3$kColorSyncAlphaNone@0$kColorSyncAlphaNoneSkipFirst@6$kColorSyncAlphaNoneSkipLast@5$kColorSyncAlphaPremultipliedFirst@2$kColorSyncAlphaPremultipliedLast@1$kColorSyncByteOrder16Big@12288$kColorSyncByteOrder16Little@4096$kColorSyncByteOrder32Big@16384$kColorSyncByteOrder32Little@8192$kColorSyncByteOrderDefault@0$kColorSyncByteOrderMask@28672$'''
misc.update({'COLORSYNC_PROFILE_INSTALL_ENTITLEMENT': b'com.apple.developer.ColorSync.profile.install'})
functions={'ColorSyncProfileCopyDescriptionString': (b'^{__CFString=}^{ColorSyncProfile=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncCMMCopyLocalizedName': (b'^{__CFString=}^{ColorSyncCMM=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCreateLink': (b'^{ColorSyncProfile=}^{__CFArray=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCreateDisplayTransferTablesFromVCGT': (b'B^{ColorSyncProfile=}n^L', '', {'arguments': {1: {'comment': 'Unclear if this is correct'}}}), 'CGDisplayGetDisplayIDFromUUID': (b'I^{__CFUUID=}',), 'ColorSyncProfileCreateDeviceProfile': (b'^{ColorSyncProfile=}^{__CFString=}^{__CFUUID=}@', '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'comment': 'CFTypeRef'}}}), 'ColorSyncProfileCopyHeader': (b'^{__CFData=}^{ColorSyncProfile=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCopyTagSignatures': (b'^{__CFArray=}^{ColorSyncProfile=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncCMMGetTypeID': (sel32or64(b'I', b'Q'),), 'ColorSyncProfileCreateWithURL': (b'^{ColorSyncProfile=}^{__CFURL=}o^{__CFError=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileVerify': (b'B^{ColorSyncProfile=}o^{__CFError=}o^{__CFError=}',), 'ColorSyncTransformConvert': (b'B^{ColorSyncTransform=}LL^viiL^viiL^{__CFDictionary=}', '', {'arguments': {3: {'type_modifier': 'o', 'c_array_of_variable_length': True}, 7: {'type_modifier': 'n', 'c_array_of_variable_length': True}}}), 'ColorSyncCMMCreate': (b'^{ColorSyncCMM=}^{__CFBundle=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCreateWithDisplayID': (b'^{ColorSyncProfile=}I', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCreateMutableCopy': (b'^{ColorSyncProfile=}^{ColorSyncProfile=}', '', {'retval': {'already_cfretained': True}}), 'CGDisplayCreateUUIDFromDisplayID': (b'^{__CFUUID=}I', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileInstall': (b'B^{ColorSyncProfile=}^{__CFString=}^{__CFString=}o^^{__CFError=}',), 'ColorSyncProfileSetTag': (b'v^{ColorSyncProfile=}^{__CFString=}^{__CFData=}',), 'ColorSyncTransformCreate': (b'^{ColorSyncTransform=}^{__CFArray=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCopyTag': (b'^{__CFData=}^{ColorSyncProfile=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncIterateDeviceProfiles': (b'v^?^v', '', {'arguments': {0: {'callable': {'retval': {'type': b'B'}, 'arguments': {0: {'type': b'^{__CFDictionary=}'}, 1: {'type': b'^v'}}}, 'callable_retained': False}}}), 'ColorSyncProfileGetURL': (b'^{__CFData=}^{ColorSyncProfile=}o^{__CFError=}',), 'ColorSyncTransformSetProperty': (b'v^{ColorSyncTransform=}@@',), 'ColorSyncUnregisterDevice': (b'B^{__CFString=}^{__CFUUID=}',), 'ColorSyncDeviceCopyDeviceInfo': (b'^{__CFDictionary=}^{__CFString=}^{__CFUUID=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileCreateMutable': (b'^{ColorSyncProfile=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncIterateInstalledProfiles': (b'v^?N^I^v^^{__CFError=}', '', {'arguments': {0: {'callable': {'retval': {'type': b'B'}, 'arguments': {0: {'type': b'^{__CFDictionary=}'}, 1: {'type': b'^v'}}}, 'callable_retained': False}, 3: {'type_modifier': 'o'}}}), 'ColorSyncProfileUninstall': (b'B^{ColorSyncProfile=}o^^{__CFError=}',), 'ColorSyncProfileCopyData': (b'^{__CFData=}^{ColorSyncProfile=}o^{__CFError=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncIterateInstalledCMMs': (b'v^?^v', '', {'arguments': {0: {'callable': {'retval': {'type': b'B'}, 'arguments': {0: {'type': b'^{ColorSyncCMM=}'}, 1: {'type': b'^v'}}}, 'callable_retained': False}}}), 'ColorSyncCMMGetBundle': (b'^{__CFBundle=}^{ColorSyncCMM=}',), 'ColorSyncProfileGetTypeID': (sel32or64(b'I', b'Q'),), 'ColorSyncProfileCreateWithName': (b'^{ColorSyncProfile=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncTransformGetTypeID': (sel32or64(b'I', b'Q'),), 'ColorSyncProfileGetDisplayTransferFormulaFromVCGT': (b'B^{ColorSyncProfile=}o^fo^fo^fo^fo^fo^fo^fo^fo^f',), 'ColorSyncRegisterDevice': (b'B^{__CFString=}^{__CFUUID=}^{__CFDictionary=}',), 'ColorSyncProfileEstimateGammaWithDisplayID': (b'fIo^{__CFError=}',), 'ColorSyncProfileGetMD5': (b'{_ColorSyncMD5=[8C]}^{ColorSyncProfile=}',), 'ColorSyncProfileRemoveTag': (b'v^{ColorSyncProfile=}^{__CFString=}',), 'ColorSyncProfileContainsTag': (b'^{__CFData=}^{ColorSyncProfile=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileEstimateGamma': (b'f^{ColorSyncProfile=}o^{__CFError=}',), 'ColorSyncProfileCreate': (b'^{ColorSyncProfile=}^{__CFData=}o^{__CFError=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncProfileSetHeader': (b'v^{ColorSyncProfile=}^{__CFData=}',), 'ColorSyncTransformCopyProperty': (b'@^{ColorSyncTransform=}@^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'ColorSyncCMMCopyCMMIdentifier': (b'^{__CFString=}^{ColorSyncCMM=}', '', {'retval': {'already_cfretained': True}})}
aliases = {'ColorSyncMutableProfileRef': 'ColorSyncProfileRef'}
cftypes=[('ColorSyncCMMRef', b'^{ColorSyncCMM=}', 'ColorSyncCMMGetTypeID', None), ('ColorSyncProfileRef', b'^{ColorSyncProfile=}', 'ColorSyncProfileGetTypeID', None), ('ColorSyncTransformRef', b'^{ColorSyncTransform=}', 'ColorSyncTransformGetTypeID', None)]
expressions = {}

# END OF FILE

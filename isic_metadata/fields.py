from __future__ import annotations

from enum import Enum
import re
from typing import Any

from isic_metadata.diagnosis_hierarchical import DiagnosisEnum  # noqa: F401


class ClinSizeLongDiamMm:
    @classmethod
    def parse_measurement_str(cls, value: Any) -> Any:
        if isinstance(value, str):
            match = re.match(r"(.+)(um|mm|cm)$", value)

            if not match:
                return value

            float_value, units = match.groups()
            float_value = float(float_value)

            # Convert to mm
            if units == "um":
                float_value *= 1e-3
            elif units == "cm":
                float_value *= 1e1

            return round(float_value, ndigits=1)

        return value


class Age:
    @classmethod
    def handle_85plus(cls, value: Any) -> Any:
        if value == "85+":
            return 85

        return value

    @staticmethod
    def clamp_upper_bound(value: int) -> int:
        return min(value, 85)


class DiagnosisConfirmTypeEnum(str, Enum):
    histopathology = "histopathology"
    serial_imaging_showing_no_change = "serial imaging showing no change"
    single_image_expert_consensus = "single image expert consensus"
    confocal_microscopy_with_consensus_dermoscopy = "confocal microscopy with consensus dermoscopy"
    single_contributor_clinical_assessment = "single contributor clinical assessment"


class LegacyDxEnum(str, Enum):
    actinic_keratosis = "actinic keratosis"
    adnexal_tumor = "adnexal tumor"
    aimp = "AIMP"
    angiokeratoma = "angiokeratoma"
    angioma = "angioma"
    basal_cell_carcinoma = "basal cell carcinoma"
    cafe_au_lait_macule = "cafe-au-lait macule"
    dermatofibroma = "dermatofibroma"
    ephelis = "ephelis"
    lentigo_nos = "lentigo NOS"
    lentigo_simplex = "lentigo simplex"
    lichenoid_keratosis = "lichenoid keratosis"
    melanoma = "melanoma"
    melanoma_metastasis = "melanoma metastasis"
    merkel_cell_carcinoma = "merkel cell carcinoma"
    mucosal_melanosis = "mucosal melanosis"
    nevus = "nevus"
    nevus_spilus = "nevus spilus"
    seborrheic_keratosis = "seborrheic keratosis"
    solar_lentigo = "solar lentigo"
    squamous_cell_carcinoma = "squamous cell carcinoma"
    clear_cell_acanthoma = "clear cell acanthoma"
    atypical_spitz_tumor = "atypical spitz tumor"
    acrochordon = "acrochordon"
    angiofibroma_or_fibrous_papule = "angiofibroma or fibrous papule"
    neurofibroma = "neurofibroma"
    pyogenic_granuloma = "pyogenic granuloma"
    scar = "scar"
    sebaceous_adenoma = "sebaceous adenoma"
    sebaceous_hyperplasia = "sebaceous hyperplasia"
    verruca = "verruca"
    atypical_melanocytic_proliferation = "atypical melanocytic proliferation"
    epidermal_nevus = "epidermal nevus"
    pigmented_benign_keratosis = "pigmented benign keratosis"
    vascular_lesion = "vascular lesion"
    other = "other"


class ImageTypeEnum(str, Enum):
    dermoscopic = "dermoscopic"
    clinical_overview = "clinical: overview"
    clinical_close_up = "clinical: close-up"
    tbp_tile_close_up = "TBP tile: close-up"
    tbp_tile_overview = "TBP tile: overview"
    # Note that RCM types need to be added to validate_rcm_fields
    rcm_macroscopic = "RCM: macroscopic"
    rcm_tile = "RCM: tile"
    rcm_mosaic = "RCM: mosaic"


class DermoscopicTypeEnum(str, Enum):
    contact_polarized = "contact polarized"
    contact_non_polarized = "contact non-polarized"
    non_contact_polarized = "non-contact polarized"


class TBPTileTypeEnum(str, Enum):
    tbp_3d_white = "3D: white"
    tbp_3d_xp = "3D: XP"
    tbp_2d = "2D"


class MelThickMm:
    _regex = re.compile(r"^([\d.]+)(\s+)?(mm)?$")

    @classmethod
    def parse_measurement_str(cls, value: Any) -> Any:
        if isinstance(value, str):
            result = re.match(MelThickMm._regex, value)

            if not result:
                return value

            value = result.group(1)

            return float(value)

        return value


class MelMitoticIndexEnum(str, Enum):
    zero = "0/mm^2"
    lt_one = "<1/mm^2"
    one = "1/mm^2"
    two = "2/mm^2"
    three = "3/mm^2"
    four = "4/mm^2"
    gt_4 = ">4/mm^2"


class AnatomSiteGeneralEnum(str, Enum):
    head_neck = "head/neck"
    upper_extremity = "upper extremity"
    lower_extremity = "lower extremity"
    anterior_torso = "anterior torso"
    posterior_torso = "posterior torso"
    palms_soles = "palms/soles"
    lateral_torso = "lateral torso"
    oral_genital = "oral/genital"


class AnatomSiteSpecialEnum(str, Enum):
    acral_nos = "acral NOS"
    nail_nos = "nail NOS"
    fingernail = "fingernail"
    toenail = "toenail"
    acral_palms_soles = "acral palms or soles"
    oral_genital = "oral or genital"


class ColorTintEnum(str, Enum):
    blue = "blue"
    pink = "pink"
    none = "none"


class FitzpatrickSkinType(str, Enum):
    type_i = "I"
    type_ii = "II"
    type_iii = "III"
    type_iv = "IV"
    type_v = "V"
    type_vi = "VI"


class ImageManipulationEnum(str, Enum):
    instrument_only = "instrument only"
    altered = "altered"
    synthetic = "synthetic"

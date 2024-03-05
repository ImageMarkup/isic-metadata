from __future__ import annotations

from enum import Enum
import re
from typing import Any


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


# todo indeterminable
class BenignMalignantEnum(str, Enum):
    benign = "benign"
    malignant = "malignant"
    indeterminate = "indeterminate"
    indeterminate_benign = "indeterminate/benign"
    indeterminate_malignant = "indeterminate/malignant"


class DiagnosisConfirmTypeEnum(str, Enum):
    histopathology = "histopathology"
    serial_imaging_showing_no_change = "serial imaging showing no change"
    single_image_expert_consensus = "single image expert consensus"
    confocal_microscopy_with_consensus_dermoscopy = "confocal microscopy with consensus dermoscopy"


class DiagnosisEnum(str, Enum):
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


class NevusTypeEnum(str, Enum):
    blue = "blue"
    combined = "combined"
    nevus_nos = "nevus NOS"
    deep_penetrating = "deep penetrating"
    halo = "halo"
    persistent_recurrent = "persistent/recurrent"
    pigmented_spindle_cell_of_reed = "pigmented spindle cell of reed"
    plexiform_spindle_cell = "plexiform spindle cell"
    special_site = "special site"
    spitz = "spitz"


class ImageTypeEnum(str, Enum):
    dermoscopic = "dermoscopic"
    clinical_close_up = "clinical: close-up"
    clinical_overview = "clinical: overview"
    tbp_tile_close_up = "TBP tile: close-up"
    tbp_tile_overview = "TBP tile: overview"


class DermoscopicTypeEnum(str, Enum):
    contact_polarized = "contact polarized"
    contact_non_polarized = "contact non-polarized"
    non_contact_polarized = "non-contact polarized"


class TBPTileTypeEnum(str, Enum):
    tbp_3d_white = "3D: white"
    tbp_3d_xp = "3D: XP"
    tbp_2d = "2D"


class MelTypeEnum(str, Enum):
    superficial_spreading_melanoma = "superficial spreading melanoma"
    nodular_melanoma = "nodular melanoma"
    lentigo_maligna_melanoma = "lentigo maligna melanoma"
    acral_lentiginous_melanoma = "acral lentiginous melanoma"
    melanoma_nos = "melanoma NOS"


class MelClassEnum(str, Enum):
    melanoma_in_situ = "melanoma in situ"
    invasive_melanoma = "invasive melanoma"
    recurrent_persistent_melanoma_in_situ = "recurrent/persistent melanoma, in situ"
    recurrent_persistent_melanoma_invasive = "recurrent/persistent melanoma, invasive"
    melanoma_nos = "melanoma NOS"


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

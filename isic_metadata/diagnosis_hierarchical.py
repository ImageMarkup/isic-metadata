from __future__ import annotations

from enum import Enum
from functools import cache
from typing import Any

# ruff: noqa: E501


class DiagnosisEnum(str, Enum):
    benign = "Benign"
    indeterminate = "Indeterminate"
    malignant = "Malignant"
    benign_benign_other = "Benign:Benign - Other"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular = (
        "Benign:Benign adnexal epithelial proliferations - Follicular"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous"
    )
    benign_benign_epidermal_proliferations = "Benign:Benign epidermal proliferations"
    benign_benign_melanocytic_proliferations = "Benign:Benign melanocytic proliferations"
    benign_benign_soft_tissue_proliferations_adipocytic = (
        "Benign:Benign soft tissue proliferations - Adipocytic"
    )
    benign_benign_soft_tissue_proliferations_cartilagenous_and_ossifying = (
        "Benign:Benign soft tissue proliferations - Cartilagenous and ossifying"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic"
    )
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic = (
        "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic"
    )
    benign_benign_soft_tissue_proliferations_myoepithelial = (
        "Benign:Benign soft tissue proliferations - Myoepithelial"
    )
    benign_benign_soft_tissue_proliferations_neural = (
        "Benign:Benign soft tissue proliferations - Neural"
    )
    benign_benign_soft_tissue_proliferations_vascular = (
        "Benign:Benign soft tissue proliferations - Vascular"
    )
    benign_collision_only_benign_proliferations = "Benign:Collision - Only benign proliferations"
    benign_cysts = "Benign:Cysts"
    benign_exogenous = "Benign:Exogenous"
    benign_flat_melanotic_pigmentations_not_melanocytic_nevus = (
        "Benign:Flat melanotic pigmentations - not melanocytic nevus"
    )
    benign_hemorrhagic_lesions = "Benign:Hemorrhagic lesions"
    benign_inflammatory_or_infectious_diseases = "Benign:Inflammatory or infectious diseases"
    benign_langerhans_cell_proliferations = "Benign:Langerhans cell proliferations"
    benign_mast_cell_proliferations = "Benign:Mast cell proliferations"
    indeterminate_indeterminate_epidermal_proliferations = (
        "Indeterminate:Indeterminate epidermal proliferations"
    )
    indeterminate_indeterminate_melanocytic_proliferations = (
        "Indeterminate:Indeterminate melanocytic proliferations"
    )
    malignant_collision_at_least_one_malignant_proliferation = (
        "Malignant:Collision - At least one malignant proliferation"
    )
    malignant_lymphocytic_proliferations_b_cell = "Malignant:Lymphocytic proliferations - B-Cell"
    malignant_lymphocytic_proliferations_t_cellnk = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK"
    )
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine = (
        "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine"
    )
    malignant_malignant_adnexal_epithelial_proliferations_follicular = (
        "Malignant:Malignant adnexal epithelial proliferations - Follicular"
    )
    malignant_malignant_adnexal_epithelial_proliferations_sebaceous = (
        "Malignant:Malignant adnexal epithelial proliferations - Sebaceous"
    )
    malignant_malignant_epidermal_proliferations = "Malignant:Malignant epidermal proliferations"
    malignant_malignant_melanocytic_proliferations_melanoma = (
        "Malignant:Malignant melanocytic proliferations (Melanoma)"
    )
    malignant_malignant_soft_tissue_proliferations_adipocytic = (
        "Malignant:Malignant soft tissue proliferations - Adipocytic"
    )
    malignant_malignant_soft_tissue_proliferations_cartilagenous_and_ossifying = (
        "Malignant:Malignant soft tissue proliferations - Cartilagenous and ossifying"
    )
    malignant_malignant_soft_tissue_proliferations_fibro_histiocytic = (
        "Malignant:Malignant soft tissue proliferations - Fibro-histiocytic"
    )
    malignant_malignant_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic = (
        "Malignant:Malignant soft tissue proliferations - Muscle tissue or myofibroblastic"
    )
    malignant_malignant_soft_tissue_proliferations_myoepithelial = (
        "Malignant:Malignant soft tissue proliferations - Myoepithelial"
    )
    malignant_malignant_soft_tissue_proliferations_neural = (
        "Malignant:Malignant soft tissue proliferations - Neural"
    )
    malignant_malignant_soft_tissue_proliferations_unknown_or_other_histiogenesis = (
        "Malignant:Malignant soft tissue proliferations - Unknown or other histiogenesis"
    )
    malignant_malignant_soft_tissue_proliferations_vascular = (
        "Malignant:Malignant soft tissue proliferations - Vascular"
    )
    malignant_merkel_cell_proliferation = "Malignant:Merkel cell proliferation"
    malignant_skin_metastasis_of_internal_solid_cancer_non_hematological = (
        "Malignant:Skin metastasis of internal solid cancer - non-hematological"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_apocrine_tubular_adenoma = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Apocrine tubular adenoma"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_cylindoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Cylindoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_cystadenoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Cystadenoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_fibroadenoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Fibroadenoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_hidradenoma_papilliferum = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Hidradenoma papilliferum"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_hidradenoma_apocrine = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Hidradenoma, Apocrine"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_hidradenoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Hidradenoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_mixed_tumor = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Mixed tumor"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_poroma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Poroma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_spiradenoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Spiradenoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_supernumerary_nipple = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Supernumerary nipple"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_syringocystadenoma_papilliferum = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Syringocystadenoma papilliferum"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_syringofibroadenoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Syringofibroadenoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_syringoma = (
        "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Syringoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_folliculosebaceous_cystic_hamartoma = "Benign:Benign adnexal epithelial proliferations - Follicular:Folliculosebaceous cystic hamartoma"
    benign_benign_adnexal_epithelial_proliferations_follicular_nevus_comedonicus = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Nevus comedonicus"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_panfolliculoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Panfolliculoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_pilar_sheath_acanthoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Pilar sheath acanthoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_pilomatricoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Pilomatricoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_proliferating_tricholemmal_tumor = "Benign:Benign adnexal epithelial proliferations - Follicular:Proliferating tricholemmal tumor"
    benign_benign_adnexal_epithelial_proliferations_follicular_trichoblastoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Trichoblastoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_trichoepithelioma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Trichoepithelioma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_trichofolliculoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Trichofolliculoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_tricholemmoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Tricholemmoma"
    )
    benign_benign_adnexal_epithelial_proliferations_follicular_tumor_of_follicular_infundibulum = "Benign:Benign adnexal epithelial proliferations - Follicular:Tumor of follicular infundibulum"
    benign_benign_adnexal_epithelial_proliferations_follicular_warty_dyskeratoma = (
        "Benign:Benign adnexal epithelial proliferations - Follicular:Warty dyskeratoma"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_fibrofolliculoma = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Fibrofolliculoma"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_fordyce_spots = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Fordyce spots"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_nevus_sebaceus = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Nevus sebaceus"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_sebaceoma = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Sebaceoma"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_sebaceous_adenoma = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Sebaceous adenoma"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_sebaceous_hyperplasia = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Sebaceous hyperplasia"
    )
    benign_benign_adnexal_epithelial_proliferations_sebaceous_trichodiscoma = (
        "Benign:Benign adnexal epithelial proliferations - Sebaceous:Trichodiscoma"
    )
    benign_benign_epidermal_proliferations_acantholytic_acanthoma = (
        "Benign:Benign epidermal proliferations:Acantholytic acanthoma"
    )
    benign_benign_epidermal_proliferations_clear_cell_acanthoma = (
        "Benign:Benign epidermal proliferations:Clear cell acanthoma"
    )
    benign_benign_epidermal_proliferations_epidermal_nevus = (
        "Benign:Benign epidermal proliferations:Epidermal nevus"
    )
    benign_benign_epidermal_proliferations_epidermolytic_acanthoma = (
        "Benign:Benign epidermal proliferations:Epidermolytic acanthoma"
    )
    benign_benign_epidermal_proliferations_large_cell_acanthoma = (
        "Benign:Benign epidermal proliferations:Large cell acanthoma"
    )
    benign_benign_epidermal_proliferations_lichen_planus_like_keratosis = (
        "Benign:Benign epidermal proliferations:Lichen planus like keratosis"
    )
    benign_benign_epidermal_proliferations_melanoacanthoma = (
        "Benign:Benign epidermal proliferations:Melanoacanthoma"
    )
    benign_benign_epidermal_proliferations_pigmented_benign_keratosis = (
        "Benign:Benign epidermal proliferations:Pigmented benign keratosis"
    )
    benign_benign_epidermal_proliferations_porokeratosis = (
        "Benign:Benign epidermal proliferations:Porokeratosis"
    )
    benign_benign_epidermal_proliferations_seborrheic_keratosis = (
        "Benign:Benign epidermal proliferations:Seborrheic keratosis"
    )
    benign_benign_epidermal_proliferations_solar_lentigo = (
        "Benign:Benign epidermal proliferations:Solar lentigo"
    )
    benign_benign_melanocytic_proliferations_nevus = (
        "Benign:Benign melanocytic proliferations:Nevus"
    )
    benign_benign_melanocytic_proliferations_dermal_melanocytosis = (
        "Benign:Benign melanocytic proliferations:Dermal melanocytosis"
    )
    benign_benign_melanocytic_proliferations_lentiginous_melanocytic_proliferation = (
        "Benign:Benign melanocytic proliferations:Lentiginous melanocytic proliferation"
    )
    benign_benign_melanocytic_proliferations_lentigo_simplex = (
        "Benign:Benign melanocytic proliferations:Lentigo simplex"
    )
    benign_benign_melanocytic_proliferations_pigmented_epithelioid_melanocytoma = (
        "Benign:Benign melanocytic proliferations:Pigmented epithelioid melanocytoma"
    )
    benign_benign_melanocytic_proliferations_proliferative_nodule_in_congenital_melanocytic_nevi_without_atypia = "Benign:Benign melanocytic proliferations:Proliferative nodule in congenital melanocytic nevi without atypia"
    benign_benign_soft_tissue_proliferations_adipocytic_angiolipoma = (
        "Benign:Benign soft tissue proliferations - Adipocytic:Angiolipoma"
    )
    benign_benign_soft_tissue_proliferations_adipocytic_fibrolipoma = (
        "Benign:Benign soft tissue proliferations - Adipocytic:Fibrolipoma"
    )
    benign_benign_soft_tissue_proliferations_adipocytic_lipoma = (
        "Benign:Benign soft tissue proliferations - Adipocytic:Lipoma"
    )
    benign_benign_soft_tissue_proliferations_adipocytic_lipomatous_nevus = (
        "Benign:Benign soft tissue proliferations - Adipocytic:Lipomatous nevus"
    )
    benign_benign_soft_tissue_proliferations_cartilagenous_and_ossifying_accessory_tragus = (
        "Benign:Benign soft tissue proliferations - Cartilagenous and ossifying:Accessory tragus"
    )
    benign_benign_soft_tissue_proliferations_cartilagenous_and_ossifying_extraskeletal_chondroma = "Benign:Benign soft tissue proliferations - Cartilagenous and ossifying:Extraskeletal chondroma"
    benign_benign_soft_tissue_proliferations_cartilagenous_and_ossifying_osteoma_cutis = (
        "Benign:Benign soft tissue proliferations - Cartilagenous and ossifying:Osteoma cutis"
    )
    benign_benign_soft_tissue_proliferations_cartilagenous_and_ossifying_subungual_osteochodroma = "Benign:Benign soft tissue proliferations - Cartilagenous and ossifying:Subungual osteochodroma"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_angiofibroma = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Angiofibroma"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_dermatofibroma = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Dermatofibroma"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_fibroepithelial_polyp = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Fibroepithelial polyp"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_fibroma = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Fibroma"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_giant_cell_tumor_of_the_tendon_sheath = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Giant cell tumor of the tendon sheath"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_juvenile_xanthogranuloma = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Juvenile xanthogranuloma"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_cutaneous_myxoma = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Cutaneous Myxoma"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_non_langerhans_histiocytosis = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Non-Langerhans histiocytosis"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_reticulohistiocytosis = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Reticulohistiocytosis"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_rosai_dorfman_disease = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Rosai-Dorfman disease"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_scar = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Scar"
    )
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_angioleiomyoma = (
        "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic:Angioleiomyoma"
    )
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_dartoic_muscle_leiomyoma = "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic:Dartoic muscle leiomyoma"
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_dermatomyofibroma = "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic:Dermatomyofibroma"
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_nodular_fasciitis = "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic:Nodular Fasciitis"
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_piloleiomyoma = (
        "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic:Piloleiomyoma"
    )
    benign_benign_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_smooth_muscle_hamartoma = "Benign:Benign soft tissue proliferations - Muscle tissue or myofibroblastic:Smooth muscle hamartoma"
    benign_benign_soft_tissue_proliferations_myoepithelial_myoepithelioma = (
        "Benign:Benign soft tissue proliferations - Myoepithelial:Myoepithelioma"
    )
    benign_benign_soft_tissue_proliferations_neural_granular_cell_tumor = (
        "Benign:Benign soft tissue proliferations - Neural:Granular cell tumor"
    )
    benign_benign_soft_tissue_proliferations_neural_nerve_sheath_myxoma = (
        "Benign:Benign soft tissue proliferations - Neural:Nerve sheath myxoma"
    )
    benign_benign_soft_tissue_proliferations_neural_neurofibroma = (
        "Benign:Benign soft tissue proliferations - Neural:Neurofibroma"
    )
    benign_benign_soft_tissue_proliferations_neural_plexiform_neurofibroma = (
        "Benign:Benign soft tissue proliferations - Neural:Plexiform Neurofibroma"
    )
    benign_benign_soft_tissue_proliferations_neural_neuroma = (
        "Benign:Benign soft tissue proliferations - Neural:Neuroma"
    )
    benign_benign_soft_tissue_proliferations_neural_perineurioma = (
        "Benign:Benign soft tissue proliferations - Neural:Perineurioma"
    )
    benign_benign_soft_tissue_proliferations_neural_schwannoma = (
        "Benign:Benign soft tissue proliferations - Neural:Schwannoma"
    )
    benign_benign_soft_tissue_proliferations_vascular_acquired_elastotic_hemangioma = (
        "Benign:Benign soft tissue proliferations - Vascular:Acquired elastotic hemangioma"
    )
    benign_benign_soft_tissue_proliferations_vascular_acroangiodermatitis_of_mali = (
        "Benign:Benign soft tissue proliferations - Vascular:Acroangiodermatitis of Mali"
    )
    benign_benign_soft_tissue_proliferations_vascular_angiokeratoma = (
        "Benign:Benign soft tissue proliferations - Vascular:Angiokeratoma"
    )
    benign_benign_soft_tissue_proliferations_vascular_angiolymphoid_hyperplasia_with_eosinophilia = "Benign:Benign soft tissue proliferations - Vascular:Angiolymphoid hyperplasia with eosinophilia"
    benign_benign_soft_tissue_proliferations_vascular_arterio_venous_malformation = (
        "Benign:Benign soft tissue proliferations - Vascular:Arterio-venous malformation"
    )
    benign_benign_soft_tissue_proliferations_vascular_capillary_vascular_malformation = (
        "Benign:Benign soft tissue proliferations - Vascular:Capillary vascular malformation"
    )
    benign_benign_soft_tissue_proliferations_vascular_glomangiomyoma = (
        "Benign:Benign soft tissue proliferations - Vascular:Glomangiomyoma"
    )
    benign_benign_soft_tissue_proliferations_vascular_glomeruloid_hemangioma = (
        "Benign:Benign soft tissue proliferations - Vascular:Glomeruloid hemangioma"
    )
    benign_benign_soft_tissue_proliferations_vascular_glomus_tumor = (
        "Benign:Benign soft tissue proliferations - Vascular:Glomus tumor"
    )
    benign_benign_soft_tissue_proliferations_vascular_hemangioma = (
        "Benign:Benign soft tissue proliferations - Vascular:Hemangioma"
    )
    benign_benign_soft_tissue_proliferations_vascular_lymphangioma = (
        "Benign:Benign soft tissue proliferations - Vascular:Lymphangioma"
    )
    benign_benign_soft_tissue_proliferations_vascular_nevus_anemicus = (
        "Benign:Benign soft tissue proliferations - Vascular:Nevus anemicus"
    )
    benign_benign_soft_tissue_proliferations_vascular_noninvoluting_congenital_hemangioma = (
        "Benign:Benign soft tissue proliferations - Vascular:Noninvoluting congenital hemangioma"
    )
    benign_benign_soft_tissue_proliferations_vascular_other_vascular_or_lymphatic_malformation_or_hamartoma = "Benign:Benign soft tissue proliferations - Vascular:Other vascular or lymphatic malformation or hamartoma"
    benign_benign_soft_tissue_proliferations_vascular_pyogenic_granuloma = (
        "Benign:Benign soft tissue proliferations - Vascular:Pyogenic granuloma"
    )
    benign_benign_soft_tissue_proliferations_vascular_rapidly_involuting_congenital_hemangioma = "Benign:Benign soft tissue proliferations - Vascular:Rapidly involuting congenital hemangioma"
    benign_benign_soft_tissue_proliferations_vascular_telangiectasia = (
        "Benign:Benign soft tissue proliferations - Vascular:Telangiectasia"
    )
    benign_benign_soft_tissue_proliferations_vascular_vascular_spider = (
        "Benign:Benign soft tissue proliferations - Vascular:Vascular spider"
    )
    benign_benign_soft_tissue_proliferations_vascular_venous_lake = (
        "Benign:Benign soft tissue proliferations - Vascular:Venous lake"
    )
    benign_benign_soft_tissue_proliferations_vascular_venous_malformation = (
        "Benign:Benign soft tissue proliferations - Vascular:Venous malformation"
    )
    benign_benign_soft_tissue_proliferations_vascular_verrucous_hemangioma = (
        "Benign:Benign soft tissue proliferations - Vascular:Verrucous hemangioma"
    )
    benign_cysts_comedo = "Benign:Cysts:Comedo"
    benign_cysts_digital_mucous_cyst = "Benign:Cysts:Digital mucous cyst"
    benign_cysts_dilated_pore = "Benign:Cysts:Dilated pore"
    benign_cysts_infundibular_or_epidermal_cyst = "Benign:Cysts:Infundibular or epidermal cyst"
    benign_cysts_sebaceous_cyst = "Benign:Cysts:Sebaceous cyst"
    benign_cysts_keratinous_cyst = "Benign:Cysts:Keratinous cyst"
    benign_cysts_milium = "Benign:Cysts:Milium"
    benign_cysts_steatocystoma = "Benign:Cysts:Steatocystoma"
    benign_cysts_trichilemmal_or_isthmic_catagen_or_pilar_cyst = (
        "Benign:Cysts:Trichilemmal or isthmic-catagen or pilar cyst"
    )
    benign_exogenous_foreign_body_granuloma = "Benign:Exogenous:Foreign body granuloma"
    benign_exogenous_tattoo = "Benign:Exogenous:Tattoo"
    benign_flat_melanotic_pigmentations_not_melanocytic_nevus_cafe_au_lait_macule_or_patch = (
        "Benign:Flat melanotic pigmentations - not melanocytic nevus:Cafe au lait macule or patch"
    )
    benign_flat_melanotic_pigmentations_not_melanocytic_nevus_ephelis = (
        "Benign:Flat melanotic pigmentations - not melanocytic nevus:Ephelis"
    )
    benign_flat_melanotic_pigmentations_not_melanocytic_nevus_ink_spot_lentigo = (
        "Benign:Flat melanotic pigmentations - not melanocytic nevus:Ink-spot lentigo"
    )
    benign_flat_melanotic_pigmentations_not_melanocytic_nevus_lentigo_nos = (
        "Benign:Flat melanotic pigmentations - not melanocytic nevus:Lentigo NOS"
    )
    benign_flat_melanotic_pigmentations_not_melanocytic_nevus_mucosal_melanotic_macule = (
        "Benign:Flat melanotic pigmentations - not melanocytic nevus:Mucosal melanotic macule"
    )
    benign_hemorrhagic_lesions_hemorrhage = "Benign:Hemorrhagic lesions:Hemorrhage"
    benign_inflammatory_or_infectious_diseases_verruca = (
        "Benign:Inflammatory or infectious diseases:Verruca"
    )
    benign_inflammatory_or_infectious_diseases_molluscum = (
        "Benign:Inflammatory or infectious diseases:Molluscum"
    )
    benign_langerhans_cell_proliferations_erdheim_chester_disease = (
        "Benign:Langerhans cell proliferations:Erdheim Chester disease"
    )
    benign_langerhans_cell_proliferations_indeterminate_cell_histiocytosis = (
        "Benign:Langerhans cell proliferations:Indeterminate cell histiocytosis"
    )
    benign_langerhans_cell_proliferations_langerhans_cell_histiocytosis = (
        "Benign:Langerhans cell proliferations:Langerhans cell histiocytosis"
    )
    benign_langerhans_cell_proliferations_mixed_langerhans_cell_histiocytosis_and_erdheim_chester_disease = "Benign:Langerhans cell proliferations:Mixed Langerhans cell histiocytosis and Erdheim Chester disease"
    benign_mast_cell_proliferations_maculopapular_mastocytoma = (
        "Benign:Mast cell proliferations:Maculopapular mastocytoma"
    )
    benign_mast_cell_proliferations_mastocytoma_solitary_or_unifocal = (
        "Benign:Mast cell proliferations:Mastocytoma, Solitary or unifocal"
    )
    benign_mast_cell_proliferations_mastocytosis = "Benign:Mast cell proliferations:Mastocytosis"
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_cheilitis = (
        "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic cheilitis"
    )
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_keratosis = (
        "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic keratosis"
    )
    indeterminate_indeterminate_melanocytic_proliferations_atypical_spitz_tumor = (
        "Indeterminate:Indeterminate melanocytic proliferations:Atypical Spitz tumor"
    )
    indeterminate_indeterminate_melanocytic_proliferations_atypical_intraepithelial_melanocytic_proliferation = "Indeterminate:Indeterminate melanocytic proliferations:Atypical intraepithelial melanocytic proliferation"
    indeterminate_indeterminate_melanocytic_proliferations_atypical_melanocytic_neoplasm = (
        "Indeterminate:Indeterminate melanocytic proliferations:Atypical melanocytic neoplasm"
    )
    indeterminate_indeterminate_melanocytic_proliferations_atypical_pigmented_spindle_cell_tumor = "Indeterminate:Indeterminate melanocytic proliferations:Atypical pigmented spindle cell tumor"
    indeterminate_indeterminate_melanocytic_proliferations_atypical_proliferative_nodules_in_congenital_melanocytic_nevus = "Indeterminate:Indeterminate melanocytic proliferations:Atypical proliferative nodules in congenital melanocytic nevus"
    indeterminate_indeterminate_melanocytic_proliferations_melanocytic_tumor_of_uncertain_malignant_potential = "Indeterminate:Indeterminate melanocytic proliferations:Melanocytic tumor of uncertain malignant potential"
    indeterminate_indeterminate_melanocytic_proliferations_superficial_atypical_melanocytic_proliferation_of_uncertain_significance = "Indeterminate:Indeterminate melanocytic proliferations:Superficial atypical melanocytic proliferation of uncertain significance"
    malignant_lymphocytic_proliferations_b_cell_ebv_positive_mucocutaneous_ulcer = (
        "Malignant:Lymphocytic proliferations - B-Cell:EBV positive mucocutaneous ulcer"
    )
    malignant_lymphocytic_proliferations_b_cell_intravascular_large_b_cell_lymphoma = (
        "Malignant:Lymphocytic proliferations - B-Cell:Intravascular large B-cell lymphoma"
    )
    malignant_lymphocytic_proliferations_b_cell_lymphocytic_proliferation_b_cell_other = (
        "Malignant:Lymphocytic proliferations - B-Cell:Lymphocytic proliferation, B-Cell, other"
    )
    malignant_lymphocytic_proliferations_b_cell_primary_cutaneous_follicle_center_lymphoma = (
        "Malignant:Lymphocytic proliferations - B-Cell:Primary cutaneous follicle center lymphoma"
    )
    malignant_lymphocytic_proliferations_b_cell_primary_cutaneous_large_b_cell_lymphoma = (
        "Malignant:Lymphocytic proliferations - B-Cell:Primary cutaneous large B-Cell lymphoma"
    )
    malignant_lymphocytic_proliferations_b_cell_primary_cutaneous_marginal_zone_lymphoma = (
        "Malignant:Lymphocytic proliferations - B-Cell:Primary cutaneous marginal zone lymphoma"
    )
    malignant_lymphocytic_proliferations_t_cellnk_adult_t_cell_leukemia_or_lymphoma = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK:Adult T-cell leukemia or lymphoma"
    )
    malignant_lymphocytic_proliferations_t_cellnk_chronic_active_ebv_infection = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK:Chronic active EBV infection"
    )
    malignant_lymphocytic_proliferations_t_cellnk_extranodal_t_cellnk_lymphoma = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK:Extranodal T-cell/NK lymphoma"
    )
    malignant_lymphocytic_proliferations_t_cellnk_lymphocytic_proliferation_t_cellnk = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK:Lymphocytic proliferation, T-Cell/NK"
    )
    malignant_lymphocytic_proliferations_t_cellnk_mycosis_fungoides = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK:Mycosis fungoides"
    )
    malignant_lymphocytic_proliferations_t_cellnk_primary_cutaneous_cd30_lymphoproliferative_disease = "Malignant:Lymphocytic proliferations - T-Cell/NK:Primary cutaneous CD30+ lymphoproliferative disease"
    malignant_lymphocytic_proliferations_t_cellnk_primary_cutaneous_cd4_small_or_medium_t_cell_lymphoproliferative_disorder = "Malignant:Lymphocytic proliferations - T-Cell/NK:Primary cutaneous CD4+ small or medium T-cell lymphoproliferative disorder"
    malignant_lymphocytic_proliferations_t_cellnk_primary_cutaneous_peripheral_t_cell_lymphoma = "Malignant:Lymphocytic proliferations - T-Cell/NK:Primary cutaneous peripheral T-cell lymphoma"
    malignant_lymphocytic_proliferations_t_cellnk_sezary_syndrome = (
        "Malignant:Lymphocytic proliferations - T-Cell/NK:Sezary syndrome"
    )
    malignant_lymphocytic_proliferations_t_cellnk_subcutaneous_panniculitis_like_t_cell_lymphoma = "Malignant:Lymphocytic proliferations - T-Cell/NK:Subcutaneous panniculitis-like T-cell lymphoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_adenoid_cystic_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Adenoid cystic carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_adnexal_adenocarcinoma_arising_in_association_with_spiradenoma_cylindroma_or_spiradenocylindroma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Adnexal adenocarcinoma arising in association with spiradenoma, cylindroma, or spiradenocylindroma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_apocrine_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Apocrine carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_digital_papillary_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Digital papillary carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_hidradenocarcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Hidradenocarcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_malignant_mixed_tumor = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Malignant mixed tumor"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_microcystic_adnexal_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Microcystic adnexal carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_mucinous_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Mucinous carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_paget_disease = (
        "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Paget disease"
    )
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_porocarcinoma = (
        "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Porocarcinoma"
    )
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_tubular_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Tubular carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma = (
        "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma"
    )
    malignant_malignant_adnexal_epithelial_proliferations_follicular_baso_squamous_carcinoma = (
        "Malignant:Malignant adnexal epithelial proliferations - Follicular:Baso-squamous carcinoma"
    )
    malignant_malignant_adnexal_epithelial_proliferations_follicular_matrical_or_pilomatrical_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Matrical or pilomatrical carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_proliferating_trichilemmal_carcinoma = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Proliferating trichilemmal carcinoma"
    malignant_malignant_adnexal_epithelial_proliferations_sebaceous_sebaceous_carcinoma = (
        "Malignant:Malignant adnexal epithelial proliferations - Sebaceous:Sebaceous carcinoma"
    )
    malignant_malignant_epidermal_proliferations_bowenoid_papulosis = (
        "Malignant:Malignant epidermal proliferations:Bowenoid papulosis"
    )
    malignant_malignant_epidermal_proliferations_keratoacanthoma = (
        "Malignant:Malignant epidermal proliferations:Keratoacanthoma"
    )
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_in_situ = (
        "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma in situ"
    )
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive = (
        "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive"
    )
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_nos = (
        "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, NOS"
    )
    malignant_malignant_epidermal_proliferations_verrucous_carcinoma = (
        "Malignant:Malignant epidermal proliferations:Verrucous carcinoma"
    )
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive = (
        "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive"
    )
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ = (
        "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ"
    )
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_metastasis = (
        "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma metastasis"
    )
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_nos = (
        "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma, NOS"
    )
    malignant_malignant_soft_tissue_proliferations_adipocytic_liposarcoma = (
        "Malignant:Malignant soft tissue proliferations - Adipocytic:Liposarcoma"
    )
    malignant_malignant_soft_tissue_proliferations_cartilagenous_and_ossifying_extraskeletal_osteosarcoma = "Malignant:Malignant soft tissue proliferations - Cartilagenous and ossifying:Extraskeletal osteosarcoma"
    malignant_malignant_soft_tissue_proliferations_fibro_histiocytic_atypical_fibroxanthoma = (
        "Malignant:Malignant soft tissue proliferations - Fibro-histiocytic:Atypical fibroxanthoma"
    )
    malignant_malignant_soft_tissue_proliferations_fibro_histiocytic_dermatofibrosarcoma_protuberans = "Malignant:Malignant soft tissue proliferations - Fibro-histiocytic:Dermatofibrosarcoma protuberans"
    malignant_malignant_soft_tissue_proliferations_fibro_histiocytic_epithelioid_sarcoma = (
        "Malignant:Malignant soft tissue proliferations - Fibro-histiocytic:Epithelioid sarcoma"
    )
    malignant_malignant_soft_tissue_proliferations_fibro_histiocytic_fibrosarcoma = (
        "Malignant:Malignant soft tissue proliferations - Fibro-histiocytic:Fibrosarcoma"
    )
    malignant_malignant_soft_tissue_proliferations_fibro_histiocytic_pleomorphic_undifferntiated_sarcoma = "Malignant:Malignant soft tissue proliferations - Fibro-histiocytic:Pleomorphic undifferntiated sarcoma"
    malignant_malignant_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_atypical_intradermal_smooth_muscle_tumor = "Malignant:Malignant soft tissue proliferations - Muscle tissue or myofibroblastic:Atypical intradermal smooth muscle tumor"
    malignant_malignant_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_leiomyosarcoma_cutaneous = "Malignant:Malignant soft tissue proliferations - Muscle tissue or myofibroblastic:Leiomyosarcoma, Cutaneous"
    malignant_malignant_soft_tissue_proliferations_muscle_tissue_or_myofibroblastic_rhabdomyoscaroma_cutaneous = "Malignant:Malignant soft tissue proliferations - Muscle tissue or myofibroblastic:Rhabdomyoscaroma, Cutaneous"
    malignant_malignant_soft_tissue_proliferations_myoepithelial_myoepithelial_sarcoma = (
        "Malignant:Malignant soft tissue proliferations - Myoepithelial:Myoepithelial sarcoma"
    )
    malignant_malignant_soft_tissue_proliferations_neural_malignant_granular_cell_tumor = (
        "Malignant:Malignant soft tissue proliferations - Neural:Malignant granular cell tumor"
    )
    malignant_malignant_soft_tissue_proliferations_neural_malignant_peripheral_nerve_sheath_tumor = "Malignant:Malignant soft tissue proliferations - Neural:Malignant peripheral nerve sheath tumor"
    malignant_malignant_soft_tissue_proliferations_unknown_or_other_histiogenesis_ewing_sarcoma_primary_cutaenous = "Malignant:Malignant soft tissue proliferations - Unknown or other histiogenesis:Ewing sarcoma, Primary cutaenous"
    malignant_malignant_soft_tissue_proliferations_vascular_angiosarcoma_cutaneous = (
        "Malignant:Malignant soft tissue proliferations - Vascular:Angiosarcoma cutaneous"
    )
    malignant_malignant_soft_tissue_proliferations_vascular_hemangioendothelioma = (
        "Malignant:Malignant soft tissue proliferations - Vascular:Hemangioendothelioma"
    )
    malignant_malignant_soft_tissue_proliferations_vascular_kaposi_sarcoma = (
        "Malignant:Malignant soft tissue proliferations - Vascular:Kaposi sarcoma"
    )
    malignant_malignant_soft_tissue_proliferations_vascular_malignant_glomus_tumor = (
        "Malignant:Malignant soft tissue proliferations - Vascular:Malignant glomus tumor"
    )
    malignant_merkel_cell_proliferation_merkel_cell_carcinoma = (
        "Malignant:Merkel cell proliferation:Merkel cell carcinoma"
    )
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_hidradenoma_apocrine_hidradenoma_apocrine_predominantly_with_clear_cells = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Hidradenoma, Apocrine:Hidradenoma, Apocrine, Predominantly with clear cells"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_hidradenoma_hidradenoma_poroid = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Hidradenoma:Hidradenoma, Poroid"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_mixed_tumor_mixed_tumor_apocrine_type = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Mixed tumor:Mixed tumor, Apocrine type"
    benign_benign_adnexal_epithelial_proliferations_apocrine_or_eccrine_mixed_tumor_mixed_tumor_eccrine_type = "Benign:Benign adnexal epithelial proliferations - Apocrine or Eccrine:Mixed tumor:Mixed tumor, Eccrine type"
    benign_benign_adnexal_epithelial_proliferations_follicular_trichoepithelioma_trichoepithelioma_desmoplastic = "Benign:Benign adnexal epithelial proliferations - Follicular:Trichoepithelioma:Trichoepithelioma, Desmoplastic"
    benign_benign_adnexal_epithelial_proliferations_follicular_tricholemmoma_tricholemmoma_desmoplastic = "Benign:Benign adnexal epithelial proliferations - Follicular:Tricholemmoma:Tricholemmoma, Desmoplastic"
    benign_benign_epidermal_proliferations_seborrheic_keratosis_seborrheic_keratosis_clonal = (
        "Benign:Benign epidermal proliferations:Seborrheic keratosis:Seborrheic keratosis, Clonal"
    )
    benign_benign_melanocytic_proliferations_nevus_blue_nevus = (
        "Benign:Benign melanocytic proliferations:Nevus:Blue nevus"
    )
    benign_benign_melanocytic_proliferations_dermal_melanocytosis_mongolian_spot = (
        "Benign:Benign melanocytic proliferations:Dermal melanocytosis:Mongolian spot"
    )
    benign_benign_melanocytic_proliferations_dermal_melanocytosis_nevus_of_ito = (
        "Benign:Benign melanocytic proliferations:Dermal melanocytosis:Nevus of Ito"
    )
    benign_benign_melanocytic_proliferations_dermal_melanocytosis_nevus_of_ota = (
        "Benign:Benign melanocytic proliferations:Dermal melanocytosis:Nevus of Ota"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_acral = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Acral"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_agminated = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Agminated"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_atypical_dysplastic_or_clark = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Atypical, Dysplastic, or Clark"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_bap_1_deficient = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, BAP-1 deficient"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_balloon_cell = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Balloon cell"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_combined = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Combined"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_congenital = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Congenital"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_deep_penetrating = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Deep penetrating"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_halo = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Halo"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_lentiginous = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Lentiginous"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_meyerson = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Meyerson"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_nos_compound = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, NOS, Compound"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_nos_dermal = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, NOS, Dermal"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_nos_junctional = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, NOS, Junctional"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_of_special_anatomic_site = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Of special anatomic site"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_recurrent_or_persistent = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Recurrent or persistent"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_reed = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Reed"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_spilus = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Spilus"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_spitz = (
        "Benign:Benign melanocytic proliferations:Nevus:Nevus, Spitz"
    )
    benign_benign_soft_tissue_proliferations_adipocytic_lipoma_lipoma_spindle_cell = (
        "Benign:Benign soft tissue proliferations - Adipocytic:Lipoma:Lipoma, Spindle cell"
    )
    benign_benign_soft_tissue_proliferations_adipocytic_lipoma_lipoma_pleomorphic = (
        "Benign:Benign soft tissue proliferations - Adipocytic:Lipoma:Lipoma, Pleomorphic"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_angiofibroma_angiofibroma_facial = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Angiofibroma:Angiofibroma, Facial"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_angiofibroma_angiofibroma_penile = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Angiofibroma:Angiofibroma, Penile"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_angiofibroma_angiofibroma_periungual = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Angiofibroma:Angiofibroma, Periungual"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_dermatofibroma_dermatofibroma_aneurysmal = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Dermatofibroma:Dermatofibroma, Aneurysmal"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_dermatofibroma_dermatofibroma_atypical = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Dermatofibroma:Dermatofibroma, Atypical"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_dermatofibroma_dermatofibroma_cellular = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Dermatofibroma:Dermatofibroma, Cellular"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_dermatofibroma_dermatofibroma_epithelioid = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Dermatofibroma:Dermatofibroma, Epithelioid"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_dermatofibroma_dermatofibroma_hemosiderotic = "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Dermatofibroma:Dermatofibroma, Hemosiderotic"
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_fibroma_fibroma_pleomorphic = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Fibroma:Fibroma, Pleomorphic"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_fibroma_fibroma_sclerotic = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Fibroma:Fibroma, Sclerotic"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_scar_scar_hypertrophic = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Scar:Scar, Hypertrophic"
    )
    benign_benign_soft_tissue_proliferations_fibro_histiocytic_scar_scar_keloid = (
        "Benign:Benign soft tissue proliferations - Fibro-histiocytic:Scar:Scar, Keloid"
    )
    benign_benign_soft_tissue_proliferations_neural_granular_cell_tumor_granular_cell_tumor_neural_and_s100_positive = "Benign:Benign soft tissue proliferations - Neural:Granular cell tumor:Granular cell tumor, neural and s100 positive"
    benign_benign_soft_tissue_proliferations_neural_granular_cell_tumor_granular_cell_tumor_non_neural_and_s100_negative = "Benign:Benign soft tissue proliferations - Neural:Granular cell tumor:Granular cell tumor, non-neural and s100 negative"
    benign_benign_soft_tissue_proliferations_neural_neuroma_neuroma_palisaded_and_encapsulated = "Benign:Benign soft tissue proliferations - Neural:Neuroma:Neuroma, Palisaded and encapsulated"
    benign_benign_soft_tissue_proliferations_neural_neuroma_neuroma_traumatic = (
        "Benign:Benign soft tissue proliferations - Neural:Neuroma:Neuroma, Traumatic"
    )
    benign_benign_soft_tissue_proliferations_vascular_hemangioma_hemangioma_cherry = (
        "Benign:Benign soft tissue proliferations - Vascular:Hemangioma:Hemangioma, Cherry"
    )
    benign_benign_soft_tissue_proliferations_vascular_hemangioma_hemangioma_hobnail = (
        "Benign:Benign soft tissue proliferations - Vascular:Hemangioma:Hemangioma, Hobnail"
    )
    benign_benign_soft_tissue_proliferations_vascular_hemangioma_hemangioma_infantile = (
        "Benign:Benign soft tissue proliferations - Vascular:Hemangioma:Hemangioma, Infantile"
    )
    benign_benign_soft_tissue_proliferations_vascular_hemangioma_hemangioma_tufted = (
        "Benign:Benign soft tissue proliferations - Vascular:Hemangioma:Hemangioma, Tufted"
    )
    benign_benign_soft_tissue_proliferations_vascular_lymphangioma_lymphangioma_superficial = (
        "Benign:Benign soft tissue proliferations - Vascular:Lymphangioma:Lymphangioma, superficial"
    )
    benign_benign_soft_tissue_proliferations_vascular_lymphangioma_lymphangioma_deep = (
        "Benign:Benign soft tissue proliferations - Vascular:Lymphangioma:Lymphangioma, deep"
    )
    benign_cysts_sebaceous_cyst_infundibular_sebaceous = (
        "Benign:Cysts:Sebaceous cyst:Infundibular, Sebaceous"
    )
    benign_cysts_sebaceous_cyst_epidermal_sebaceous = (
        "Benign:Cysts:Sebaceous cyst:Epidermal, Sebaceous"
    )
    benign_cysts_keratinous_cyst_infundibular_keratinous = (
        "Benign:Cysts:Keratinous cyst:Infundibular, Keratinous"
    )
    benign_cysts_keratinous_cyst_epidermal_keratinous = (
        "Benign:Cysts:Keratinous cyst:Epidermal, Keratinous"
    )
    benign_cysts_trichilemmal_or_isthmic_catagen_or_pilar_cyst_trichilemmal_cyst = (
        "Benign:Cysts:Trichilemmal or isthmic-catagen or pilar cyst:Trichilemmal cyst"
    )
    benign_cysts_trichilemmal_or_isthmic_catagen_or_pilar_cyst_isthmic_catagen_cyst = (
        "Benign:Cysts:Trichilemmal or isthmic-catagen or pilar cyst:Isthmic-catagen cyst"
    )
    benign_cysts_trichilemmal_or_isthmic_catagen_or_pilar_cyst_pilar_cyst = (
        "Benign:Cysts:Trichilemmal or isthmic-catagen or pilar cyst:Pilar cyst"
    )
    benign_hemorrhagic_lesions_hemorrhage_dermal_and_subcutaneous_hemorhage = (
        "Benign:Hemorrhagic lesions:Hemorrhage:Dermal and subcutaneous hemorhage"
    )
    benign_hemorrhagic_lesions_hemorrhage_mucosal_hemorrhage = (
        "Benign:Hemorrhagic lesions:Hemorrhage:Mucosal hemorrhage"
    )
    benign_hemorrhagic_lesions_hemorrhage_subcorneal_and_intracorneal_hemorrhage = (
        "Benign:Hemorrhagic lesions:Hemorrhage:Subcorneal and intracorneal hemorrhage"
    )
    benign_hemorrhagic_lesions_hemorrhage_subungual_hemorrhage = (
        "Benign:Hemorrhagic lesions:Hemorrhage:Subungual hemorrhage"
    )
    benign_langerhans_cell_proliferations_langerhans_cell_histiocytosis_langerhans_cell_histiocytosis_diffuse_or_multifocal = "Benign:Langerhans cell proliferations:Langerhans cell histiocytosis:Langerhans cell histiocytosis, Diffuse or multifocal"
    benign_langerhans_cell_proliferations_langerhans_cell_histiocytosis_langerhans_cell_histiocytosis_solitary_or_unifocal = "Benign:Langerhans cell proliferations:Langerhans cell histiocytosis:Langerhans cell histiocytosis, Solitary or unifocal"
    benign_mast_cell_proliferations_mastocytosis_mastocytosis_diffuse_or_multifocal = (
        "Benign:Mast cell proliferations:Mastocytosis:Mastocytosis, Diffuse or multifocal"
    )
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_keratosis_actinic_keratosis_acantholytic = "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic keratosis:Actinic keratosis, Acantholytic"
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_keratosis_actinic_keratosis_atrophic = "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic keratosis:Actinic keratosis, Atrophic"
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_keratosis_actinic_keratosis_bowenoid = "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic keratosis:Actinic keratosis, Bowenoid"
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_keratosis_actinic_keratosis_hypertrophic = "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic keratosis:Actinic keratosis, Hypertrophic"
    indeterminate_indeterminate_epidermal_proliferations_solar_or_actinic_keratosis_actinic_keratosis_lichenoid = "Indeterminate:Indeterminate epidermal proliferations:Solar or actinic keratosis:Actinic keratosis, Lichenoid"
    indeterminate_indeterminate_melanocytic_proliferations_atypical_spitz_tumor_atypical_spitz_tumor_compound = "Indeterminate:Indeterminate melanocytic proliferations:Atypical Spitz tumor:Atypical Spitz tumor, Compound"
    indeterminate_indeterminate_melanocytic_proliferations_atypical_spitz_tumor_atypical_spitz_tumor_dermal = "Indeterminate:Indeterminate melanocytic proliferations:Atypical Spitz tumor:Atypical Spitz tumor, Dermal"
    indeterminate_indeterminate_melanocytic_proliferations_atypical_spitz_tumor_atypical_spitz_tumor_junctional = "Indeterminate:Indeterminate melanocytic proliferations:Atypical Spitz tumor:Atypical Spitz tumor, Junctional"
    malignant_lymphocytic_proliferations_t_cellnk_extranodal_t_cellnk_lymphoma_extranodal_t_cellnk_lymphoma_nasal_type = "Malignant:Lymphocytic proliferations - T-Cell/NK:Extranodal T-cell/NK lymphoma:Extranodal T-cell/NK lymphoma, Nasal type"
    malignant_lymphocytic_proliferations_t_cellnk_mycosis_fungoides_mycosis_fungoides_folliculotropic = "Malignant:Lymphocytic proliferations - T-Cell/NK:Mycosis fungoides:Mycosis fungoides, Folliculotropic"
    malignant_lymphocytic_proliferations_t_cellnk_mycosis_fungoides_mycosis_fungoides_granulomatous_slack_skin = "Malignant:Lymphocytic proliferations - T-Cell/NK:Mycosis fungoides:Mycosis fungoides, Granulomatous slack skin"
    malignant_lymphocytic_proliferations_t_cellnk_mycosis_fungoides_mycosis_fungoides_pagetoid_reticulosis = "Malignant:Lymphocytic proliferations - T-Cell/NK:Mycosis fungoides:Mycosis fungoides, Pagetoid reticulosis"
    malignant_lymphocytic_proliferations_t_cellnk_mycosis_fungoides_mycosis_fungoides_with_large_cell_transformation = "Malignant:Lymphocytic proliferations - T-Cell/NK:Mycosis fungoides:Mycosis fungoides, With large cell transformation"
    malignant_lymphocytic_proliferations_t_cellnk_primary_cutaneous_cd30_lymphoproliferative_disease_cutanous_anaplastic_large_cell_lymphoma = "Malignant:Lymphocytic proliferations - T-Cell/NK:Primary cutaneous CD30+ lymphoproliferative disease:Cutanous anaplastic large cell lymphoma"
    malignant_lymphocytic_proliferations_t_cellnk_primary_cutaneous_cd30_lymphoproliferative_disease_lymphomatoid_papulosis = "Malignant:Lymphocytic proliferations - T-Cell/NK:Primary cutaneous CD30+ lymphoproliferative disease:Lymphomatoid papulosis"
    malignant_lymphocytic_proliferations_t_cellnk_primary_cutaneous_peripheral_t_cell_lymphoma_primary_cutaneous_peripheral_t_cell_lymphoma_rare_subtype = "Malignant:Lymphocytic proliferations - T-Cell/NK:Primary cutaneous peripheral T-cell lymphoma:Primary cutaneous peripheral T-cell lymphoma, Rare subtype"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_paget_disease_paget_disease_extra_mammary = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Paget disease:Paget disease, Extra-mammary"
    malignant_malignant_adnexal_epithelial_proliferations_apocrine_or_eccrine_paget_disease_paget_disease_mammary = "Malignant:Malignant adnexal epithelial proliferations - Apocrine or Eccrine:Paget disease:Paget disease, Mammary"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_with_adnexal_differentiation = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma with adnexal differentiation"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_with_sarcomatoid_differentiation = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma with sarcomatoid differentiation"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_combined_subtypes = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Combined subtypes"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_fibroeipthelial = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Fibroeipthelial"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_infiltrating = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Infiltrating"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_micronodular = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Micronodular"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_nodular = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Nodular"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_sclerosing_or_morpheaform = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Sclerosing or morpheaform"
    malignant_malignant_adnexal_epithelial_proliferations_follicular_basal_cell_carcinoma_basal_cell_carcinoma_superficial = "Malignant:Malignant adnexal epithelial proliferations - Follicular:Basal cell carcinoma:Basal cell carcinoma, Superficial"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_in_situ_squamous_cell_carcinoma_in_situ_bowens_disease = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma in situ:Squamous cell carcinoma in situ, Bowens disease"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_acantholytic = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Acantholytic"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_adeno_squamous = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Adeno-squamous"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_clear_cell = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Clear cell"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_keratoacanthoma_type = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Keratoacanthoma-type"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_sarcomatoid = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Sarcomatoid"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_spindle_cell = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Spindle cell"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_verrucous = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Verrucous"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_nos_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, NOS, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_nos_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, NOS, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_nos_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, NOS, poorly differentiated"
    malignant_malignant_epidermal_proliferations_verrucous_carcinoma_verrucous_carcinoma_carcinoma_cuniculatum_type = "Malignant:Malignant epidermal proliferations:Verrucous carcinoma:Verrucous carcinoma, Carcinoma cuniculatum type"
    malignant_malignant_epidermal_proliferations_verrucous_carcinoma_verrucous_carcinoma_giant_condyloma_type = "Malignant:Malignant epidermal proliferations:Verrucous carcinoma:Verrucous carcinoma, Giant condyloma type"
    malignant_malignant_epidermal_proliferations_verrucous_carcinoma_verrucous_carcinoma_oral_florid_papilomatosis_type = "Malignant:Malignant epidermal proliferations:Verrucous carcinoma:Verrucous carcinoma, Oral florid papilomatosis type"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_acral_or_acral_lentiginous = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Acral or Acral-lentiginous"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_arising_in_a_congenital_nevus = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Arising in a congenital nevus"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_associated_with_a_nevus = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Associated with a nevus"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_blue_nevus_like = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Blue nevus-like"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_desmoplastic = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Desmoplastic"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_heavily_pigmented = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Heavily pigmented"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_mucosal = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Mucosal"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_neurotropic = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Neurotropic"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_nevoid = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Nevoid"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_nodular = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Nodular"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_on_chronically_sun_exposed_skin_or_lentigo_maligna_melanoma = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, On chronically sun-exposed skin or lentigo maligna melanoma"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_pigmented_spindle_cell_nevus_like = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Pigmented spindle cell nevus like"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_recurrent_or_persistent = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Recurrent or persistent"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_spitzoid = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Spitzoid"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_superficial_spreading = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Superficial spreading"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ_melanoma_in_situ_acral_or_acral_lentiginous = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ:Melanoma in situ, Acral or acral-lentiginous"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ_melanoma_in_situ_lentigo_maligna_type = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ:Melanoma in situ, Lentigo maligna type"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ_melanoma_in_situ_mucosal = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ:Melanoma in situ, Mucosal"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ_melanoma_in_situ_recurrent_or_persistent = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ:Melanoma in situ, Recurrent or persistent"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ_melanoma_in_situ_superficial_spreading = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ:Melanoma in situ, Superficial spreading"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_in_situ_melanoma_in_situ_associated_with_a_nevus = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma in situ:Melanoma in situ, associated with a nevus"
    malignant_malignant_soft_tissue_proliferations_adipocytic_liposarcoma_liposarcoma_undifferentiated = "Malignant:Malignant soft tissue proliferations - Adipocytic:Liposarcoma:Liposarcoma, Undifferentiated"
    malignant_malignant_soft_tissue_proliferations_adipocytic_liposarcoma_liposarcoma_well_differentiated = "Malignant:Malignant soft tissue proliferations - Adipocytic:Liposarcoma:Liposarcoma, Well differentiated"
    malignant_malignant_soft_tissue_proliferations_vascular_angiosarcoma_cutaneous_angiosarcoma_cutaneous_epithelioid = "Malignant:Malignant soft tissue proliferations - Vascular:Angiosarcoma cutaneous:Angiosarcoma cutaneous, Epithelioid"
    malignant_malignant_soft_tissue_proliferations_vascular_angiosarcoma_cutaneous_angiosarcoma_cutaneous_face_and_scalp_of_elderly_patients = "Malignant:Malignant soft tissue proliferations - Vascular:Angiosarcoma cutaneous:Angiosarcoma cutaneous, Face and scalp of elderly patients"
    malignant_malignant_soft_tissue_proliferations_vascular_angiosarcoma_cutaneous_angiosarcoma_cutaneous_post_irradiation = "Malignant:Malignant soft tissue proliferations - Vascular:Angiosarcoma cutaneous:Angiosarcoma cutaneous, Post-irradiation"
    malignant_malignant_soft_tissue_proliferations_vascular_angiosarcoma_cutaneous_angiosarcoma_cutaneous_with_associated_lymphedema = "Malignant:Malignant soft tissue proliferations - Vascular:Angiosarcoma cutaneous:Angiosarcoma cutaneous, With associated lymphedema"
    malignant_malignant_soft_tissue_proliferations_vascular_hemangioendothelioma_hemangioendothelioma_kaposiform = "Malignant:Malignant soft tissue proliferations - Vascular:Hemangioendothelioma:Hemangioendothelioma, Kaposiform"
    benign_benign_melanocytic_proliferations_nevus_blue_nevus_blue_nevus_cellular = (
        "Benign:Benign melanocytic proliferations:Nevus:Blue nevus:Blue nevus, Cellular"
    )
    benign_benign_melanocytic_proliferations_nevus_blue_nevus_blue_nevus_common = (
        "Benign:Benign melanocytic proliferations:Nevus:Blue nevus:Blue nevus, Common"
    )
    benign_benign_melanocytic_proliferations_nevus_blue_nevus_blue_nevus_epithelioid = (
        "Benign:Benign melanocytic proliferations:Nevus:Blue nevus:Blue nevus, Epithelioid"
    )
    benign_benign_melanocytic_proliferations_nevus_blue_nevus_blue_nevus_plaque_type = (
        "Benign:Benign melanocytic proliferations:Nevus:Blue nevus:Blue nevus, Plaque type"
    )
    benign_benign_melanocytic_proliferations_nevus_blue_nevus_blue_nevus_sclerosing = (
        "Benign:Benign melanocytic proliferations:Nevus:Blue nevus:Blue nevus, Sclerosing"
    )
    benign_benign_melanocytic_proliferations_nevus_nevus_atypical_dysplastic_or_clark_nevus_atypical = "Benign:Benign melanocytic proliferations:Nevus:Nevus, Atypical, Dysplastic, or Clark:Nevus, Atypical"
    benign_benign_melanocytic_proliferations_nevus_nevus_atypical_dysplastic_or_clark_nevus_dysplastic = "Benign:Benign melanocytic proliferations:Nevus:Nevus, Atypical, Dysplastic, or Clark:Nevus, Dysplastic"
    benign_benign_melanocytic_proliferations_nevus_nevus_atypical_dysplastic_or_clark_nevus_clark = "Benign:Benign melanocytic proliferations:Nevus:Nevus, Atypical, Dysplastic, or Clark:Nevus, Clark"
    benign_benign_melanocytic_proliferations_nevus_nevus_congenital_nevus_congenital_by_history = "Benign:Benign melanocytic proliferations:Nevus:Nevus, Congenital:Nevus, Congenital, by history"
    benign_benign_melanocytic_proliferations_nevus_nevus_congenital_nevus_congenital_by_histopathological_pattern = "Benign:Benign melanocytic proliferations:Nevus:Nevus, Congenital:Nevus, Congenital, by histopathological pattern"
    benign_benign_melanocytic_proliferations_nevus_nevus_congenital_nevus_congenital_by_history_and_histopathological_pattern = "Benign:Benign melanocytic proliferations:Nevus:Nevus, Congenital:Nevus, Congenital, by history and histopathological pattern"
    benign_mast_cell_proliferations_mastocytosis_mastocytosis_diffuse_or_multifocal_telangiectasia_macularis_eruptiva_perstans = "Benign:Mast cell proliferations:Mastocytosis:Mastocytosis, Diffuse or multifocal:Telangiectasia macularis eruptiva perstans"
    benign_mast_cell_proliferations_mastocytosis_mastocytosis_diffuse_or_multifocal_mastocytosis_diffuse_cutaenous = "Benign:Mast cell proliferations:Mastocytosis:Mastocytosis, Diffuse or multifocal:Mastocytosis, Diffuse cutaenous"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_acantholytic_squamous_cell_carcinoma_invasive_acantholytic_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Acantholytic:Squamous cell carcinoma, Invasive, Acantholytic, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_acantholytic_squamous_cell_carcinoma_invasive_acantholytic_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Acantholytic:Squamous cell carcinoma, Invasive, Acantholytic, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_acantholytic_squamous_cell_carcinoma_invasive_acantholytic_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Acantholytic:Squamous cell carcinoma, Invasive, Acantholytic, poorly differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_adeno_squamous_squamous_cell_carcinoma_invasive_adeno_squamous_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Adeno-squamous:Squamous cell carcinoma, Invasive, Adeno-squamous, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_adeno_squamous_squamous_cell_carcinoma_invasive_adeno_squamous_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Adeno-squamous:Squamous cell carcinoma, Invasive, Adeno-squamous, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_adeno_squamous_squamous_cell_carcinoma_invasive_adeno_squamous_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Adeno-squamous:Squamous cell carcinoma, Invasive, Adeno-squamous, poorly differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_clear_cell_squamous_cell_carcinoma_invasive_clear_cell_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Clear cell:Squamous cell carcinoma, Invasive, Clear cell, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_clear_cell_squamous_cell_carcinoma_invasive_clear_cell_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Clear cell:Squamous cell carcinoma, Invasive, Clear cell, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_clear_cell_squamous_cell_carcinoma_invasive_clear_cell_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Clear cell:Squamous cell carcinoma, Invasive, Clear cell, poorly differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_keratoacanthoma_type_squamous_cell_carcinoma_invasive_keratoacanthoma_type_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Keratoacanthoma-type:Squamous cell carcinoma, Invasive, Keratoacanthoma-type, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_keratoacanthoma_type_squamous_cell_carcinoma_invasive_keratoacanthoma_type_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Keratoacanthoma-type:Squamous cell carcinoma, Invasive, Keratoacanthoma-type, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_keratoacanthoma_type_squamous_cell_carcinoma_invasive_keratoacanthoma_type_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Keratoacanthoma-type:Squamous cell carcinoma, Invasive, Keratoacanthoma-type, poorly differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_sarcomatoid_squamous_cell_carcinoma_invasive_sarcomatoid_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Sarcomatoid:Squamous cell carcinoma, Invasive, Sarcomatoid, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_sarcomatoid_squamous_cell_carcinoma_invasive_sarcomatoid_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Sarcomatoid:Squamous cell carcinoma, Invasive, Sarcomatoid, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_sarcomatoid_squamous_cell_carcinoma_invasive_sarcomatoid_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Sarcomatoid:Squamous cell carcinoma, Invasive, Sarcomatoid, poorly differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_spindle_cell_squamous_cell_carcinoma_invasive_spindle_cell_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Spindle cell:Squamous cell carcinoma, Invasive, Spindle cell, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_spindle_cell_squamous_cell_carcinoma_invasive_spindle_cell_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Spindle cell:Squamous cell carcinoma, Invasive, Spindle cell, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_spindle_cell_squamous_cell_carcinoma_invasive_spindle_cell_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Spindle cell:Squamous cell carcinoma, Invasive, Spindle cell, poorly differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_verrucous_squamous_cell_carcinoma_invasive_verrucous_well_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Verrucous:Squamous cell carcinoma, Invasive, Verrucous, well differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_verrucous_squamous_cell_carcinoma_invasive_verrucous_moderately_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Verrucous:Squamous cell carcinoma, Invasive, Verrucous, moderately differentiated"
    malignant_malignant_epidermal_proliferations_squamous_cell_carcinoma_invasive_squamous_cell_carcinoma_invasive_verrucous_squamous_cell_carcinoma_invasive_verrucous_poorly_differentiated = "Malignant:Malignant epidermal proliferations:Squamous cell carcinoma, Invasive:Squamous cell carcinoma, Invasive, Verrucous:Squamous cell carcinoma, Invasive, Verrucous, poorly differentiated"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_blue_nevus_like_melanoma_invasive_resembling_blue_nevus = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Blue nevus-like:Melanoma Invasive, resembling blue nevus"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_blue_nevus_like_melanoma_invasive_originating_from_blue_nevus = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Blue nevus-like:Melanoma Invasive, originating from blue nevus"
    malignant_malignant_melanocytic_proliferations_melanoma_melanoma_invasive_melanoma_invasive_heavily_pigmented_melanoma_invasive_heavily_pigmented_resembling_epithelioid_blue_nevus_or_melanoma_developing_in_animals = "Malignant:Malignant melanocytic proliferations (Melanoma):Melanoma Invasive:Melanoma Invasive, Heavily pigmented:Melanoma Invasive, Heavily pigmented, resembling epithelioid blue nevus or melanoma developing in animals"

    @staticmethod
    @cache
    def levels(value: str) -> list[str | None]:
        levels_list = value.split(":")
        levels_list += [None] * (5 - len(levels_list))
        return levels_list

    @staticmethod
    @cache
    def as_dict(value: str) -> dict[str, str | None]:
        return {
            "diagnosis_1": DiagnosisEnum.levels(value)[0],
            "diagnosis_2": DiagnosisEnum.levels(value)[1],
            "diagnosis_3": DiagnosisEnum.levels(value)[2],
            "diagnosis_4": DiagnosisEnum.levels(value)[3],
            "diagnosis_5": DiagnosisEnum.levels(value)[4],
        }

    @classmethod
    @cache
    def reverse_ordered_hierarchy(cls) -> list[str]:
        return sorted(cls, key=lambda x: x.value.count(":"), reverse=True)

    @classmethod
    @cache
    def accept_terminal_values(cls, value: Any) -> Any:
        """
        Allow the user to specify any terminal value of the hierarchy to obtain the relevant value.

        e.g. "baz" can be used to obtain "foo:bar:baz", or "bar" for "foo:bar".
        """
        if ":" not in value:
            for member in cls.reverse_ordered_hierarchy():
                if value == member.value.split(":")[-1]:
                    return member.value

        return value

    @classmethod
    @cache
    def _melanoma_diagnoses(cls):
        return [
            diagnosis
            for diagnosis in cls
            if diagnosis.startswith(cls.malignant_malignant_melanocytic_proliferations_melanoma)
        ] + [cls.malignant_collision_at_least_one_malignant_proliferation]

    @classmethod
    @cache
    def is_melanoma(cls, value: str) -> bool:
        return value in cls._melanoma_diagnoses()

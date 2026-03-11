from __future__ import annotations

from enum import StrEnum
from functools import cache
from typing import Self


class AnatomSiteEnum(StrEnum):
    head_and_neck = "Head and neck"
    trunk = "Trunk"
    upper_extremity = "Upper extremity"
    lower_extremity = "Lower extremity"
    anogenital_region = "Anogenital region"
    head_and_neck_head = "Head and neck:Head"
    head_and_neck_neck = "Head and neck:Neck"
    trunk_anterior_trunk = "Trunk:Anterior trunk"
    trunk_lateral_trunk = "Trunk:Lateral trunk"
    trunk_posterior_trunk = "Trunk:Posterior trunk"
    upper_extremity_shoulder = "Upper extremity:Shoulder"
    upper_extremity_upper_arm = "Upper extremity:Upper arm"
    upper_extremity_elbow = "Upper extremity:Elbow"
    upper_extremity_forearm = "Upper extremity:Forearm"
    upper_extremity_wrist = "Upper extremity:Wrist"
    upper_extremity_hand = "Upper extremity:Hand"
    lower_extremity_buttock = "Lower extremity:Buttock"
    lower_extremity_thigh = "Lower extremity:Thigh"
    lower_extremity_knee = "Lower extremity:Knee"
    lower_extremity_lower_leg = "Lower extremity:Lower leg"
    lower_extremity_ankle = "Lower extremity:Ankle"
    lower_extremity_foot = "Lower extremity:Foot"
    anogenital_region_perianal_region = "Anogenital region:Perianal region"
    anogenital_region_genital_region = "Anogenital region:Genital region"
    head_and_neck_head_scalp = "Head and neck:Head:Scalp"
    head_and_neck_head_ear = "Head and neck:Head:Ear"
    head_and_neck_head_face = "Head and neck:Head:Face"
    head_and_neck_neck_front_of_neck = "Head and neck:Neck:Front of neck"
    head_and_neck_neck_side_of_neck = "Head and neck:Neck:Side of neck"
    head_and_neck_neck_nape_of_neck = "Head and neck:Neck:Nape of neck"
    head_and_neck_neck_supraclavicular_region = "Head and neck:Neck:Supraclavicular region"
    trunk_anterior_trunk_anterior_chest = "Trunk:Anterior trunk:Anterior chest"
    trunk_anterior_trunk_anterior_abdomen = "Trunk:Anterior trunk:Anterior abdomen"
    trunk_lateral_trunk_axilla = "Trunk:Lateral trunk:Axilla"
    trunk_lateral_trunk_lateral_chest = "Trunk:Lateral trunk:Lateral chest"
    trunk_lateral_trunk_lateral_abdomen = "Trunk:Lateral trunk:Lateral abdomen"
    trunk_posterior_trunk_upper_back = "Trunk:Posterior trunk:Upper back"
    trunk_posterior_trunk_mid_back = "Trunk:Posterior trunk:Mid back"
    trunk_posterior_trunk_lower_back = "Trunk:Posterior trunk:Lower back"
    upper_extremity_shoulder_anterior_shoulder = "Upper extremity:Shoulder:Anterior shoulder"
    upper_extremity_shoulder_lateral_shoulder = "Upper extremity:Shoulder:Lateral shoulder"
    upper_extremity_shoulder_posterior_shoulder = "Upper extremity:Shoulder:Posterior shoulder"
    upper_extremity_upper_arm_anterior_upper_arm = "Upper extremity:Upper arm:Anterior upper arm"
    upper_extremity_upper_arm_lateral_upper_arm = "Upper extremity:Upper arm:Lateral upper arm"
    upper_extremity_upper_arm_posterior_upper_arm = "Upper extremity:Upper arm:Posterior upper arm"
    upper_extremity_upper_arm_medial_upper_arm = "Upper extremity:Upper arm:Medial upper arm"
    upper_extremity_elbow_elbow_tip = "Upper extremity:Elbow:Elbow tip"
    upper_extremity_elbow_lateral_elbow = "Upper extremity:Elbow:Lateral elbow"
    upper_extremity_elbow_medial_elbow = "Upper extremity:Elbow:Medial elbow"
    upper_extremity_elbow_antecubital_fossa = "Upper extremity:Elbow:Antecubital fossa"
    upper_extremity_forearm_dorsal_forearm = "Upper extremity:Forearm:Dorsal forearm"
    upper_extremity_forearm_volar_forearm = "Upper extremity:Forearm:Volar forearm"
    upper_extremity_forearm_radial_forearm = "Upper extremity:Forearm:Radial forearm"
    upper_extremity_forearm_ulnar_forearm = "Upper extremity:Forearm:Ulnar forearm"
    upper_extremity_wrist_dorsal_wrist = "Upper extremity:Wrist:Dorsal wrist"
    upper_extremity_wrist_volar_wrist = "Upper extremity:Wrist:Volar wrist"
    upper_extremity_wrist_radial_wrist = "Upper extremity:Wrist:Radial wrist"
    upper_extremity_wrist_ulnar_wrist = "Upper extremity:Wrist:Ulnar wrist"
    upper_extremity_hand_dorsum_of_hand = "Upper extremity:Hand:Dorsum of hand"
    upper_extremity_hand_palm_of_hand = "Upper extremity:Hand:Palm of hand"
    upper_extremity_hand_fingers_and_thumb = "Upper extremity:Hand:Fingers and thumb"
    lower_extremity_buttock_gluteal_fold = "Lower extremity:Buttock:Gluteal fold"
    lower_extremity_thigh_anterior_thigh = "Lower extremity:Thigh:Anterior thigh"
    lower_extremity_thigh_lateral_thigh = "Lower extremity:Thigh:Lateral thigh"
    lower_extremity_thigh_posterior_thigh = "Lower extremity:Thigh:Posterior thigh"
    lower_extremity_thigh_medial_thigh = "Lower extremity:Thigh:Medial thigh"
    lower_extremity_knee_patellar_region = "Lower extremity:Knee:Patellar region"
    lower_extremity_knee_lateral_knee = "Lower extremity:Knee:Lateral knee"
    lower_extremity_knee_medial_knee = "Lower extremity:Knee:Medial knee"
    lower_extremity_knee_popliteal_fossa = "Lower extremity:Knee:Popliteal fossa"
    lower_extremity_lower_leg_shin = "Lower extremity:Lower leg:Shin"
    lower_extremity_lower_leg_calf = "Lower extremity:Lower leg:Calf"
    lower_extremity_ankle_anterior_ankle = "Lower extremity:Ankle:Anterior ankle"
    lower_extremity_ankle_medial_ankle = "Lower extremity:Ankle:Medial ankle"
    lower_extremity_ankle_lateral_ankle = "Lower extremity:Ankle:Lateral ankle"
    lower_extremity_ankle_achilles_region = "Lower extremity:Ankle:Achilles region"
    lower_extremity_foot_dorsum_of_foot = "Lower extremity:Foot:Dorsum of foot"
    lower_extremity_foot_sole_of_foot = "Lower extremity:Foot:Sole of foot"
    lower_extremity_foot_toes = "Lower extremity:Foot:Toes"
    anogenital_region_perianal_region_anus = "Anogenital region:Perianal region:Anus"
    anogenital_region_perianal_region_intergluteal_cleft = (
        "Anogenital region:Perianal region:Intergluteal cleft"
    )
    anogenital_region_perianal_region_perineum = "Anogenital region:Perianal region:Perineum"
    anogenital_region_genital_region_vulva = "Anogenital region:Genital region:Vulva"
    anogenital_region_genital_region_vagina = "Anogenital region:Genital region:Vagina"
    anogenital_region_genital_region_penis = "Anogenital region:Genital region:Penis"
    anogenital_region_genital_region_scrotum = "Anogenital region:Genital region:Scrotum"
    anogenital_region_genital_region_perigenital_region = (
        "Anogenital region:Genital region:Perigenital region"
    )
    head_and_neck_head_scalp_frontal_scalp = "Head and neck:Head:Scalp:Frontal scalp"
    head_and_neck_head_scalp_temporal_scalp = "Head and neck:Head:Scalp:Temporal scalp"
    head_and_neck_head_scalp_parietal_scalp = "Head and neck:Head:Scalp:Parietal scalp"
    head_and_neck_head_scalp_occipital_scalp = "Head and neck:Head:Scalp:Occipital scalp"
    head_and_neck_head_scalp_vertex_of_scalp = "Head and neck:Head:Scalp:Vertex of scalp"
    head_and_neck_head_ear_pinna = "Head and neck:Head:Ear:Pinna"
    head_and_neck_head_ear_external_auditory_canal = (
        "Head and neck:Head:Ear:External auditory canal"
    )
    head_and_neck_head_face_forehead = "Head and neck:Head:Face:Forehead"
    head_and_neck_head_face_temple = "Head and neck:Head:Face:Temple"
    head_and_neck_head_face_orbital_region = "Head and neck:Head:Face:Orbital region"
    head_and_neck_head_face_cheek = "Head and neck:Head:Face:Cheek"
    head_and_neck_head_face_nose = "Head and neck:Head:Face:Nose"
    head_and_neck_head_face_oral_region = "Head and neck:Head:Face:Oral region"
    head_and_neck_head_face_mouth = "Head and neck:Head:Face:Mouth"
    head_and_neck_head_face_chin = "Head and neck:Head:Face:Chin"
    trunk_anterior_trunk_anterior_chest_upper_anterior_chest = (
        "Trunk:Anterior trunk:Anterior chest:Upper anterior chest"
    )
    trunk_anterior_trunk_anterior_chest_lower_anterior_chest = (
        "Trunk:Anterior trunk:Anterior chest:Lower anterior chest"
    )
    trunk_anterior_trunk_anterior_chest_breast = "Trunk:Anterior trunk:Anterior chest:Breast"
    trunk_anterior_trunk_anterior_abdomen_upper_anterior_abdomen = (
        "Trunk:Anterior trunk:Anterior abdomen:Upper anterior abdomen"
    )
    trunk_anterior_trunk_anterior_abdomen_mid_anterior_abdomen = (
        "Trunk:Anterior trunk:Anterior abdomen:Mid anterior abdomen"
    )
    trunk_anterior_trunk_anterior_abdomen_periumbilical_region = (
        "Trunk:Anterior trunk:Anterior abdomen:Periumbilical region"
    )
    trunk_anterior_trunk_anterior_abdomen_lower_anterior_abdomen = (
        "Trunk:Anterior trunk:Anterior abdomen:Lower anterior abdomen"
    )
    trunk_lateral_trunk_axilla_apex_of_axilla = "Trunk:Lateral trunk:Axilla:Apex of axilla"
    trunk_lateral_trunk_axilla_anterior_axillary_fold = (
        "Trunk:Lateral trunk:Axilla:Anterior axillary fold"
    )
    trunk_lateral_trunk_axilla_posterior_axillary_fold = (
        "Trunk:Lateral trunk:Axilla:Posterior axillary fold"
    )
    trunk_lateral_trunk_lateral_chest_upper_lateral_chest = (
        "Trunk:Lateral trunk:Lateral chest:Upper lateral chest"
    )
    trunk_lateral_trunk_lateral_chest_lower_lateral_chest = (
        "Trunk:Lateral trunk:Lateral chest:Lower lateral chest"
    )
    trunk_posterior_trunk_upper_back_lateral_upper_back = (
        "Trunk:Posterior trunk:Upper back:Lateral upper back"
    )
    trunk_posterior_trunk_upper_back_paraspinal_upper_back = (
        "Trunk:Posterior trunk:Upper back:Paraspinal upper back"
    )
    trunk_posterior_trunk_mid_back_lateral_mid_back = (
        "Trunk:Posterior trunk:Mid back:Lateral mid back"
    )
    trunk_posterior_trunk_mid_back_paraspinal_mid_back = (
        "Trunk:Posterior trunk:Mid back:Paraspinal mid back"
    )
    trunk_posterior_trunk_lower_back_lateral_lower_back = (
        "Trunk:Posterior trunk:Lower back:Lateral lower back"
    )
    trunk_posterior_trunk_lower_back_paraspinal_lower_back = (
        "Trunk:Posterior trunk:Lower back:Paraspinal lower back"
    )
    upper_extremity_hand_dorsum_of_hand_knuckles = "Upper extremity:Hand:Dorsum of hand:Knuckles"
    upper_extremity_hand_dorsum_of_hand_interdigital_web_spaces_of_hand = (
        "Upper extremity:Hand:Dorsum of hand:Interdigital web spaces of hand"
    )
    upper_extremity_hand_palm_of_hand_hypothenar_eminence = (
        "Upper extremity:Hand:Palm of hand:Hypothenar eminence"
    )
    upper_extremity_hand_palm_of_hand_thenar_eminence = (
        "Upper extremity:Hand:Palm of hand:Thenar eminence"
    )
    upper_extremity_hand_palm_of_hand_central_palm = (
        "Upper extremity:Hand:Palm of hand:Central palm"
    )
    upper_extremity_hand_palm_of_hand_distal_palm = "Upper extremity:Hand:Palm of hand:Distal palm"
    upper_extremity_hand_fingers_and_thumb_thumb = "Upper extremity:Hand:Fingers and thumb:Thumb"
    upper_extremity_hand_fingers_and_thumb_index_finger = (
        "Upper extremity:Hand:Fingers and thumb:Index finger"
    )
    upper_extremity_hand_fingers_and_thumb_middle_finger = (
        "Upper extremity:Hand:Fingers and thumb:Middle finger"
    )
    upper_extremity_hand_fingers_and_thumb_ring_finger = (
        "Upper extremity:Hand:Fingers and thumb:Ring finger"
    )
    upper_extremity_hand_fingers_and_thumb_little_finger = (
        "Upper extremity:Hand:Fingers and thumb:Little finger"
    )
    lower_extremity_thigh_lateral_thigh_hip = "Lower extremity:Thigh:Lateral thigh:Hip"
    lower_extremity_thigh_medial_thigh_upper_medial_thigh = (
        "Lower extremity:Thigh:Medial thigh:Upper medial thigh"
    )
    lower_extremity_lower_leg_calf_lateral_calf = "Lower extremity:Lower leg:Calf:Lateral calf"
    lower_extremity_lower_leg_calf_medial_calf = "Lower extremity:Lower leg:Calf:Medial calf"
    lower_extremity_lower_leg_calf_posterior_calf = "Lower extremity:Lower leg:Calf:Posterior calf"
    lower_extremity_ankle_medial_ankle_medial_malleolus = (
        "Lower extremity:Ankle:Medial ankle:Medial malleolus"
    )
    lower_extremity_ankle_lateral_ankle_lateral_malleolus = (
        "Lower extremity:Ankle:Lateral ankle:Lateral malleolus"
    )
    lower_extremity_foot_dorsum_of_foot_metatarsophalangeal_joints = (
        "Lower extremity:Foot:Dorsum of foot:Metatarsophalangeal joints"
    )
    lower_extremity_foot_dorsum_of_foot_interdigital_web_spaces_of_foot = (
        "Lower extremity:Foot:Dorsum of foot:Interdigital web spaces of foot"
    )
    lower_extremity_foot_sole_of_foot_plantar_surface_of_forefoot = (
        "Lower extremity:Foot:Sole of foot:Plantar surface of forefoot"
    )
    lower_extremity_foot_sole_of_foot_lateral_plantar_region = (
        "Lower extremity:Foot:Sole of foot:Lateral plantar region"
    )
    lower_extremity_foot_sole_of_foot_medial_surface_of_sole_of_foot = (
        "Lower extremity:Foot:Sole of foot:Medial surface of sole of foot"
    )
    lower_extremity_foot_sole_of_foot_arch_of_foot = (
        "Lower extremity:Foot:Sole of foot:Arch of foot"
    )
    lower_extremity_foot_sole_of_foot_heel = "Lower extremity:Foot:Sole of foot:Heel"
    lower_extremity_foot_toes_great_toe = "Lower extremity:Foot:Toes:Great toe"
    lower_extremity_foot_toes_second_toe = "Lower extremity:Foot:Toes:Second toe"
    lower_extremity_foot_toes_third_toe = "Lower extremity:Foot:Toes:Third toe"
    lower_extremity_foot_toes_fourth_toe = "Lower extremity:Foot:Toes:Fourth toe"
    lower_extremity_foot_toes_fifth_toe = "Lower extremity:Foot:Toes:Fifth toe"
    anogenital_region_genital_region_vulva_labium_majus = (
        "Anogenital region:Genital region:Vulva:Labium majus"
    )
    anogenital_region_genital_region_vulva_labium_minus = (
        "Anogenital region:Genital region:Vulva:Labium minus"
    )
    anogenital_region_genital_region_vulva_clitoris = (
        "Anogenital region:Genital region:Vulva:Clitoris"
    )
    anogenital_region_genital_region_vulva_vulval_vestibule = (
        "Anogenital region:Genital region:Vulva:Vulval vestibule"
    )
    anogenital_region_genital_region_vulva_frenulum_of_labia_minora = (
        "Anogenital region:Genital region:Vulva:Frenulum of labia minora"
    )
    anogenital_region_genital_region_vagina_vaginal_introitus = (
        "Anogenital region:Genital region:Vagina:Vaginal introitus"
    )
    anogenital_region_genital_region_penis_glans_penis = (
        "Anogenital region:Genital region:Penis:Glans penis"
    )
    anogenital_region_genital_region_perigenital_region_inguinocrural_fold = (
        "Anogenital region:Genital region:Perigenital region:Inguinocrural fold"
    )
    anogenital_region_genital_region_perigenital_region_suprapubic_region = (
        "Anogenital region:Genital region:Perigenital region:Suprapubic region"
    )
    head_and_neck_head_ear_pinna_helix_of_pinna = "Head and neck:Head:Ear:Pinna:Helix of pinna"
    head_and_neck_head_ear_pinna_antihelix_of_pinna = (
        "Head and neck:Head:Ear:Pinna:Antihelix of pinna"
    )
    head_and_neck_head_ear_pinna_concha = "Head and neck:Head:Ear:Pinna:Concha"
    head_and_neck_head_face_orbital_region_periorbital_region = (
        "Head and neck:Head:Face:Orbital region:Periorbital region"
    )
    head_and_neck_head_face_orbital_region_eyelid = "Head and neck:Head:Face:Orbital region:Eyelid"
    head_and_neck_head_face_orbital_region_conjunctiva = (
        "Head and neck:Head:Face:Orbital region:Conjunctiva"
    )
    head_and_neck_head_face_orbital_region_sclera = "Head and neck:Head:Face:Orbital region:Sclera"
    head_and_neck_head_face_orbital_region_cornea = "Head and neck:Head:Face:Orbital region:Cornea"
    head_and_neck_head_face_orbital_region_iris = "Head and neck:Head:Face:Orbital region:Iris"
    head_and_neck_head_face_cheek_upper_cheek = "Head and neck:Head:Face:Cheek:Upper cheek"
    head_and_neck_head_face_cheek_central_cheek = "Head and neck:Head:Face:Cheek:Central cheek"
    head_and_neck_head_face_cheek_lateral_cheek = "Head and neck:Head:Face:Cheek:Lateral cheek"
    head_and_neck_head_face_cheek_lower_cheek = "Head and neck:Head:Face:Cheek:Lower cheek"
    head_and_neck_head_face_cheek_perinasal_region = (
        "Head and neck:Head:Face:Cheek:Perinasal region"
    )
    head_and_neck_head_face_nose_root_of_nose = "Head and neck:Head:Face:Nose:Root of nose"
    head_and_neck_head_face_nose_dorsum_of_nose = "Head and neck:Head:Face:Nose:Dorsum of nose"
    head_and_neck_head_face_nose_lateral_side_wall_of_nose = (
        "Head and neck:Head:Face:Nose:Lateral side wall of nose"
    )
    head_and_neck_head_face_nose_tip_of_nose = "Head and neck:Head:Face:Nose:Tip of nose"
    head_and_neck_head_face_nose_ala_nasi = "Head and neck:Head:Face:Nose:Ala nasi"
    head_and_neck_head_face_nose_nostril = "Head and neck:Head:Face:Nose:Nostril"
    head_and_neck_head_face_oral_region_perioral_region = (
        "Head and neck:Head:Face:Oral region:Perioral region"
    )
    head_and_neck_head_face_oral_region_lip = "Head and neck:Head:Face:Oral region:Lip"
    head_and_neck_head_face_oral_region_upper_lip = "Head and neck:Head:Face:Oral region:Upper lip"
    head_and_neck_head_face_oral_region_lower_lip = "Head and neck:Head:Face:Oral region:Lower lip"
    head_and_neck_head_face_oral_region_nasolabial_fold = (
        "Head and neck:Head:Face:Oral region:Nasolabial fold"
    )
    head_and_neck_head_face_mouth_oral_mucosa = "Head and neck:Head:Face:Mouth:Oral mucosa"
    head_and_neck_head_face_mouth_palate = "Head and neck:Head:Face:Mouth:Palate"
    head_and_neck_head_face_mouth_floor_of_mouth = "Head and neck:Head:Face:Mouth:Floor of mouth"
    head_and_neck_head_face_mouth_gingiva = "Head and neck:Head:Face:Mouth:Gingiva"
    head_and_neck_head_face_mouth_tongue = "Head and neck:Head:Face:Mouth:Tongue"
    head_and_neck_head_face_mouth_tonsillar_region = (
        "Head and neck:Head:Face:Mouth:Tonsillar region"
    )
    head_and_neck_head_face_mouth_oropharynx = "Head and neck:Head:Face:Mouth:Oropharynx"
    trunk_anterior_trunk_anterior_chest_upper_anterior_chest_clavicle = (
        "Trunk:Anterior trunk:Anterior chest:Upper anterior chest:Clavicle"
    )
    trunk_anterior_trunk_anterior_chest_upper_anterior_chest_infraclavicular_region = (
        "Trunk:Anterior trunk:Anterior chest:Upper anterior chest:Infraclavicular region"
    )
    trunk_anterior_trunk_anterior_chest_upper_anterior_chest_presternal_region = (
        "Trunk:Anterior trunk:Anterior chest:Upper anterior chest:Presternal region"
    )
    trunk_anterior_trunk_anterior_chest_breast_upper_outer_quadrant_of_breast = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Upper outer quadrant of breast"
    )
    trunk_anterior_trunk_anterior_chest_breast_upper_inner_quadrant_of_breast = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Upper inner quadrant of breast"
    )
    trunk_anterior_trunk_anterior_chest_breast_lower_outer_quadrant_of_breast = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Lower outer quadrant of breast"
    )
    trunk_anterior_trunk_anterior_chest_breast_lower_inner_quadrant_of_breast = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Lower inner quadrant of breast"
    )
    trunk_anterior_trunk_anterior_chest_breast_axillary_tail_of_breast = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Axillary tail of breast"
    )
    trunk_anterior_trunk_anterior_chest_breast_inframammary_flexure = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Inframammary flexure"
    )
    trunk_anterior_trunk_anterior_chest_breast_areola = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Areola"
    )
    trunk_anterior_trunk_anterior_chest_breast_nipple = (
        "Trunk:Anterior trunk:Anterior chest:Breast:Nipple"
    )
    trunk_anterior_trunk_anterior_abdomen_periumbilical_region_umbilicus = (
        "Trunk:Anterior trunk:Anterior abdomen:Periumbilical region:Umbilicus"
    )
    trunk_anterior_trunk_anterior_abdomen_lower_anterior_abdomen_hypogastric_region = (
        "Trunk:Anterior trunk:Anterior abdomen:Lower anterior abdomen:Hypogastric region"
    )
    trunk_anterior_trunk_anterior_abdomen_lower_anterior_abdomen_inguinal_region = (
        "Trunk:Anterior trunk:Anterior abdomen:Lower anterior abdomen:Inguinal region"
    )
    anogenital_region_genital_region_perigenital_region_suprapubic_region_mons_pubis = (
        "Anogenital region:Genital region:Perigenital region:Suprapubic region:Mons pubis"
    )

    @staticmethod
    @cache
    def levels(value: str) -> list[str | None]:
        levels_list = value.split(":")
        return levels_list + [None] * (5 - len(levels_list))

    @staticmethod
    @cache
    def as_dict(value: str) -> dict[str, str | None]:
        return {
            "anatom_site_1": AnatomSiteEnum.levels(value)[0],
            "anatom_site_2": AnatomSiteEnum.levels(value)[1],
            "anatom_site_3": AnatomSiteEnum.levels(value)[2],
            "anatom_site_4": AnatomSiteEnum.levels(value)[3],
            "anatom_site_5": AnatomSiteEnum.levels(value)[4],
        }

    @classmethod
    @cache
    def reverse_ordered_hierarchy(cls) -> list[Self]:
        return sorted(cls, key=lambda x: x.count(":"), reverse=True)

    @classmethod
    @cache
    def accept_terminal_values(cls, value: str) -> str:
        """
        Allow the user to specify any terminal value of the hierarchy to obtain the relevant value.

        e.g. "Scalp" can be used to obtain "Head and neck:Head:Scalp",
        or "Head" for "Head and neck:Head".
        """
        if ":" not in value:
            for member in cls.reverse_ordered_hierarchy():
                if value == member.split(":")[-1]:
                    return member

        return value

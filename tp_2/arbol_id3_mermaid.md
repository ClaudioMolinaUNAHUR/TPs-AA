# Árbol de decisión (ID3)

```mermaid
flowchart LR
classDef otorgado fill:#d4ffd4,stroke:#2e7d32,stroke-width:1px;
classDef rechazado fill:#ffd6d6,stroke:#c62828,stroke-width:1px;
classDef attr fill:#eef2ff,stroke:#4f46e5,stroke-width:1px;
Pr_stamos_previos_impagos_5d21fa15["Préstamos previos impagos"]
class Pr_stamos_previos_impagos_5d21fa15 attr;
RECHAZADO_58fc0ad5["RECHAZADO"]
class RECHAZADO_58fc0ad5 rechazado;
Pr_stamos_previos_impagos_5d21fa15 -- "SI" --> RECHAZADO_58fc0ad5
Estado_de_vivienda_3652e245["Estado de vivienda"]
class Estado_de_vivienda_3652e245 attr;
Pr_stamos_previos_impagos_5d21fa15 -- "NO" --> Estado_de_vivienda_3652e245
Mayor_nivel_educativo_c4c2b05a["Mayor nivel educativo"]
class Mayor_nivel_educativo_c4c2b05a attr;
Estado_de_vivienda_3652e245 -- "PROPIETARIO" --> Mayor_nivel_educativo_c4c2b05a
OTORGADO_34761ad2["OTORGADO"]
class OTORGADO_34761ad2 otorgado;
Mayor_nivel_educativo_c4c2b05a -- "DOCTORADO" --> OTORGADO_34761ad2
RECHAZADO_5ee0c34c["RECHAZADO"]
class RECHAZADO_5ee0c34c rechazado;
Mayor_nivel_educativo_c4c2b05a -- "MAESTRíA" --> RECHAZADO_5ee0c34c
RECHAZADO_82691658["RECHAZADO"]
class RECHAZADO_82691658 rechazado;
Mayor_nivel_educativo_c4c2b05a -- "UNIVERSITARIO" --> RECHAZADO_82691658
Destino_de_los_fondos_12c2061f["Destino de los fondos"]
class Destino_de_los_fondos_12c2061f attr;
Mayor_nivel_educativo_c4c2b05a -- "TERCIARIO" --> Destino_de_los_fondos_12c2061f
RECHAZADO_e64cc432["RECHAZADO"]
class RECHAZADO_e64cc432 rechazado;
Destino_de_los_fondos_12c2061f -- "PERSONAL" --> RECHAZADO_e64cc432
RECHAZADO_7e7da1b3["RECHAZADO"]
class RECHAZADO_7e7da1b3 rechazado;
Destino_de_los_fondos_12c2061f -- "EMPRESA" --> RECHAZADO_7e7da1b3
RECHAZADO_1a4ca648["RECHAZADO"]
class RECHAZADO_1a4ca648 rechazado;
Destino_de_los_fondos_12c2061f -- "SALUD" --> RECHAZADO_1a4ca648
Sexo_50393c52["Sexo"]
class Sexo_50393c52 attr;
Destino_de_los_fondos_12c2061f -- "EDUCACION" --> Sexo_50393c52
OTORGADO_1722eb66["OTORGADO"]
class OTORGADO_1722eb66 otorgado;
Sexo_50393c52 -- "MASCULINO" --> OTORGADO_1722eb66
Destino_de_los_fondos_75bb072f["Destino de los fondos"]
class Destino_de_los_fondos_75bb072f attr;
Mayor_nivel_educativo_c4c2b05a -- "SECUNDARIO" --> Destino_de_los_fondos_75bb072f
RECHAZADO_9340b1a1["RECHAZADO"]
class RECHAZADO_9340b1a1 rechazado;
Destino_de_los_fondos_75bb072f -- "EMPRESA" --> RECHAZADO_9340b1a1
RECHAZADO_67700700["RECHAZADO"]
class RECHAZADO_67700700 rechazado;
Destino_de_los_fondos_75bb072f -- "EDUCACION" --> RECHAZADO_67700700
RECHAZADO_8dc9247a["RECHAZADO"]
class RECHAZADO_8dc9247a rechazado;
Destino_de_los_fondos_75bb072f -- "PERSONAL" --> RECHAZADO_8dc9247a
Sexo_d3e7b1b9["Sexo"]
class Sexo_d3e7b1b9 attr;
Destino_de_los_fondos_75bb072f -- "VIVIENDA" --> Sexo_d3e7b1b9
OTORGADO_41301d36["OTORGADO"]
class OTORGADO_41301d36 otorgado;
Sexo_d3e7b1b9 -- "MASCULINO" --> OTORGADO_41301d36
RECHAZADO_a1d61c69["RECHAZADO"]
class RECHAZADO_a1d61c69 rechazado;
Sexo_d3e7b1b9 -- "FEMENINO" --> RECHAZADO_a1d61c69
Sexo_d40583e6["Sexo"]
class Sexo_d40583e6 attr;
Destino_de_los_fondos_75bb072f -- "SALUD" --> Sexo_d40583e6
RECHAZADO_6a07eec2["RECHAZADO"]
class RECHAZADO_6a07eec2 rechazado;
Sexo_d40583e6 -- "MASCULINO" --> RECHAZADO_6a07eec2
Destino_de_los_fondos_8a6c1391["Destino de los fondos"]
class Destino_de_los_fondos_8a6c1391 attr;
Estado_de_vivienda_3652e245 -- "HIPOTECA" --> Destino_de_los_fondos_8a6c1391
Mayor_nivel_educativo_b9321ba0["Mayor nivel educativo"]
class Mayor_nivel_educativo_b9321ba0 attr;
Destino_de_los_fondos_8a6c1391 -- "EMPRESA" --> Mayor_nivel_educativo_b9321ba0
RECHAZADO_0d06f2b0["RECHAZADO"]
class RECHAZADO_0d06f2b0 rechazado;
Mayor_nivel_educativo_b9321ba0 -- "DOCTORADO" --> RECHAZADO_0d06f2b0
RECHAZADO_dc66dc54["RECHAZADO"]
class RECHAZADO_dc66dc54 rechazado;
Mayor_nivel_educativo_b9321ba0 -- "MAESTRíA" --> RECHAZADO_dc66dc54
RECHAZADO_77cb8e92["RECHAZADO"]
class RECHAZADO_77cb8e92 rechazado;
Mayor_nivel_educativo_b9321ba0 -- "UNIVERSITARIO" --> RECHAZADO_77cb8e92
Sexo_4506eba5["Sexo"]
class Sexo_4506eba5 attr;
Mayor_nivel_educativo_b9321ba0 -- "TERCIARIO" --> Sexo_4506eba5
RECHAZADO_344c5b4d["RECHAZADO"]
class RECHAZADO_344c5b4d rechazado;
Sexo_4506eba5 -- "MASCULINO" --> RECHAZADO_344c5b4d
RECHAZADO_bdbfae05["RECHAZADO"]
class RECHAZADO_bdbfae05 rechazado;
Sexo_4506eba5 -- "FEMENINO" --> RECHAZADO_bdbfae05
Sexo_00b3d4c3["Sexo"]
class Sexo_00b3d4c3 attr;
Mayor_nivel_educativo_b9321ba0 -- "SECUNDARIO" --> Sexo_00b3d4c3
RECHAZADO_2ccc62ec["RECHAZADO"]
class RECHAZADO_2ccc62ec rechazado;
Sexo_00b3d4c3 -- "MASCULINO" --> RECHAZADO_2ccc62ec
Mayor_nivel_educativo_f688248a["Mayor nivel educativo"]
class Mayor_nivel_educativo_f688248a attr;
Destino_de_los_fondos_8a6c1391 -- "DEUDAS" --> Mayor_nivel_educativo_f688248a
OTORGADO_7d74a51b["OTORGADO"]
class OTORGADO_7d74a51b otorgado;
Mayor_nivel_educativo_f688248a -- "DOCTORADO" --> OTORGADO_7d74a51b
RECHAZADO_53314915["RECHAZADO"]
class RECHAZADO_53314915 rechazado;
Mayor_nivel_educativo_f688248a -- "MAESTRíA" --> RECHAZADO_53314915
Sexo_88a88db3["Sexo"]
class Sexo_88a88db3 attr;
Mayor_nivel_educativo_f688248a -- "UNIVERSITARIO" --> Sexo_88a88db3
RECHAZADO_08d59fe2["RECHAZADO"]
class RECHAZADO_08d59fe2 rechazado;
Sexo_88a88db3 -- "MASCULINO" --> RECHAZADO_08d59fe2
RECHAZADO_cdbe28aa["RECHAZADO"]
class RECHAZADO_cdbe28aa rechazado;
Sexo_88a88db3 -- "FEMENINO" --> RECHAZADO_cdbe28aa
Sexo_71dc2840["Sexo"]
class Sexo_71dc2840 attr;
Mayor_nivel_educativo_f688248a -- "TERCIARIO" --> Sexo_71dc2840
RECHAZADO_8d9fe0aa["RECHAZADO"]
class RECHAZADO_8d9fe0aa rechazado;
Sexo_71dc2840 -- "MASCULINO" --> RECHAZADO_8d9fe0aa
RECHAZADO_58a8b322["RECHAZADO"]
class RECHAZADO_58a8b322 rechazado;
Sexo_71dc2840 -- "FEMENINO" --> RECHAZADO_58a8b322
Sexo_191fb715["Sexo"]
class Sexo_191fb715 attr;
Mayor_nivel_educativo_f688248a -- "SECUNDARIO" --> Sexo_191fb715
RECHAZADO_05f33d6c["RECHAZADO"]
class RECHAZADO_05f33d6c rechazado;
Sexo_191fb715 -- "MASCULINO" --> RECHAZADO_05f33d6c
OTORGADO_a422d6b3["OTORGADO"]
class OTORGADO_a422d6b3 otorgado;
Sexo_191fb715 -- "FEMENINO" --> OTORGADO_a422d6b3
Mayor_nivel_educativo_9cdc6ecd["Mayor nivel educativo"]
class Mayor_nivel_educativo_9cdc6ecd attr;
Destino_de_los_fondos_8a6c1391 -- "EDUCACION" --> Mayor_nivel_educativo_9cdc6ecd
Sexo_c6a579d4["Sexo"]
class Sexo_c6a579d4 attr;
Mayor_nivel_educativo_9cdc6ecd -- "DOCTORADO" --> Sexo_c6a579d4
RECHAZADO_0203943b["RECHAZADO"]
class RECHAZADO_0203943b rechazado;
Sexo_c6a579d4 -- "MASCULINO" --> RECHAZADO_0203943b
RECHAZADO_9a2edc2a["RECHAZADO"]
class RECHAZADO_9a2edc2a rechazado;
Sexo_c6a579d4 -- "FEMENINO" --> RECHAZADO_9a2edc2a
OTORGADO_fbd839ae["OTORGADO"]
class OTORGADO_fbd839ae otorgado;
Mayor_nivel_educativo_9cdc6ecd -- "MAESTRíA" --> OTORGADO_fbd839ae
RECHAZADO_e8ee1c30["RECHAZADO"]
class RECHAZADO_e8ee1c30 rechazado;
Mayor_nivel_educativo_9cdc6ecd -- "UNIVERSITARIO" --> RECHAZADO_e8ee1c30
Sexo_18578f85["Sexo"]
class Sexo_18578f85 attr;
Mayor_nivel_educativo_9cdc6ecd -- "TERCIARIO" --> Sexo_18578f85
RECHAZADO_6c443861["RECHAZADO"]
class RECHAZADO_6c443861 rechazado;
Sexo_18578f85 -- "MASCULINO" --> RECHAZADO_6c443861
RECHAZADO_5cfc71d3["RECHAZADO"]
class RECHAZADO_5cfc71d3 rechazado;
Sexo_18578f85 -- "FEMENINO" --> RECHAZADO_5cfc71d3
Sexo_2f4302e6["Sexo"]
class Sexo_2f4302e6 attr;
Mayor_nivel_educativo_9cdc6ecd -- "SECUNDARIO" --> Sexo_2f4302e6
RECHAZADO_e1d2efd3["RECHAZADO"]
class RECHAZADO_e1d2efd3 rechazado;
Sexo_2f4302e6 -- "MASCULINO" --> RECHAZADO_e1d2efd3
RECHAZADO_fd978078["RECHAZADO"]
class RECHAZADO_fd978078 rechazado;
Sexo_2f4302e6 -- "FEMENINO" --> RECHAZADO_fd978078
Mayor_nivel_educativo_33e0b460["Mayor nivel educativo"]
class Mayor_nivel_educativo_33e0b460 attr;
Destino_de_los_fondos_8a6c1391 -- "PERSONAL" --> Mayor_nivel_educativo_33e0b460
Sexo_097e1025["Sexo"]
class Sexo_097e1025 attr;
Mayor_nivel_educativo_33e0b460 -- "DOCTORADO" --> Sexo_097e1025
RECHAZADO_eb7664bc["RECHAZADO"]
class RECHAZADO_eb7664bc rechazado;
Sexo_097e1025 -- "MASCULINO" --> RECHAZADO_eb7664bc
OTORGADO_d68e5fed["OTORGADO"]
class OTORGADO_d68e5fed otorgado;
Sexo_097e1025 -- "FEMENINO" --> OTORGADO_d68e5fed
Sexo_7c721456["Sexo"]
class Sexo_7c721456 attr;
Mayor_nivel_educativo_33e0b460 -- "MAESTRíA" --> Sexo_7c721456
OTORGADO_015b0a0e["OTORGADO"]
class OTORGADO_015b0a0e otorgado;
Sexo_7c721456 -- "MASCULINO" --> OTORGADO_015b0a0e
RECHAZADO_564d7d27["RECHAZADO"]
class RECHAZADO_564d7d27 rechazado;
Sexo_7c721456 -- "FEMENINO" --> RECHAZADO_564d7d27
Sexo_d22462c5["Sexo"]
class Sexo_d22462c5 attr;
Mayor_nivel_educativo_33e0b460 -- "UNIVERSITARIO" --> Sexo_d22462c5
RECHAZADO_eb71cca5["RECHAZADO"]
class RECHAZADO_eb71cca5 rechazado;
Sexo_d22462c5 -- "MASCULINO" --> RECHAZADO_eb71cca5
OTORGADO_83a1a7d5["OTORGADO"]
class OTORGADO_83a1a7d5 otorgado;
Sexo_d22462c5 -- "FEMENINO" --> OTORGADO_83a1a7d5
Sexo_c62c7c02["Sexo"]
class Sexo_c62c7c02 attr;
Mayor_nivel_educativo_33e0b460 -- "TERCIARIO" --> Sexo_c62c7c02
RECHAZADO_ad684b1c["RECHAZADO"]
class RECHAZADO_ad684b1c rechazado;
Sexo_c62c7c02 -- "MASCULINO" --> RECHAZADO_ad684b1c
RECHAZADO_9ec124be["RECHAZADO"]
class RECHAZADO_9ec124be rechazado;
Sexo_c62c7c02 -- "FEMENINO" --> RECHAZADO_9ec124be
Sexo_8e84941b["Sexo"]
class Sexo_8e84941b attr;
Mayor_nivel_educativo_33e0b460 -- "SECUNDARIO" --> Sexo_8e84941b
RECHAZADO_eaa22afc["RECHAZADO"]
class RECHAZADO_eaa22afc rechazado;
Sexo_8e84941b -- "MASCULINO" --> RECHAZADO_eaa22afc
RECHAZADO_ea736482["RECHAZADO"]
class RECHAZADO_ea736482 rechazado;
Sexo_8e84941b -- "FEMENINO" --> RECHAZADO_ea736482
Mayor_nivel_educativo_d803a70b["Mayor nivel educativo"]
class Mayor_nivel_educativo_d803a70b attr;
Destino_de_los_fondos_8a6c1391 -- "VIVIENDA" --> Mayor_nivel_educativo_d803a70b
Sexo_f7aae22a["Sexo"]
class Sexo_f7aae22a attr;
Mayor_nivel_educativo_d803a70b -- "SECUNDARIO" --> Sexo_f7aae22a
RECHAZADO_72fd4050["RECHAZADO"]
class RECHAZADO_72fd4050 rechazado;
Sexo_f7aae22a -- "MASCULINO" --> RECHAZADO_72fd4050
RECHAZADO_cc7a0990["RECHAZADO"]
class RECHAZADO_cc7a0990 rechazado;
Sexo_f7aae22a -- "FEMENINO" --> RECHAZADO_cc7a0990
Sexo_a34259c8["Sexo"]
class Sexo_a34259c8 attr;
Mayor_nivel_educativo_d803a70b -- "TERCIARIO" --> Sexo_a34259c8
RECHAZADO_ce7a2587["RECHAZADO"]
class RECHAZADO_ce7a2587 rechazado;
Sexo_a34259c8 -- "MASCULINO" --> RECHAZADO_ce7a2587
RECHAZADO_87f01416["RECHAZADO"]
class RECHAZADO_87f01416 rechazado;
Sexo_a34259c8 -- "FEMENINO" --> RECHAZADO_87f01416
Sexo_2d0a6870["Sexo"]
class Sexo_2d0a6870 attr;
Mayor_nivel_educativo_d803a70b -- "UNIVERSITARIO" --> Sexo_2d0a6870
RECHAZADO_c1668ab4["RECHAZADO"]
class RECHAZADO_c1668ab4 rechazado;
Sexo_2d0a6870 -- "MASCULINO" --> RECHAZADO_c1668ab4
OTORGADO_372c39a2["OTORGADO"]
class OTORGADO_372c39a2 otorgado;
Sexo_2d0a6870 -- "FEMENINO" --> OTORGADO_372c39a2
RECHAZADO_06847e0d["RECHAZADO"]
class RECHAZADO_06847e0d rechazado;
Mayor_nivel_educativo_d803a70b -- "DOCTORADO" --> RECHAZADO_06847e0d
Mayor_nivel_educativo_5670482d["Mayor nivel educativo"]
class Mayor_nivel_educativo_5670482d attr;
Destino_de_los_fondos_8a6c1391 -- "SALUD" --> Mayor_nivel_educativo_5670482d
Sexo_0c1e2585["Sexo"]
class Sexo_0c1e2585 attr;
Mayor_nivel_educativo_5670482d -- "DOCTORADO" --> Sexo_0c1e2585
RECHAZADO_e1644b10["RECHAZADO"]
class RECHAZADO_e1644b10 rechazado;
Sexo_0c1e2585 -- "MASCULINO" --> RECHAZADO_e1644b10
RECHAZADO_cee46bde["RECHAZADO"]
class RECHAZADO_cee46bde rechazado;
Sexo_0c1e2585 -- "FEMENINO" --> RECHAZADO_cee46bde
Sexo_7ccaa3e6["Sexo"]
class Sexo_7ccaa3e6 attr;
Mayor_nivel_educativo_5670482d -- "MAESTRíA" --> Sexo_7ccaa3e6
RECHAZADO_2add7614["RECHAZADO"]
class RECHAZADO_2add7614 rechazado;
Sexo_7ccaa3e6 -- "MASCULINO" --> RECHAZADO_2add7614
RECHAZADO_386fcfeb["RECHAZADO"]
class RECHAZADO_386fcfeb rechazado;
Sexo_7ccaa3e6 -- "FEMENINO" --> RECHAZADO_386fcfeb
Sexo_5c8e7abd["Sexo"]
class Sexo_5c8e7abd attr;
Mayor_nivel_educativo_5670482d -- "UNIVERSITARIO" --> Sexo_5c8e7abd
OTORGADO_6f9adb92["OTORGADO"]
class OTORGADO_6f9adb92 otorgado;
Sexo_5c8e7abd -- "MASCULINO" --> OTORGADO_6f9adb92
RECHAZADO_4b0a48a2["RECHAZADO"]
class RECHAZADO_4b0a48a2 rechazado;
Sexo_5c8e7abd -- "FEMENINO" --> RECHAZADO_4b0a48a2
Sexo_6551b048["Sexo"]
class Sexo_6551b048 attr;
Mayor_nivel_educativo_5670482d -- "TERCIARIO" --> Sexo_6551b048
RECHAZADO_e855b56d["RECHAZADO"]
class RECHAZADO_e855b56d rechazado;
Sexo_6551b048 -- "MASCULINO" --> RECHAZADO_e855b56d
RECHAZADO_041f7566["RECHAZADO"]
class RECHAZADO_041f7566 rechazado;
Sexo_6551b048 -- "FEMENINO" --> RECHAZADO_041f7566
Sexo_62dd1afc["Sexo"]
class Sexo_62dd1afc attr;
Mayor_nivel_educativo_5670482d -- "SECUNDARIO" --> Sexo_62dd1afc
RECHAZADO_498f8f20["RECHAZADO"]
class RECHAZADO_498f8f20 rechazado;
Sexo_62dd1afc -- "MASCULINO" --> RECHAZADO_498f8f20
RECHAZADO_e9acdd7b["RECHAZADO"]
class RECHAZADO_e9acdd7b rechazado;
Sexo_62dd1afc -- "FEMENINO" --> RECHAZADO_e9acdd7b
Mayor_nivel_educativo_66981af2["Mayor nivel educativo"]
class Mayor_nivel_educativo_66981af2 attr;
Estado_de_vivienda_3652e245 -- "INQUILINO" --> Mayor_nivel_educativo_66981af2
Destino_de_los_fondos_d9174387["Destino de los fondos"]
class Destino_de_los_fondos_d9174387 attr;
Mayor_nivel_educativo_66981af2 -- "DOCTORADO" --> Destino_de_los_fondos_d9174387
RECHAZADO_fea207d8["RECHAZADO"]
class RECHAZADO_fea207d8 rechazado;
Destino_de_los_fondos_d9174387 -- "EMPRESA" --> RECHAZADO_fea207d8
Sexo_c1aadd64["Sexo"]
class Sexo_c1aadd64 attr;
Destino_de_los_fondos_d9174387 -- "EDUCACION" --> Sexo_c1aadd64
RECHAZADO_e94b2070["RECHAZADO"]
class RECHAZADO_e94b2070 rechazado;
Sexo_c1aadd64 -- "MASCULINO" --> RECHAZADO_e94b2070
OTORGADO_ab811834["OTORGADO"]
class OTORGADO_ab811834 otorgado;
Sexo_c1aadd64 -- "FEMENINO" --> OTORGADO_ab811834
RECHAZADO_a65a7293["RECHAZADO"]
class RECHAZADO_a65a7293 rechazado;
Destino_de_los_fondos_d9174387 -- "PERSONAL" --> RECHAZADO_a65a7293
Sexo_77f71d00["Sexo"]
class Sexo_77f71d00 attr;
Destino_de_los_fondos_d9174387 -- "VIVIENDA" --> Sexo_77f71d00
OTORGADO_76fb0164["OTORGADO"]
class OTORGADO_76fb0164 otorgado;
Sexo_77f71d00 -- "MASCULINO" --> OTORGADO_76fb0164
OTORGADO_aea6e79c["OTORGADO"]
class OTORGADO_aea6e79c otorgado;
Sexo_77f71d00 -- "FEMENINO" --> OTORGADO_aea6e79c
Sexo_ded6732e["Sexo"]
class Sexo_ded6732e attr;
Destino_de_los_fondos_d9174387 -- "SALUD" --> Sexo_ded6732e
RECHAZADO_eaaea912["RECHAZADO"]
class RECHAZADO_eaaea912 rechazado;
Sexo_ded6732e -- "MASCULINO" --> RECHAZADO_eaaea912
RECHAZADO_34676cc8["RECHAZADO"]
class RECHAZADO_34676cc8 rechazado;
Sexo_ded6732e -- "FEMENINO" --> RECHAZADO_34676cc8
Destino_de_los_fondos_7294d626["Destino de los fondos"]
class Destino_de_los_fondos_7294d626 attr;
Mayor_nivel_educativo_66981af2 -- "MAESTRíA" --> Destino_de_los_fondos_7294d626
Sexo_52c38d06["Sexo"]
class Sexo_52c38d06 attr;
Destino_de_los_fondos_7294d626 -- "EMPRESA" --> Sexo_52c38d06
OTORGADO_db320715["OTORGADO"]
class OTORGADO_db320715 otorgado;
Sexo_52c38d06 -- "MASCULINO" --> OTORGADO_db320715
RECHAZADO_d513593f["RECHAZADO"]
class RECHAZADO_d513593f rechazado;
Sexo_52c38d06 -- "FEMENINO" --> RECHAZADO_d513593f
Sexo_76aba1af["Sexo"]
class Sexo_76aba1af attr;
Destino_de_los_fondos_7294d626 -- "DEUDAS" --> Sexo_76aba1af
RECHAZADO_2224a954["RECHAZADO"]
class RECHAZADO_2224a954 rechazado;
Sexo_76aba1af -- "MASCULINO" --> RECHAZADO_2224a954
RECHAZADO_6edf7b0f["RECHAZADO"]
class RECHAZADO_6edf7b0f rechazado;
Sexo_76aba1af -- "FEMENINO" --> RECHAZADO_6edf7b0f
Sexo_5f0fac92["Sexo"]
class Sexo_5f0fac92 attr;
Destino_de_los_fondos_7294d626 -- "EDUCACION" --> Sexo_5f0fac92
OTORGADO_00118a5f["OTORGADO"]
class OTORGADO_00118a5f otorgado;
Sexo_5f0fac92 -- "MASCULINO" --> OTORGADO_00118a5f
OTORGADO_9844f9cb["OTORGADO"]
class OTORGADO_9844f9cb otorgado;
Sexo_5f0fac92 -- "FEMENINO" --> OTORGADO_9844f9cb
Sexo_78ea1ead["Sexo"]
class Sexo_78ea1ead attr;
Destino_de_los_fondos_7294d626 -- "PERSONAL" --> Sexo_78ea1ead
OTORGADO_e0a51e9a["OTORGADO"]
class OTORGADO_e0a51e9a otorgado;
Sexo_78ea1ead -- "MASCULINO" --> OTORGADO_e0a51e9a
RECHAZADO_7be90425["RECHAZADO"]
class RECHAZADO_7be90425 rechazado;
Sexo_78ea1ead -- "FEMENINO" --> RECHAZADO_7be90425
Sexo_fc2f75fc["Sexo"]
class Sexo_fc2f75fc attr;
Destino_de_los_fondos_7294d626 -- "VIVIENDA" --> Sexo_fc2f75fc
OTORGADO_9c8188f6["OTORGADO"]
class OTORGADO_9c8188f6 otorgado;
Sexo_fc2f75fc -- "MASCULINO" --> OTORGADO_9c8188f6
OTORGADO_be1c431a["OTORGADO"]
class OTORGADO_be1c431a otorgado;
Sexo_fc2f75fc -- "FEMENINO" --> OTORGADO_be1c431a
Sexo_fcdbb527["Sexo"]
class Sexo_fcdbb527 attr;
Destino_de_los_fondos_7294d626 -- "SALUD" --> Sexo_fcdbb527
RECHAZADO_9688a374["RECHAZADO"]
class RECHAZADO_9688a374 rechazado;
Sexo_fcdbb527 -- "MASCULINO" --> RECHAZADO_9688a374
OTORGADO_7ac0b42e["OTORGADO"]
class OTORGADO_7ac0b42e otorgado;
Sexo_fcdbb527 -- "FEMENINO" --> OTORGADO_7ac0b42e
Destino_de_los_fondos_f5cad66a["Destino de los fondos"]
class Destino_de_los_fondos_f5cad66a attr;
Mayor_nivel_educativo_66981af2 -- "UNIVERSITARIO" --> Destino_de_los_fondos_f5cad66a
Sexo_cc19851f["Sexo"]
class Sexo_cc19851f attr;
Destino_de_los_fondos_f5cad66a -- "EMPRESA" --> Sexo_cc19851f
OTORGADO_2ea50d45["OTORGADO"]
class OTORGADO_2ea50d45 otorgado;
Sexo_cc19851f -- "MASCULINO" --> OTORGADO_2ea50d45
RECHAZADO_ef486ba5["RECHAZADO"]
class RECHAZADO_ef486ba5 rechazado;
Sexo_cc19851f -- "FEMENINO" --> RECHAZADO_ef486ba5
Sexo_e0997b34["Sexo"]
class Sexo_e0997b34 attr;
Destino_de_los_fondos_f5cad66a -- "DEUDAS" --> Sexo_e0997b34
OTORGADO_ce539e5d["OTORGADO"]
class OTORGADO_ce539e5d otorgado;
Sexo_e0997b34 -- "MASCULINO" --> OTORGADO_ce539e5d
RECHAZADO_188e1686["RECHAZADO"]
class RECHAZADO_188e1686 rechazado;
Sexo_e0997b34 -- "FEMENINO" --> RECHAZADO_188e1686
Sexo_55eb9c85["Sexo"]
class Sexo_55eb9c85 attr;
Destino_de_los_fondos_f5cad66a -- "EDUCACION" --> Sexo_55eb9c85
OTORGADO_876117a1["OTORGADO"]
class OTORGADO_876117a1 otorgado;
Sexo_55eb9c85 -- "MASCULINO" --> OTORGADO_876117a1
RECHAZADO_4c027ae7["RECHAZADO"]
class RECHAZADO_4c027ae7 rechazado;
Sexo_55eb9c85 -- "FEMENINO" --> RECHAZADO_4c027ae7
Sexo_f40f95f2["Sexo"]
class Sexo_f40f95f2 attr;
Destino_de_los_fondos_f5cad66a -- "PERSONAL" --> Sexo_f40f95f2
RECHAZADO_9abc1ef7["RECHAZADO"]
class RECHAZADO_9abc1ef7 rechazado;
Sexo_f40f95f2 -- "MASCULINO" --> RECHAZADO_9abc1ef7
RECHAZADO_1c7bfdc3["RECHAZADO"]
class RECHAZADO_1c7bfdc3 rechazado;
Sexo_f40f95f2 -- "FEMENINO" --> RECHAZADO_1c7bfdc3
Sexo_85b7235a["Sexo"]
class Sexo_85b7235a attr;
Destino_de_los_fondos_f5cad66a -- "VIVIENDA" --> Sexo_85b7235a
OTORGADO_419e36df["OTORGADO"]
class OTORGADO_419e36df otorgado;
Sexo_85b7235a -- "MASCULINO" --> OTORGADO_419e36df
OTORGADO_bab69d6f["OTORGADO"]
class OTORGADO_bab69d6f otorgado;
Sexo_85b7235a -- "FEMENINO" --> OTORGADO_bab69d6f
Sexo_ac2d883a["Sexo"]
class Sexo_ac2d883a attr;
Destino_de_los_fondos_f5cad66a -- "SALUD" --> Sexo_ac2d883a
OTORGADO_b4333f7a["OTORGADO"]
class OTORGADO_b4333f7a otorgado;
Sexo_ac2d883a -- "MASCULINO" --> OTORGADO_b4333f7a
RECHAZADO_11e7fc63["RECHAZADO"]
class RECHAZADO_11e7fc63 rechazado;
Sexo_ac2d883a -- "FEMENINO" --> RECHAZADO_11e7fc63
Destino_de_los_fondos_0904b113["Destino de los fondos"]
class Destino_de_los_fondos_0904b113 attr;
Mayor_nivel_educativo_66981af2 -- "TERCIARIO" --> Destino_de_los_fondos_0904b113
Sexo_c21b127e["Sexo"]
class Sexo_c21b127e attr;
Destino_de_los_fondos_0904b113 -- "EMPRESA" --> Sexo_c21b127e
RECHAZADO_c00902ec["RECHAZADO"]
class RECHAZADO_c00902ec rechazado;
Sexo_c21b127e -- "MASCULINO" --> RECHAZADO_c00902ec
RECHAZADO_7c460e5a["RECHAZADO"]
class RECHAZADO_7c460e5a rechazado;
Sexo_c21b127e -- "FEMENINO" --> RECHAZADO_7c460e5a
Sexo_fcc278bb["Sexo"]
class Sexo_fcc278bb attr;
Destino_de_los_fondos_0904b113 -- "DEUDAS" --> Sexo_fcc278bb
RECHAZADO_b5cbd82b["RECHAZADO"]
class RECHAZADO_b5cbd82b rechazado;
Sexo_fcc278bb -- "MASCULINO" --> RECHAZADO_b5cbd82b
OTORGADO_37ef7695["OTORGADO"]
class OTORGADO_37ef7695 otorgado;
Sexo_fcc278bb -- "FEMENINO" --> OTORGADO_37ef7695
Sexo_ccef87f5["Sexo"]
class Sexo_ccef87f5 attr;
Destino_de_los_fondos_0904b113 -- "EDUCACION" --> Sexo_ccef87f5
RECHAZADO_b189bbd4["RECHAZADO"]
class RECHAZADO_b189bbd4 rechazado;
Sexo_ccef87f5 -- "MASCULINO" --> RECHAZADO_b189bbd4
RECHAZADO_c89bd85f["RECHAZADO"]
class RECHAZADO_c89bd85f rechazado;
Sexo_ccef87f5 -- "FEMENINO" --> RECHAZADO_c89bd85f
Sexo_3f4942bf["Sexo"]
class Sexo_3f4942bf attr;
Destino_de_los_fondos_0904b113 -- "PERSONAL" --> Sexo_3f4942bf
OTORGADO_7f358bc8["OTORGADO"]
class OTORGADO_7f358bc8 otorgado;
Sexo_3f4942bf -- "MASCULINO" --> OTORGADO_7f358bc8
RECHAZADO_0d3d5a0e["RECHAZADO"]
class RECHAZADO_0d3d5a0e rechazado;
Sexo_3f4942bf -- "FEMENINO" --> RECHAZADO_0d3d5a0e
Sexo_f82ebe21["Sexo"]
class Sexo_f82ebe21 attr;
Destino_de_los_fondos_0904b113 -- "VIVIENDA" --> Sexo_f82ebe21
OTORGADO_7594f499["OTORGADO"]
class OTORGADO_7594f499 otorgado;
Sexo_f82ebe21 -- "MASCULINO" --> OTORGADO_7594f499
OTORGADO_1c989724["OTORGADO"]
class OTORGADO_1c989724 otorgado;
Sexo_f82ebe21 -- "FEMENINO" --> OTORGADO_1c989724
Sexo_ec444bbd["Sexo"]
class Sexo_ec444bbd attr;
Destino_de_los_fondos_0904b113 -- "SALUD" --> Sexo_ec444bbd
OTORGADO_0064b06f["OTORGADO"]
class OTORGADO_0064b06f otorgado;
Sexo_ec444bbd -- "MASCULINO" --> OTORGADO_0064b06f
RECHAZADO_12275126["RECHAZADO"]
class RECHAZADO_12275126 rechazado;
Sexo_ec444bbd -- "FEMENINO" --> RECHAZADO_12275126
Destino_de_los_fondos_f6c15e16["Destino de los fondos"]
class Destino_de_los_fondos_f6c15e16 attr;
Mayor_nivel_educativo_66981af2 -- "SECUNDARIO" --> Destino_de_los_fondos_f6c15e16
Sexo_3a6b46d1["Sexo"]
class Sexo_3a6b46d1 attr;
Destino_de_los_fondos_f6c15e16 -- "EMPRESA" --> Sexo_3a6b46d1
RECHAZADO_a66f0b7a["RECHAZADO"]
class RECHAZADO_a66f0b7a rechazado;
Sexo_3a6b46d1 -- "MASCULINO" --> RECHAZADO_a66f0b7a
OTORGADO_7bab342d["OTORGADO"]
class OTORGADO_7bab342d otorgado;
Sexo_3a6b46d1 -- "FEMENINO" --> OTORGADO_7bab342d
Sexo_0a377c89["Sexo"]
class Sexo_0a377c89 attr;
Destino_de_los_fondos_f6c15e16 -- "DEUDAS" --> Sexo_0a377c89
OTORGADO_b92be825["OTORGADO"]
class OTORGADO_b92be825 otorgado;
Sexo_0a377c89 -- "MASCULINO" --> OTORGADO_b92be825
OTORGADO_e515511b["OTORGADO"]
class OTORGADO_e515511b otorgado;
Sexo_0a377c89 -- "FEMENINO" --> OTORGADO_e515511b
Sexo_49181de1["Sexo"]
class Sexo_49181de1 attr;
Destino_de_los_fondos_f6c15e16 -- "EDUCACION" --> Sexo_49181de1
OTORGADO_a88e5913["OTORGADO"]
class OTORGADO_a88e5913 otorgado;
Sexo_49181de1 -- "MASCULINO" --> OTORGADO_a88e5913
OTORGADO_d502bba9["OTORGADO"]
class OTORGADO_d502bba9 otorgado;
Sexo_49181de1 -- "FEMENINO" --> OTORGADO_d502bba9
Sexo_84373768["Sexo"]
class Sexo_84373768 attr;
Destino_de_los_fondos_f6c15e16 -- "PERSONAL" --> Sexo_84373768
RECHAZADO_8704f1a8["RECHAZADO"]
class RECHAZADO_8704f1a8 rechazado;
Sexo_84373768 -- "MASCULINO" --> RECHAZADO_8704f1a8
OTORGADO_7796082a["OTORGADO"]
class OTORGADO_7796082a otorgado;
Sexo_84373768 -- "FEMENINO" --> OTORGADO_7796082a
Sexo_6bae667c["Sexo"]
class Sexo_6bae667c attr;
Destino_de_los_fondos_f6c15e16 -- "VIVIENDA" --> Sexo_6bae667c
OTORGADO_09454ba3["OTORGADO"]
class OTORGADO_09454ba3 otorgado;
Sexo_6bae667c -- "MASCULINO" --> OTORGADO_09454ba3
OTORGADO_f0e59deb["OTORGADO"]
class OTORGADO_f0e59deb otorgado;
Sexo_6bae667c -- "FEMENINO" --> OTORGADO_f0e59deb
Sexo_f80cad7e["Sexo"]
class Sexo_f80cad7e attr;
Destino_de_los_fondos_f6c15e16 -- "SALUD" --> Sexo_f80cad7e
RECHAZADO_2d9c338e["RECHAZADO"]
class RECHAZADO_2d9c338e rechazado;
Sexo_f80cad7e -- "MASCULINO" --> RECHAZADO_2d9c338e
OTORGADO_05c75c06["OTORGADO"]
class OTORGADO_05c75c06 otorgado;
Sexo_f80cad7e -- "FEMENINO" --> OTORGADO_05c75c06
Mayor_nivel_educativo_b9f41ab0["Mayor nivel educativo"]
class Mayor_nivel_educativo_b9f41ab0 attr;
Estado_de_vivienda_3652e245 -- "OTRO" --> Mayor_nivel_educativo_b9f41ab0
RECHAZADO_9abaab7c["RECHAZADO"]
class RECHAZADO_9abaab7c rechazado;
Mayor_nivel_educativo_b9f41ab0 -- "UNIVERSITARIO" --> RECHAZADO_9abaab7c
OTORGADO_a13a4a2c["OTORGADO"]
class OTORGADO_a13a4a2c otorgado;
Mayor_nivel_educativo_b9f41ab0 -- "SECUNDARIO" --> OTORGADO_a13a4a2c
Destino_de_los_fondos_f763adbe["Destino de los fondos"]
class Destino_de_los_fondos_f763adbe attr;
Mayor_nivel_educativo_b9f41ab0 -- "TERCIARIO" --> Destino_de_los_fondos_f763adbe
OTORGADO_1d656aeb["OTORGADO"]
class OTORGADO_1d656aeb otorgado;
Destino_de_los_fondos_f763adbe -- "PERSONAL" --> OTORGADO_1d656aeb
RECHAZADO_56b35ba2["RECHAZADO"]
class RECHAZADO_56b35ba2 rechazado;
Destino_de_los_fondos_f763adbe -- "VIVIENDA" --> RECHAZADO_56b35ba2
OTORGADO_2dedb869["OTORGADO"]
class OTORGADO_2dedb869 otorgado;
Destino_de_los_fondos_f763adbe -- "EDUCACION" --> OTORGADO_2dedb869
```

[![](https://mermaid.ink/img/pako:eNqlXe1u3TiSfRXjzt_0QKT4JQ-wgGF7dwx04qyd9I9ZLwx-KW1MYgeOk-meRj_Q_tinmBdb5V4eNWmJKskLBEhsHp4qlorFYpFSftv5hxB3x7ub-_7jwz_8z_bx6ejd2c29_2i_fDmL_dHD08PjBxsejvq7jx-P_xRE3wfx6svT48Pf4_GfeNSh5enHH_5xF55-Pmaff_lLRvAYB9Z__sEw9FdBjQxeccPNIoN9enpMnWPsed-PnUUvVJRznd8-3n55sp8evtx-fozf7oa_7z59th-Gv2XgrLdM_tfN7u3jv_7ngDpKqKOEutn9d1LgiGbaKzjIvDo__evJ307OLm-l6X1jw3cZ4y8zyinwDyut0v3ohx-ObnbXFze74V__NsN3c38-UISH2xBvv919u4v3wd62SvLIxXetDq1HIR6hNVNvoSuGulbFN5dJxQXOm_vX9teHx9v7u2_x420MX719uvv2cOuF566RdlB3DzjaA45GQKbxMgGUXhrXXtu3V5dvL87fnVxdQO1l4pv7y3eXV__x3fCt0IrZwAdl8btMvwlsnFZ_oUZ_0Ozs8nSg2JPu9ZoQFt4XY-Nb4WnvS8DC-9ao8_rk_Prd1b_-92TqgIky18dw1TElDakPgJv1ef_m4qfzq-uL_NFNaW_uz-KXp7v7vQt8HHy1f7gPw1-Me94o1g_6JcD3iTEAjg6ATNdlAjjaGpXfnV-dXmTqLjPn5oxKeC9aTpoTwMKcxAgO82Cw5eWbkx8nlgRjro4elgDLXEuqA-Bmdc5fv706v576GghzbZgV3ipB-xqAm7W5Pvnx_dlEF9Dd3F_HXx5uZdN2rZffn9H3nzMNimY4zCornL0_PTm9uHyTZBdEWSRimvPolCIiEWB5JCp1SzP9-vT9jxdvJoEH_WvKa-lco_nLJxUItkyq6_PT92_OyFkF6txxulY0jllGOg6AKxxnHMKiG4Mw10Zp3TTDH1IbALdr88ydppRFCA--40JbOoQn4GZ9qjEHjMk9Qxu1Y66rzCw0L8-sUvRPFz9dnA9uk08s8GQTS7C2YaGlJhZgk4k1qrY8sdA_N79lQTGvOtL8ABbmn5H-7-evz9_8IXxKgF6ikaaNqmbt1LzF2nn8LEgK_7eNjtHTaxyAMwOGbrPmnjLUtDdWedZ27MWBDASr09C_Xry9fHd-erIYw8BaC4yuazlztnlx9gyC5Wc7Dm4mxC3z5o-7CY3qhzhOPm4AV2SIo_6zCfSUMtcneKWCl4LUB8DN-tQzaFAWOZb2zsSOng4AbtZnOYMGbZpaQjYqOisrUQHNyyt3Kf95OlwQ5aZohfDSiUCaAsBpZBj1IyIDGHLxLrjexobe2QNIia9GYhCkXk3j2iB8W7E5mrfYfJItFUz5qLn3XvFI7ygBnI56VJAwOhhqQ-iVMVyYl1cFQLAlrp2dvz87uV4Ma6DNEgYdtLCSOSJhAIyuCYyqL9cEQFjUBNqWiY6tqEgl4IoIUqqzUBNIlMkTjLHGBFfzZDQve3Ipey56FWTFYmOC7PpIB1MAp8486kg4Mxhy8T64yI2lU2kAKfHVCAKC1Euz4LkRTcXuaN5i99moDaJy_zCYobFr9g8H4HTQo36EzcFQ1mOtcS3nK-qxByAlvmpzEKRerGO906y2UqJ5i83nozaYCkeXfdsGRUdtAKejHhWkHD0xZNHPCs6D2k_zpegH2GS7VIp-ZvBJ95rtOj_kU9GHFy8XINiUBj_bWy8zp_F6ZaXugqi4CpqXXWXUdnaFKIgKT-FN24nW0Z6SgFNPGfWjPCUxFLUXy-Mwu-joACAlvjo9QZD5ae-CaTsbCT8FjF6ly2fwfFmcEBalXRMj8y29DwJwxSpdqrOc54MWU9BIbXpTjV6peYtLzq4YICoqAF6I1ii6HgfgTPCCflQFIDEUK4bv_RDy6ao2gJT4-oqRCFIv3ou24dWKC5q32Hx-xQBT4X8s8NivGDWA01GPChJGB0Muvg-dNo2mi_cAUuKrRgdBzYBtGxsn1MurJyDYsmw8K4EuE2Nb1enIGl6bomhedpdR2fqqAaLCW5xWSjg6vwBwZlcI_ShvSQxZ3A7KRNnHQMRtwCb5RSm6ll-gO7JArzkTsjY70bzF3M8XiIIoG2_DpGtsQ61TgE3GO-q2XH5G_yIYKhF04JoOhgk4kz4X0uvBMBGghsu5UNzXvBvNW8xd3SqC7JmHM--tXOPhe-BMGRo60h6-Z8ieuGkts3p_i2TpiQM2PXAoRNc8HN3HRIp77RteTUMPzVtMPrvmg6g45hhmm3CMDigAzuWBST_C3GAo0tDoGRcu0mloAlLi62loIsB-PhrRiX2haLYikpq32Hx-zQdT4ePWcm77FVE8AWfqEVCQ8vHEUIrXrRJmxW2GBKTEV40OgpoBg2laqxv34jUfBFvW_Gdnj8vEaby9tjby_XZpzl3QvOwuo7IL7gKm4iiC999P1ugtCoDT5zUqSLgLGIrqmde26TpaPICU-Hr1LBGkXrYVXHbeVIyO5i1Gn42LICoGHbXl0tDrL4DTQY_6ETYHQ1G8033DBFN08S4BKfFVm4MAyXxorDK6VrFE8xabV5d_kBV2Z0oZ6-hjQABn9iPQkbJ7YsivFGru286SVwoTbLL8l6Jryz-6F-WgYW3UsaHP2ABcUYYoH8PCcWyirPFIpZshiL-8oAeCLVE6v7OwzIrNhWdxmEbVbVlqXvbcUdOFbVkiKjfxSgypzYoiUgLObMugH7mJPzCUwSoK5UJcEawOQEp8PUIngnGL4a2t31VB8xabV_ZmB6LigNSGoBWjIwWAczukpB91QJoYikNxo3rfR7p-CyAlvmpzEOCyoDfDguFC7Z5jat5i82qEBlkWIlXf2eA6KkQCNr3rCP2W98Ton5tcDLtkYSydtwI4NXkpvWpyEKReSkrmGlFLRNC8xeSziQiIyvq0lE6qsKI-fQBOBz3qR4WWxFCsS4L1Wio6EQGQEl-1OQjQi4fADnukWZun5i02n8-4wVR4Wmd603M6ngM4M2ooSBgdDMUz76wfIg4dWwCkxNc3aImgZkClOjPQ8Bcv_SBYfRPv4s1_vr_ILLVMW8slQse0aPfp-8tuEIJg2b_G0c2mC8vMRRU-Wt7osKIKn4Ar7vqOI1i8CQ1CFFOYHdY6VT0RTc3LidwzyXOX6EFUer1wgy4rkqgEnKkFQT8q0iWG_OzcGcZMK6iz8wSbrGul6OrZeepelOCUtJp39AkQgJsffvWiNxiRkOhes9BUr6uk5i1Pf-6iN3jye1uqdw1TlPUBm1baodpyVoH--XOPVkXdeeq5JxghufrcU3eUiWNQuuWxVmRPzVsMPb3jnUieFR6j7diayt8BOFNch2504XHPUF4kVVp5b1ZcJD0AKfH1nDkRVO_H804ExdXLX5VJBFvWh-dbm2VmZKzctyY0tS0WmonXAaDtzFpQ0OSHfa4dQiSjjkIAmyb60Gx5SqJ_cRdcslZ2bU_fBU_AmUS_kF71ExBgMivr7PDAagEwNW8xdnGPtWApNrOcC9utuP0O4MxuEspRm9nEUNz8iKHXrqENDiAlvmpwEOAx9U1vfVd9aS81b_Lu2Zf2ElF-uNsMK7GVPXW4m2BT_4ZuxOFu6p9J7owQfeepS8qAEZJrSw664_mYaFm0tbIBmrdY-llaUfBkw42NlWzYaBDDBWy6wkK1ZUOjf3Fy4mLXCE4fJgM449eF9KpfgwAHHp4Pm9nq7hXNW6w9l0mBJ3cub5gxPfXKHGATa4-qLVsb_TPJLjIvWkY9Z8AIyTW3RvexU3BO7u9JzBv60LzF0JNMCiTFwbUyxraaDtgAzhyKQTciYIMhT5etb5zg1MUUwGZMnYuumRrda2brpbdBKfviJAoEW5KouVrlMjs2aJ51RrLa2o7mZU8ZNa4lUqDJHhaPVjZBUIkUYNOdJTRbnpHoX-T7vTDKrblMk4AzW-pCer2QlAhSr9h0nXZtrY6A5i3GniZSYMls7aNsuyipG2qATWw9KrZsa_QvPoNgTGTK0JVSAKe2LqVXbQ0CpAMyuiEc1w6-0LzJsWdzqESUX5fSijG9f4N_8bpUgk0zGei2bG70L0q0vuHaRvqAHsCZPUIhvX4YkAgQO0XTd7Kvpaxo3mLuuUQKPOWlfedZ7PWKS_sH4MyiA_WoRScxFB7uteuDpwtVAFLi6x6eCHDbSDrNW1m7fYPmLSafy6bAU3yAoIutCj35AYIDbOLgo2rUBwgO_fNsyjrVBUVJBoyQXM2mUnfcGfE8GNPWDI3mLYaeZFMgyccq2rbtNZk5JthkrKNey1ZG_8KnWdS9Vyt8OgFnLtoU0us-nQhqZmuG_YNjrH1xNgWCLdnUuk8igRkpAWeOcV2rXqJ52UtGbauZVKIpLjo0Q7c1L0UDOJPPQDvqdlBiKLaTXqgmSvqlKQAp8fXtZCIY83XPtXGuuss5NG-x-DSdAkvx7r30LhhOn0QCOLfNScoRBgdDcR1rWIFUJ8nrWAfYzDYnF12_jnXoPia8sTe6l9V9wqF5k3fPHoElosLczHTOBXpXCeBcvp70o8ydGIrpNfwqGEmXAQGkxNfvESWC1KvtRSe4q-3N0LzF5nM5FXjynXTfSuP2RxKLO-kEm7jYqBpx8JT6l19gaYM8vF1CfYHlAJxau5Rev1qRCDAtDI8uclaLJql5i7Vni1OJJ7e27MSgckdZO8GmExqqEdZO_fNPtPnOdJpTB4yAEZJroQTdsZ_zQghXvaqF5i2GnqRTICkq20q4RtGV7QNsugmGXlRl-9C_SKc415LxFZvgBJzZBBfS6-lUIqhmocozGdnLT_hAsCWdWvkxPFBjFlvlhAq1-YhmIuuGurV8CjTl1QPVN27FN-YAnAlB0I56-ycx5NFg2H20glPFGsCmsbcQXa1ipu646GpbrYflp3ZNODVvMfY0lQJLvsfpuIuGU7kMYNN3J6EYscdJ_fPzF8mkZOQ3cQAjJNfMjO744lLHDAux5tNo3uTTc1kUiPIbHcZE2THyKxgJNhnvqNuypdE_PzKXDXfOUssbYITk6vuxqTs2-qLVrVa1y6lo3mLpudwJPOVbKo3omV3xleEEnHmRDOpRn5hJDHn40J1qDKeqBoBNKySF6Gr4SN1xr9LZqJSuXktNzVusPZc7gSdf1TshhbOUWwM2Ge6oGrGqp_755zqGnWgXIhVAACMk1wyN7mPC1XgbqkUGNG8x9PRgL5EUNzFC59vW0Fk5gDM7XuhG3cRIDPlDll5L31Cnt4DNpKm56Jqp0b3-zbpeMOv-Px-yPBCsvvV7-e7qkviE5YHxWTncWqf9mnL4HrjqE41J8xWfbgFtvvaw1grLyduECUZ_2abUZ5JfThirM0Gr1ob9i9YvTIcTAfW1w1zdddVFMOe7taCksmTEASw3I6H93Po24Ss_xOBa6Va8dALgitu5pTbP4v-UMT9LDjE4o6gMA7CthnmeYk0Ib-5v7nevdp_i4yd7F3bHu99u7o-Gjk8_x0_xZnc8_DPYx7_f7G7ufx9w9uvTw_Wv9353_PT4Nb7aPT58_fDz7ri3H78MP339HOxTPLuzHx7tJ0A-2_u_PTzkP-6Of9v9sjvmovsz061oJGsYU1K-2v06_JYNvzVMsLbrWt617PdXu3_u-zd_VpyrYfk2zMhWGMle7WK4Gwzy-vD_r-z_G5ZXuw-P3weS9BtCU3w8ffh6_7Sn_v3_ABVt8NQ?type=png)](https://mermaid.live/edit#pako:eNqlXe1u3TiSfRXjzt_0QKT4JQ-wgGF7dwx04qyd9I9ZLwx-KW1MYgeOk-meRj_Q_tinmBdb5V4eNWmJKskLBEhsHp4qlorFYpFSftv5hxB3x7ub-_7jwz_8z_bx6ejd2c29_2i_fDmL_dHD08PjBxsejvq7jx-P_xRE3wfx6svT48Pf4_GfeNSh5enHH_5xF55-Pmaff_lLRvAYB9Z__sEw9FdBjQxeccPNIoN9enpMnWPsed-PnUUvVJRznd8-3n55sp8evtx-fozf7oa_7z59th-Gv2XgrLdM_tfN7u3jv_7ngDpKqKOEutn9d1LgiGbaKzjIvDo__evJ307OLm-l6X1jw3cZ4y8zyinwDyut0v3ohx-ObnbXFze74V__NsN3c38-UISH2xBvv919u4v3wd62SvLIxXetDq1HIR6hNVNvoSuGulbFN5dJxQXOm_vX9teHx9v7u2_x420MX719uvv2cOuF566RdlB3DzjaA45GQKbxMgGUXhrXXtu3V5dvL87fnVxdQO1l4pv7y3eXV__x3fCt0IrZwAdl8btMvwlsnFZ_oUZ_0Ozs8nSg2JPu9ZoQFt4XY-Nb4WnvS8DC-9ao8_rk_Prd1b_-92TqgIky18dw1TElDakPgJv1ef_m4qfzq-uL_NFNaW_uz-KXp7v7vQt8HHy1f7gPw1-Me94o1g_6JcD3iTEAjg6ATNdlAjjaGpXfnV-dXmTqLjPn5oxKeC9aTpoTwMKcxAgO82Cw5eWbkx8nlgRjro4elgDLXEuqA-Bmdc5fv706v576GghzbZgV3ipB-xqAm7W5Pvnx_dlEF9Dd3F_HXx5uZdN2rZffn9H3nzMNimY4zCornL0_PTm9uHyTZBdEWSRimvPolCIiEWB5JCp1SzP9-vT9jxdvJoEH_WvKa-lco_nLJxUItkyq6_PT92_OyFkF6txxulY0jllGOg6AKxxnHMKiG4Mw10Zp3TTDH1IbALdr88ydppRFCA--40JbOoQn4GZ9qjEHjMk9Qxu1Y66rzCw0L8-sUvRPFz9dnA9uk08s8GQTS7C2YaGlJhZgk4k1qrY8sdA_N79lQTGvOtL8ABbmn5H-7-evz9_8IXxKgF6ikaaNqmbt1LzF2nn8LEgK_7eNjtHTaxyAMwOGbrPmnjLUtDdWedZ27MWBDASr09C_Xry9fHd-erIYw8BaC4yuazlztnlx9gyC5Wc7Dm4mxC3z5o-7CY3qhzhOPm4AV2SIo_6zCfSUMtcneKWCl4LUB8DN-tQzaFAWOZb2zsSOng4AbtZnOYMGbZpaQjYqOisrUQHNyyt3Kf95OlwQ5aZohfDSiUCaAsBpZBj1IyIDGHLxLrjexobe2QNIia9GYhCkXk3j2iB8W7E5mrfYfJItFUz5qLn3XvFI7ygBnI56VJAwOhhqQ-iVMVyYl1cFQLAlrp2dvz87uV4Ma6DNEgYdtLCSOSJhAIyuCYyqL9cEQFjUBNqWiY6tqEgl4IoIUqqzUBNIlMkTjLHGBFfzZDQve3Ipey56FWTFYmOC7PpIB1MAp8486kg4Mxhy8T64yI2lU2kAKfHVCAKC1Euz4LkRTcXuaN5i99moDaJy_zCYobFr9g8H4HTQo36EzcFQ1mOtcS3nK-qxByAlvmpzEKRerGO906y2UqJ5i83nozaYCkeXfdsGRUdtAKejHhWkHD0xZNHPCs6D2k_zpegH2GS7VIp-ZvBJ95rtOj_kU9GHFy8XINiUBj_bWy8zp_F6ZaXugqi4CpqXXWXUdnaFKIgKT-FN24nW0Z6SgFNPGfWjPCUxFLUXy-Mwu-joACAlvjo9QZD5ae-CaTsbCT8FjF6ly2fwfFmcEBalXRMj8y29DwJwxSpdqrOc54MWU9BIbXpTjV6peYtLzq4YICoqAF6I1ii6HgfgTPCCflQFIDEUK4bv_RDy6ao2gJT4-oqRCFIv3ou24dWKC5q32Hx-xQBT4X8s8NivGDWA01GPChJGB0Muvg-dNo2mi_cAUuKrRgdBzYBtGxsn1MurJyDYsmw8K4EuE2Nb1enIGl6bomhedpdR2fqqAaLCW5xWSjg6vwBwZlcI_ShvSQxZ3A7KRNnHQMRtwCb5RSm6ll-gO7JArzkTsjY70bzF3M8XiIIoG2_DpGtsQ61TgE3GO-q2XH5G_yIYKhF04JoOhgk4kz4X0uvBMBGghsu5UNzXvBvNW8xd3SqC7JmHM--tXOPhe-BMGRo60h6-Z8ieuGkts3p_i2TpiQM2PXAoRNc8HN3HRIp77RteTUMPzVtMPrvmg6g45hhmm3CMDigAzuWBST_C3GAo0tDoGRcu0mloAlLi62loIsB-PhrRiX2haLYikpq32Hx-zQdT4ePWcm77FVE8AWfqEVCQ8vHEUIrXrRJmxW2GBKTEV40OgpoBg2laqxv34jUfBFvW_Gdnj8vEaby9tjby_XZpzl3QvOwuo7IL7gKm4iiC999P1ugtCoDT5zUqSLgLGIrqmde26TpaPICU-Hr1LBGkXrYVXHbeVIyO5i1Gn42LICoGHbXl0tDrL4DTQY_6ETYHQ1G8033DBFN08S4BKfFVm4MAyXxorDK6VrFE8xabV5d_kBV2Z0oZ6-hjQABn9iPQkbJ7YsivFGru286SVwoTbLL8l6Jryz-6F-WgYW3UsaHP2ABcUYYoH8PCcWyirPFIpZshiL-8oAeCLVE6v7OwzIrNhWdxmEbVbVlqXvbcUdOFbVkiKjfxSgypzYoiUgLObMugH7mJPzCUwSoK5UJcEawOQEp8PUIngnGL4a2t31VB8xabV_ZmB6LigNSGoBWjIwWAczukpB91QJoYikNxo3rfR7p-CyAlvmpzEOCyoDfDguFC7Z5jat5i82qEBlkWIlXf2eA6KkQCNr3rCP2W98Ton5tcDLtkYSydtwI4NXkpvWpyEKReSkrmGlFLRNC8xeSziQiIyvq0lE6qsKI-fQBOBz3qR4WWxFCsS4L1Wio6EQGQEl-1OQjQi4fADnukWZun5i02n8-4wVR4Wmd603M6ngM4M2ooSBgdDMUz76wfIg4dWwCkxNc3aImgZkClOjPQ8Bcv_SBYfRPv4s1_vr_ILLVMW8slQse0aPfp-8tuEIJg2b_G0c2mC8vMRRU-Wt7osKIKn4Ar7vqOI1i8CQ1CFFOYHdY6VT0RTc3LidwzyXOX6EFUer1wgy4rkqgEnKkFQT8q0iWG_OzcGcZMK6iz8wSbrGul6OrZeepelOCUtJp39AkQgJsffvWiNxiRkOhes9BUr6uk5i1Pf-6iN3jye1uqdw1TlPUBm1baodpyVoH--XOPVkXdeeq5JxghufrcU3eUiWNQuuWxVmRPzVsMPb3jnUieFR6j7diayt8BOFNch2504XHPUF4kVVp5b1ZcJD0AKfH1nDkRVO_H804ExdXLX5VJBFvWh-dbm2VmZKzctyY0tS0WmonXAaDtzFpQ0OSHfa4dQiSjjkIAmyb60Gx5SqJ_cRdcslZ2bU_fBU_AmUS_kF71ExBgMivr7PDAagEwNW8xdnGPtWApNrOcC9utuP0O4MxuEspRm9nEUNz8iKHXrqENDiAlvmpwEOAx9U1vfVd9aS81b_Lu2Zf2ElF-uNsMK7GVPXW4m2BT_4ZuxOFu6p9J7owQfeepS8qAEZJrSw664_mYaFm0tbIBmrdY-llaUfBkw42NlWzYaBDDBWy6wkK1ZUOjf3Fy4mLXCE4fJgM449eF9KpfgwAHHp4Pm9nq7hXNW6w9l0mBJ3cub5gxPfXKHGATa4-qLVsb_TPJLjIvWkY9Z8AIyTW3RvexU3BO7u9JzBv60LzF0JNMCiTFwbUyxraaDtgAzhyKQTciYIMhT5etb5zg1MUUwGZMnYuumRrda2brpbdBKfviJAoEW5KouVrlMjs2aJ51RrLa2o7mZU8ZNa4lUqDJHhaPVjZBUIkUYNOdJTRbnpHoX-T7vTDKrblMk4AzW-pCer2QlAhSr9h0nXZtrY6A5i3GniZSYMls7aNsuyipG2qATWw9KrZsa_QvPoNgTGTK0JVSAKe2LqVXbQ0CpAMyuiEc1w6-0LzJsWdzqESUX5fSijG9f4N_8bpUgk0zGei2bG70L0q0vuHaRvqAHsCZPUIhvX4YkAgQO0XTd7Kvpaxo3mLuuUQKPOWlfedZ7PWKS_sH4MyiA_WoRScxFB7uteuDpwtVAFLi6x6eCHDbSDrNW1m7fYPmLSafy6bAU3yAoIutCj35AYIDbOLgo2rUBwgO_fNsyjrVBUVJBoyQXM2mUnfcGfE8GNPWDI3mLYaeZFMgyccq2rbtNZk5JthkrKNey1ZG_8KnWdS9Vyt8OgFnLtoU0us-nQhqZmuG_YNjrH1xNgWCLdnUuk8igRkpAWeOcV2rXqJ52UtGbauZVKIpLjo0Q7c1L0UDOJPPQDvqdlBiKLaTXqgmSvqlKQAp8fXtZCIY83XPtXGuuss5NG-x-DSdAkvx7r30LhhOn0QCOLfNScoRBgdDcR1rWIFUJ8nrWAfYzDYnF12_jnXoPia8sTe6l9V9wqF5k3fPHoElosLczHTOBXpXCeBcvp70o8ydGIrpNfwqGEmXAQGkxNfvESWC1KvtRSe4q-3N0LzF5nM5FXjynXTfSuP2RxKLO-kEm7jYqBpx8JT6l19gaYM8vF1CfYHlAJxau5Rev1qRCDAtDI8uclaLJql5i7Vni1OJJ7e27MSgckdZO8GmExqqEdZO_fNPtPnOdJpTB4yAEZJroQTdsZ_zQghXvaqF5i2GnqRTICkq20q4RtGV7QNsugmGXlRl-9C_SKc415LxFZvgBJzZBBfS6-lUIqhmocozGdnLT_hAsCWdWvkxPFBjFlvlhAq1-YhmIuuGurV8CjTl1QPVN27FN-YAnAlB0I56-ycx5NFg2H20glPFGsCmsbcQXa1ipu646GpbrYflp3ZNODVvMfY0lQJLvsfpuIuGU7kMYNN3J6EYscdJ_fPzF8mkZOQ3cQAjJNfMjO744lLHDAux5tNo3uTTc1kUiPIbHcZE2THyKxgJNhnvqNuypdE_PzKXDXfOUssbYITk6vuxqTs2-qLVrVa1y6lo3mLpudwJPOVbKo3omV3xleEEnHmRDOpRn5hJDHn40J1qDKeqBoBNKySF6Gr4SN1xr9LZqJSuXktNzVusPZc7gSdf1TshhbOUWwM2Ge6oGrGqp_755zqGnWgXIhVAACMk1wyN7mPC1XgbqkUGNG8x9PRgL5EUNzFC59vW0Fk5gDM7XuhG3cRIDPlDll5L31Cnt4DNpKm56Jqp0b3-zbpeMOv-Px-yPBCsvvV7-e7qkviE5YHxWTncWqf9mnL4HrjqE41J8xWfbgFtvvaw1grLyduECUZ_2abUZ5JfThirM0Gr1ob9i9YvTIcTAfW1w1zdddVFMOe7taCksmTEASw3I6H93Po24Ss_xOBa6Va8dALgitu5pTbP4v-UMT9LDjE4o6gMA7CthnmeYk0Ib-5v7nevdp_i4yd7F3bHu99u7o-Gjk8_x0_xZnc8_DPYx7_f7G7ufx9w9uvTw_Wv9353_PT4Nb7aPT58_fDz7ri3H78MP339HOxTPLuzHx7tJ0A-2_u_PTzkP-6Of9v9sjvmovsz061oJGsYU1K-2v06_JYNvzVMsLbrWt617PdXu3_u-zd_VpyrYfk2zMhWGMle7WK4Gwzy-vD_r-z_G5ZXuw-P3weS9BtCU3w8ffh6_7Sn_v3_ABVt8NQ)

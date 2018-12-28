#!usr/bin/python
# coding: utf-8

cipher = "MSW{byly_Cm_sIol_lYqUlx_yhdIs_Cn_Wuymul_il_wuff_bcg_pCwnIl_cm_u_Yrwyffyhn_guh_cz_sio_quhn_ni_ayn_bcm_chzilguncihm_sio_wuh_dich_om}"
# cipher = list(cipher)
# print(cipher)
# _len = len(cipher)
# result = []
# for i in range(_len):
#     if cipher[i] != '{' and cipher[i] != '}':
#         result.append(
#             chr(
#                 ord(cipher[i]) + 25
#             )
#         )
#     else:
#         result.append(cipher[i])
# print(''.join(result))

a = "MSW{b"
b = "flag{"
for i in range(4):
    print("%d: %s: %d -> %s: %d" % (i, a[i], ord(a[i]), b[i], ord(b[i])))





def transpose(df):
    # 转置DataFrame
    df_transposed = df.T

    # 将第一行设置为列标题
    df_transposed.columns = df_transposed.iloc[0]

    # 删除原来的第一行
    df_transposed = df_transposed.drop(df_transposed.index[0])

    # # 删除含有NaN值的列
    # df_transposed = df_transposed.dropna(axis=1, how='any')

    return df_transposed

def shaku_list():
    list1 = ['barcode',
             'wide_Bz',

             'wide_temperature_sensor',
             'wide_aps_E',
             'wide_aps_W',
             'wide_oc_xShift',
             'wide_oc_yShift',

             'wide_aps_DELTA_poly_c0_cubic_lowTemp',
             'wide_aps_DELTA_poly_c1_cubic_lowTemp',
             'wide_aps_DELTA_poly_c2_cubic_lowTemp',
             'wide_aps_DELTA_poly_c3_cubic_lowTemp',
             'wide_aps_DELTA_vh_a0_cubic',
             'wide_aps_DELTA_vh_a1_cubic',
             'wide_aps_DELTA_vh_a2_cubic',
             'wide_aps_DELTA_vh_a3_cubic',
             'wide_aps_DELTA_poly_c0_lin',
             'wide_aps_DELTA_poly_c1_lin',
             'wide_aps_DELTA_coil_linear_lowTemp_temp',
             'wide_aps_DELTA_sensor_linear_lowTemp_temp',
             'wide_aps_DELTA_vh_beta',
             'wide_aps_DELTA_vh_rho',

             'wide_aps_vcmpoly_maum_c0',
             'wide_aps_vcmpoly_maum_c1',
             'wide_aps_vcmpoly_maum_c2',
             'wide_aps_vcmpoly_maum_c3',
             'wide_aps_af_force_sensitivity_mAum',
             'wide_aps_vcmpoly_umma_c0',
             'wide_aps_vcmpoly_umma_c1',
             'wide_aps_vcmpoly_umma_c2',
             'wide_aps_vcmpoly_umma_c3',
             'wide_aps_af_force_sensitivity_ummA',

             'wide_aps_polarity',
             'wide_enableEMCorrection'
             ]
    return list1
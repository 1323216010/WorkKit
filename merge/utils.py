import pandas as pd


def summary_cal():
    #list1 = ["barcode","time","aps_DELTA_poly_c0_cub_lowTemp","aps_DELTA_poly_c1_cub_lowTemp","aps_DELTA_poly_c2_cub_lowTemp","aps_DELTA_poly_c3_cub_lowTemp","aps_DELTA_poly_c0_lin","aps_DELTA_poly_c1_lin","aps_DELTA_poly_zInflection1","aps_DELTA_poly_zInflection2","aps_DELTA_poly_gainRatio","aps_DELTA_poly_linGainMin","aps_DELTA_poly_linGainMax","aps_DELTA_linear_lowTemp_temp","aps_DELTA_coil_linear_lowTemp_temp","aps_DELTA_sensor_linear_lowTemp_temp","aps_DELTA_driver_linear_lowTemp_temp","aps_DELTA_cub_linear_max_error","aps_DELTA_cub_linear_rms_error","aps_DELTA_cub_fulllinear_max_error","aps_DELTA_cub_fulllinear_rms_error","aps_DELTA_lin_linear_max_error","aps_DELTA_lin_linear_rms_error","aps_DELTA_lin_fulllinear_max_error","aps_DELTA_lin_fulllinear_rms_error","aps_DELTA_ref_upstrokeTempDelta_degC","aps_DELTA_ref_tempDelta_degC","aps_DELTA_max_hysteresis_um","aps_DELTA_vh_a0_cub","aps_DELTA_vh_a1_cub","aps_DELTA_vh_a2_cub","aps_DELTA_vh_a3_cub","aps_DELTA_vh_beta","aps_DELTA_vh_rho","aps_DELTA_cubtemp_max_error","aps_DELTA_cubtemp_rms_error","aps_DELTA_cubtemp_uncorrected_max_error","aps_DELTA_cubtemp_uncorrected_rms_error","aps_DELTA_cubtemp_fulllinear_max_error","aps_DELTA_cubtemp_fulllinear_rms_error","aps_DELTA_cubtempfit_max_error_LSB","aps_DELTA_cubtempfit_rms_error_LSB","aps_DELTA_lintemp_max_error","aps_DELTA_lintemp_rms_error","aps_DELTA_VCM_A_DAC","aps_DELTA_A_zPos","aps_DELTA_A_ADC","aps_DELTA_A_temp","aps_DELTA_coil_A_temp","aps_DELTA_driver_A_temp","aps_DELTA_sensor_A_temp","aps_DELTA_VCM_B_DAC","aps_DELTA_B_zPos","aps_DELTA_B_ADC","aps_DELTA_B_temp","aps_DELTA_coil_B_temp","aps_DELTA_driver_B_temp","aps_DELTA_sensor_B_temp","aps_DELTA_VCM_C_DAC","aps_DELTA_C_zPos","aps_DELTA_C_ADC","aps_DELTA_C_temp","aps_DELTA_coil_C_temp","aps_DELTA_driver_C_temp","aps_DELTA_sensor_C_temp","aps_DELTA_VCM_D_DAC","aps_DELTA_D_zPos","aps_DELTA_D_ADC","aps_DELTA_D_temp","aps_DELTA_coil_D_temp","aps_DELTA_driver_D_temp","aps_DELTA_sensor_D_temp","aps_DELTA_topFullLinearRegion_DAC","aps_DELTA_bottomFullLinearRegion_DAC","aps_DELTA_topFullLinearRegion_ADC","aps_DELTA_bottomFullLinearRegion_ADC","aps_DELTA_bottomFullLinearRegion_zPos","aps_DELTA_topFullLinearRegion_zPos","aps_DELTA_bottomLinearRegion_E_ADC","aps_DELTA_topLinearRegion_E_ADC","aps_DELTA_neutral_E_ADC","aps_DELTA_bottomLinearRegion_W_ADC","aps_DELTA_topLinearRegion_W_ADC","aps_DELTA_neutral_W_ADC","aps_DELTA_bottomLinearRegion_zPos","aps_DELTA_topLinearRegion_zPos","aps_DELTA_bottomLinearRegion_DELTA_ADC","aps_DELTA_topLinearRegion_DELTA_ADC","aps_DELTA_topLinearRegion_temp","aps_DELTA_bottomLinearRegion_temp","aps_DELTA_coil_topLinearRegion_temp","aps_DELTA_coil_bottomLinearRegion_temp","aps_DELTA_sensor_topLinearRegion_temp","aps_DELTA_sensor_bottomLinearRegion_temp","aps_DELTA_topLinearRegion_DAC","aps_DELTA_bottomLinearRegion_DAC","aps_DELTA_bottomEndStop_E_z_ADC","aps_DELTA_topEndStop_E_z_ADC","aps_DELTA_bottomEndStop_W_z_ADC","aps_DELTA_topEndStop_W_z_ADC","aps_DELTA_bottomEndStop_z_zPos","aps_DELTA_topEndStop_z_zPos","aps_DELTA_bottomEndStop_DELTA_z_ADC","aps_DELTA_topEndStop_DELTA_z_ADC","aps_DELTA_topEndStop_z_temp","aps_DELTA_bottomEndStop_z_temp","aps_DELTA_coil_topEndStop_z_temp","aps_DELTA_coil_bottomEndStop_z_temp","aps_DELTA_sensor_topEndStop_z_temp","aps_DELTA_sensor_bottomEndStop_z_temp","aps_DELTA_topEndStop_z_DAC","aps_DELTA_bottomEndStop_z_DAC","aps_DELTA_bottomEndStop_E_aps_ADC","aps_DELTA_topEndStop_E_aps_ADC","aps_DELTA_bottomEndStop_W_aps_ADC","aps_DELTA_topEndStop_W_aps_ADC","aps_DELTA_bottomEndStop_aps_zPos","aps_DELTA_topEndStop_aps_zPos","aps_DELTA_bottomEndStop_DELTA_aps_ADC","aps_DELTA_topEndStop_DELTA_aps_ADC","aps_DELTA_topEndStop_aps_temp","aps_DELTA_bottomEndStop_aps_temp","aps_DELTA_coil_topEndStop_aps_temp","aps_DELTA_coil_bottomEndStop_aps_temp","aps_DELTA_sensor_topEndStop_aps_temp","aps_DELTA_sensor_bottomEndStop_aps_temp","aps_DELTA_topEndStop_aps_DAC","aps_DELTA_bottomEndStop_aps_DAC","aps_DELTA_bottomEndStop_apsvsz_zPos","aps_DELTA_topEndStop_apsvsz_zPos","aps_topEndStop_flatness_margin","aps_DELTA_polarity","aps_DELTA_sensor_deltaTemp","aps_headroomE_per","aps_headroomW_per","aps_DELTA_linear_percentage_over_linear_range","aps_DELTA_versionERS","bottomEndstop_Sphere_H1","bottomEndstop_Sphere_H2","bottomLinearRegion_Sphere_H1","bottomLinearRegion_Sphere_H2","A_Sphere_H1","A_Sphere_H2","B_Sphere_H1","B_Sphere_H2","C_Sphere_H1","C_Sphere_H2","D_Sphere_H1","D_Sphere_H2","topLinearRegion_H1","topLinearRegion_H2","topEndStop_Sphere_H1","topEndStop_Sphere_H2","aps_topendstop_cal_h1_ois_position","aps_topendstop_cal_h2_ois_position","aps_bottomendstop_cal_h1_ois_position","aps_bottomendstop_cal_h2_ois_position","aps_sweep_upstroke_diff1","aps_sweep_upstroke_diff2","aps_sweep_upstroke_diff3","aps_valid_sweep1","aps_valid_sweep2","aps_valid_sweep3","aps_valid_sweep_linear","aps_headroomE_per_sweep1","aps_headroomE_per_sweep2","aps_headroomE_per_sweep3","aps_headroomW_per_sweep1","aps_headroomW_per_sweep2","aps_headroomW_per_sweep3","aps_sweep_peak_ADC_diff","aps_valid_sweep_gap","valid_sweep_merged"]
    list1 = ["barcode","time","aps_DELTA_poly_c0_cub_lowTemp","aps_DELTA_poly_c1_cub_lowTemp","aps_DELTA_poly_c2_cub_lowTemp","aps_DELTA_poly_c3_cub_lowTemp","aps_DELTA_poly_c0_lin","aps_DELTA_poly_c1_lin","aps_single_SWIDE_poly_zInflection1","aps_single_SWIDE_poly_zInflection2","aps_DELTA_poly_gainRatio","aps_single_SWIDE_poly_linGainMin","aps_single_SWIDE_poly_linGainMax","aps_single_SWIDE_NTC_linear_lowTemp_temp","aps_DELTA_coil_linear_lowTemp_temp","aps_DELTA_sensor_linear_lowTemp_temp","aps_DELTA_driver_linear_lowTemp_temp","aps_single_SWIDE_cubic_linear_max_error","aps_single_SWIDE_cubic_linear_rms_error","aps_DELTA_cub_fulllinear_max_error","aps_DELTA_cub_fulllinear_rms_error","aps_DELTA_lin_linear_max_error","aps_DELTA_lin_linear_rms_error","aps_DELTA_lin_fulllinear_max_error","aps_DELTA_lin_fulllinear_rms_error","aps_DELTA_ref_upstrokeTempDelta_degC","aps_DELTA_ref_tempDelta_degC","aps_DELTA_max_hysteresis_um","aps_DELTA_vh_a0_cub","aps_DELTA_vh_a1_cub","aps_DELTA_vh_a2_cub","aps_DELTA_vh_a3_cub","aps_DELTA_vh_beta","aps_single_SWIDE_vh_rho","aps_single_SWIDE_cubictemp_max_error","aps_single_SWIDE_cubictemp_rms_error","aps_DELTA_cubtemp_uncorrected_max_error","aps_DELTA_cubtemp_uncorrected_rms_error","aps_DELTA_cubtemp_fulllinear_max_error","aps_DELTA_cubtemp_fulllinear_rms_error","aps_DELTA_cubtempfit_max_error_LSB","aps_DELTA_cubtempfit_rms_error_LSB","aps_DELTA_lintemp_max_error","aps_DELTA_lintemp_rms_error","aps_DELTA_VCM_A_DAC","aps_DELTA_A_zPos","aps_DELTA_A_ADC","aps_DELTA_A_temp","aps_DELTA_coil_A_temp","aps_DELTA_driver_A_temp","aps_DELTA_sensor_A_temp","aps_DELTA_VCM_B_DAC","aps_DELTA_B_zPos","aps_DELTA_B_ADC","aps_DELTA_B_temp","aps_DELTA_coil_B_temp","aps_DELTA_driver_B_temp","aps_DELTA_sensor_B_temp","aps_DELTA_VCM_C_DAC","aps_DELTA_C_zPos","aps_DELTA_C_ADC","aps_DELTA_C_temp","aps_DELTA_coil_C_temp","aps_DELTA_driver_C_temp","aps_DELTA_sensor_C_temp","aps_DELTA_VCM_D_DAC","aps_DELTA_D_zPos","aps_DELTA_D_ADC","aps_DELTA_D_temp","aps_DELTA_coil_D_temp","aps_DELTA_driver_D_temp","aps_DELTA_sensor_D_temp","aps_single_SWIDE_topFullLinearRegion_DAC","aps_single_SWIDE_bottomFullLinearRegion_DAC","aps_single_SWIDE_topFullLinearRegion_ADC","aps_single_SWIDE_bottomFullLinearRegion_ADC","aps_single_SWIDE_bottomFullLinearRegion_zPos","aps_single_SWIDE_topFullLinearRegion_zPos","aps_DELTA_bottomLinearRegion_E_ADC","aps_DELTA_topLinearRegion_E_ADC","aps_DELTA_neutral_E_ADC","aps_DELTA_bottomLinearRegion_W_ADC","aps_DELTA_topLinearRegion_W_ADC","aps_DELTA_neutral_W_ADC","aps_DELTA_bottomLinearRegion_zPos","aps_DELTA_topLinearRegion_zPos","aps_DELTA_bottomLinearRegion_DELTA_ADC","aps_DELTA_topLinearRegion_DELTA_ADC","aps_DELTA_topLinearRegion_temp","aps_DELTA_bottomLinearRegion_temp","aps_DELTA_coil_topLinearRegion_temp","aps_DELTA_coil_bottomLinearRegion_temp","aps_DELTA_sensor_topLinearRegion_temp","aps_DELTA_sensor_bottomLinearRegion_temp","aps_DELTA_topLinearRegion_DAC","aps_DELTA_bottomLinearRegion_DAC","aps_DELTA_bottomEndStop_E_z_ADC","aps_DELTA_topEndStop_E_z_ADC","aps_DELTA_bottomEndStop_W_z_ADC","aps_DELTA_topEndStop_W_z_ADC","aps_DELTA_bottomEndStop_z_zPos","aps_DELTA_topEndStop_z_zPos","aps_DELTA_bottomEndStop_DELTA_z_ADC","aps_DELTA_topEndStop_DELTA_z_ADC","aps_DELTA_topEndStop_z_temp","aps_DELTA_bottomEndStop_z_temp","aps_DELTA_coil_topEndStop_z_temp","aps_DELTA_coil_bottomEndStop_z_temp","aps_DELTA_sensor_topEndStop_z_temp","aps_DELTA_sensor_bottomEndStop_z_temp","aps_DELTA_topEndStop_z_DAC","aps_DELTA_bottomEndStop_z_DAC","aps_DELTA_bottomEndStop_E_aps_ADC","aps_DELTA_topEndStop_E_aps_ADC","aps_DELTA_bottomEndStop_W_aps_ADC","aps_DELTA_topEndStop_W_aps_ADC","aps_DELTA_bottomEndStop_aps_zPos","aps_DELTA_topEndStop_aps_zPos","aps_DELTA_bottomEndStop_DELTA_aps_ADC","aps_DELTA_topEndStop_DELTA_aps_ADC","aps_DELTA_topEndStop_aps_temp","aps_DELTA_bottomEndStop_aps_temp","aps_DELTA_coil_topEndStop_aps_temp","aps_DELTA_coil_bottomEndStop_aps_temp","aps_DELTA_sensor_topEndStop_aps_temp","aps_DELTA_sensor_bottomEndStop_aps_temp","aps_DELTA_topEndStop_aps_DAC","aps_DELTA_bottomEndStop_aps_DAC","aps_DELTA_bottomEndStop_apsvsz_zPos","aps_DELTA_topEndStop_apsvsz_zPos","aps_topEndStop_flatness_margin","aps_DELTA_polarity","aps_single_SWIDE_NTC_deltaTemp","aps_single_SWIDE_headroom_per_e","aps_single_SWIDE_headroom_per_w","aps_DELTA_linear_percentage_over_linear_range","aps_DELTA_versionERS","bottomEndstop_Sphere_H1","bottomEndstop_Sphere_H2","bottomLinearRegion_Sphere_H1","bottomLinearRegion_Sphere_H2","A_Sphere_H1","A_Sphere_H2","B_Sphere_H1","B_Sphere_H2","C_Sphere_H1","C_Sphere_H2","D_Sphere_H1","D_Sphere_H2","topLinearRegion_H1","topLinearRegion_H2","topEndStop_Sphere_H1","topEndStop_Sphere_H2","aps_topendstop_cal_h1_ois_position","aps_topendstop_cal_h2_ois_position","aps_bottomendstop_cal_h1_ois_position","aps_bottomendstop_cal_h2_ois_position","aps_single_SWIDE_sweep_upstroke_diff_1","aps_single_SWIDE_sweep_upstroke_diff_2","aps_single_SWIDE_sweep_upstroke_diff_3","aps_valid_sweep1","aps_valid_sweep2","aps_valid_sweep3","aps_valid_sweep_linear","aps_headroomE_per_sweep1","aps_headroomE_per_sweep2","aps_headroomE_per_sweep3","aps_headroomW_per_sweep1","aps_headroomW_per_sweep2","aps_headroomW_per_sweep3","aps_single_SWIDE_sweep_peak_ADC_diff","aps_valid_sweep_gap","valid_sweep_merged","aps_DELTA_A_E_ADC","aps_DELTA_A_W_ADC","aps_DELTA_B_E_ADC","aps_DELTA_B_W_ADC","aps_DELTA_C_E_ADC","aps_DELTA_C_W_ADC","aps_DELTA_D_E_ADC","aps_DELTA_D_W_ADC","aps_single_zeroumRefPos","aps_single_SWIDE_iBias_e","aps_single_SWIDE_iBias_w"]


    return list1

def read_csv1(path, columns_to_read):
    # 首先读取列名，以确认文件中包含哪些列
    col_names = pd.read_csv(path, nrows=1).columns

    # 筛选出我们需要读取的列名
    valid_columns = [col for col in columns_to_read if col in col_names]

    # 读取特定的列
    df = pd.read_csv(path, usecols=valid_columns, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def read_csv(path):
    col_names = pd.read_csv(path, nrows=1).columns
    df = pd.read_csv(path, usecols=col_names, low_memory=False, encoding="UTF-8", delimiter=',')
    return df


def remove_columns(merged_df):
    columns_to_remove = []  # 存储需要删除的列名
    for col in merged_df.columns:
        if col.endswith('_x'):
            original_col_name = col[:-2]  # 去除_x后缀获取原始列名
            col_y = original_col_name + '_y'

            # 如果存在对应的_y列，可以选择删除_y列
            if col_y in merged_df.columns:
                columns_to_remove.append(col_y)

            # 重命名_x列为原始列名
            merged_df.rename(columns={col: original_col_name}, inplace=True)

    # 删除所有标记为删除的列
    merged_df.drop(columns=columns_to_remove, inplace=True)

    return merged_df
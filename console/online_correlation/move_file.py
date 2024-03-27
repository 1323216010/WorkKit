import shutil
import os
import fnmatch


APS_ResFreq = ["Infu[","Neutral[","SuperMcup["]#可能需要改变,注意顺序
ViscoEladstic = ["Infu[","ViscoElastic_FixedFQ_data_CmpInf",
                 "SuperMcup[","ViscoElastic_FixedFQ_data_CmpMac"]
FocusMargins=["FocusMarginCheck_15_","FocusMarginCheck_25_","FocusMarginCheck_40_"]
testerpath = r'C:\Users\pengcheng.yan\Desktop\APS Online\Log1' #summaylog 文件所在路径
debugpath = r"C:\Users\pengcheng.yan\Desktop\APS Online\Log\Debug_A\20240320214952"   #数据文件所在的路径，根据文件所在的路径调整
pattern = '*.csv'
path = r"./input"  #代码路径  根据实际情况调整
def judge(file):   #判断文件名中是否有bin 如果有跳转到下一个文件
    if "bin" in file:
        return 0
def movefile(file_path,file):  #移动文件到目标文件夹
    if "ADDITIONNAL_CHECK" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\"+file
        newname = path + r"\Addtional_Check.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname,newname)
    if "ApsCalibrationSweepFromMcu" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\APScal.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "VcmMeasure" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\VcmMeasure.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if APS_ResFreq[0] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\Infu.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if APS_ResFreq[1] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\Neutral.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if APS_ResFreq[2] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\Supermcup.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if ViscoEladstic[0] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\Infu.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if ViscoEladstic[1] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\ViscoElastic_FixedFQ_data_CmpInf.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if ViscoEladstic[2] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\SuperMcup.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if ViscoEladstic[3] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\ViscoElastic_FixedFQ_data_CmpMac.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "OISAFDST" in file:
        shutil.copy2(file_path,path)
        oldname = path + "\\" + file
        newname = path +r"\AFDST.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "Bz_drive_pattern_with_APS_Reading" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\Bz_drive_pattern_with_APS_Reading.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "APS_nosie_off_aps_single_SWIDE_delta_poly_c1_cubic" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\APS_nosie_aps_single_SWIDE_delta_poly_c1_cubic.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if FocusMargins[0] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\FocusMarginCheck_15_.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if FocusMargins[1] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\FocusMarginCheck_25_.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if FocusMargins[2] in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path +r"\FocusMarginCheck_40_.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "getEstimatedInfuDac_input" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\getEstimatedInfuDac_input.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "OptiCalOffset" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\OptiCalOffset.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "APSNoiseStreamingOn_DAC0" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\APSNoiseStreamingOn_DAC0.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "APS_nosie_on_aps_single_SWIDE_delta_poly_c1_cubic" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\APS_nosie_aps_single_SWIDE_delta_poly_c1_cubic.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "APS_nosie_aps_single_SWIDE_delta_poly_c1_cubic" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\APS_nosie_aps_single_SWIDE_delta_poly_c1_cubic.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "APSNoiseStreamingOff_DAC0" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\APSNoiseStreamingOff_DAC0.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "VCM_SAG" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\VCM_Sag.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "ApsCalibrationSweepFromMcu" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\ApsCalibrationSweepFromMcu.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "TILT_PDX" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\TILT_PDX.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname, newname)
    if "zEstimationProfile" in file:
        shutil.copy2(file_path, path)
        oldname = path + "\\" + file
        newname = path + r"\zEstimationProfile.csv"
        if os.path.exists(newname):
            os.remove(newname)
        os.rename(oldname,newname)

def cutfilename():
    files = os.listdir(debugpath)  # 获取文件夹下的所有文件名
    for file in files:
        if judge(file) == 0:  #判断当文件名中含有bin字符串时，跳到下一个文件
            continue
        file_path = os.path.join(debugpath,file)
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.isfile(file_path) and fnmatch.fnmatch(file, pattern):  #判断文件是否为.csv文件
            movefile(file_path,file)
    files1 = os.listdir(testerpath)
    for file in files1:
        if 'Tester_A' in file and 'LimitLog' not in file:
            file_path = os.path.join(testerpath,file)
            shutil.copy2(file_path, path)
            oldname = path + "\\" + file
            newname = path + r"\tester.csv"
            if os.path.exists(newname):
                os.remove(newname)
            os.rename(oldname, newname)


if __name__ == '__main__':
    cutfilename()


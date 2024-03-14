import os
import numpy as np
import scipy.io as io
import copy
import struct
import sys
import pandas as pd


# see D:\SVN1\DayList2022_2\day0513_OA_Ru_fieldneighbor_max\testBench_OA_D50\relative_uniformity.m

def SaveRomBinFile(lst, strPathName):
    f = open(strPathName, "wb")
    for x in lst:
        s1 = struct.pack('h', x)
        f.write(s1)
    f.close()


def LoadIntBinFile(rPath, h, w):
    # read bin file
    f = open(rPath, 'rb')
    tt = struct.unpack('<' + str(w * h) + 'i', f.read(w * h * 4))
    f.close()
    retA = np.array(tt, order='C')
    retA.shape = (h, w)
    return retA


def OC_algo(IDy):
    h, w = IDy.shape
    hCentre = h / 2 + 0.5;
    wCentre = w / 2 + 0.5;
    roiSize = 100;
    roiSizeHalf = roiSize / 2;
    # centre top right bottom left
    roiCentreX = np.array(
        [wCentre, wCentre, wCentre + hCentre - (roiSizeHalf + .5), wCentre, wCentre - hCentre + roiSizeHalf + .5])
    roiCentreY = np.array([hCentre, roiSizeHalf + .5, hCentre, h - (roiSizeHalf - .5), hCentre])
    # threshold_binary
    x1 = (roiCentreX - (roiSizeHalf - 0.5)).astype(int)
    x2 = (roiCentreX + (roiSizeHalf - 0.5)).astype(int)
    y1 = (roiCentreY - (roiSizeHalf - 0.5)).astype(int)
    y2 = (roiCentreY + (roiSizeHalf - 0.5)).astype(int)
    thresholdData = np.zeros((5,))
    for i in range(5):
        thresholdData[i] = (IDy[y1[i] - 1:y2[i], x1[i] - 1: x2[i]]).mean()
    # (0.5* cen + 0.125 * corners)
    oc_threshold = 0.5 * thresholdData[0] + 0.125 * np.sum(thresholdData[1:])
    IDthreshold_binary = (IDy >= oc_threshold).astype(float)
    colSum = (np.arange(w) + 1) * np.sum(IDthreshold_binary, axis=0)  # 行加  列数， x
    rowSum = (np.arange(h) + 1) * np.sum(IDthreshold_binary, axis=1)  # 列加  行数， y
    oc_x = colSum.sum() / IDthreshold_binary.sum()
    oc_y = rowSum.sum() / IDthreshold_binary.sum()
    oc_xShift = oc_x - (w / 2 + 0.5)
    oc_yShift = (h / 2 + 0.5) - oc_y
    oc_magShift = np.sqrt(oc_xShift ** 2 + oc_yShift ** 2)
    output = {}
    output['oc_threshold'] = oc_threshold
    output['oc_x'] = oc_x;
    output['oc_xShift'] = oc_xShift;
    output['oc_y'] = oc_y;
    output['oc_yShift'] = oc_yShift;
    output['oc_magShift'] = oc_magShift;
    output['test_ver'] = 8.11;

    return output


# matlab ,based 1
def ROIinImage(x1, y1, x2, y2, w, h):
    if x1 <= 0 or y1 <= 0: return False
    if x2 > w or y2 > h: return False
    return True


def main():
    DEF_USE_argvMode = True
    print('note OA 1280X1280')
    if DEF_USE_argvMode:
        pass
        if len(sys.argv) == 2:
            rpath = sys.argv[1]
            rpath = rpath.strip('"')
            if not os.path.isfile(rpath):
                print('path not exist')
                os.sys.exit()
        else:
            print('pls input raw file path ,nvm data as an option')
    else:
        print("please input path of image raw file :")
        rpath = input() or None
        rpath = rpath.strip('"')

    # rpath= r'D:\SVN1\DayList2022_2\day0513_OA_Ru_fieldneighbor_max\image\FTU_20220207_093751_NULL_F0W146300DEKVGVE9_D50_Average_20220207_093620.raw'
    # rpath= rpath.strip('"')

    f = open(rpath, 'rb')
    w, h = 1280, 1280
    assert (os.path.getsize(rpath) == w * h * 2)
    tt = struct.unpack('<' + str(w * h) + 'h', f.read(w * h * 2))
    imgWidth, imgHeight = w, h
    f.close()
    IDraw = np.array(tt, order='C')
    IDraw.shape = (h, w)
    pass
    # preprocess
    pedestal = -16
    ID = (IDraw + pedestal).astype(float)
    OCResult = OC_algo(ID)

    ImageCircleRadius = 710
    padBorder = 0
    MaskRadius = ImageCircleRadius - padBorder
    # r_grid= sqrt( （x-cenX）**2 + （x-cenX）**2)
    # ImageMask = (r_grid < MaskRadius);  skip
    # if maskImageCircle == 1
    im_diagonal = 0.85 * ImageCircleRadius;
    xcentre, ycentre = np.round(OCResult['oc_x'] + 1e-6), np.round(OCResult['oc_y'] + 1e-6)

    roi_diagonal = 0.05 * im_diagonal;
    roi_length = np.round(np.sqrt(roi_diagonal ** 2 / 2) + 1e-6);  # 21

    # start here
    lst = []
    ROInum = 1
    # ('ROInum', 'field', 'angle', 'x', 'y', 'val')
    ROI = {}
    ROI['ROInum'] = ROInum
    ROI['field'] = 0
    ROI['angle'] = 0.0

    x1 = int(xcentre - np.round(roi_length / 2 + 1e-6));
    y1 = int(ycentre - np.round(roi_length / 2 + 1e-6));
    x2 = int(x1 + roi_length - 1);
    y2 = int(y1 + roi_length - 1);
    ROI['x'] = (x1 + x2) / 2
    ROI['y'] = (y1 + y2) / 2;
    ROI['val'] = ID[y1 - 1:y2, x1 - 1:x2].mean();
    lst.append(copy.deepcopy(ROI))

    for idxRing in range(5, 100 + 5, 5):
        ROIsInRing = np.floor(2 * np.pi * idxRing / 5);
        r = im_diagonal * idxRing / 100;
        for rot in range(0, int(ROIsInRing)):
            x1 = int(xcentre + np.round(r * np.cos(rot / ROIsInRing * 2 * np.pi) - roi_length / 2));
            y1 = int(ycentre + np.round(r * np.sin(rot / ROIsInRing * 2 * np.pi) - roi_length / 2));
            x2 = int(x1 + roi_length - 1);
            y2 = int(y1 + roi_length - 1);
            if not ROIinImage(x1, y1, x2, y2, w, h):
                print('roi not in image ', rot, x1, y1, x2, y2, w, h)
                continue

            ROInum += 1
            ROI = {}
            ROI['ROInum'] = ROInum
            ROI['field'] = idxRing
            ROI['angle'] = rot / ROIsInRing * 360;
            ROI['x'] = (x1 + x2) / 2
            ROI['y'] = (y1 + y2) / 2;
            ROI['val'] = ID[y1 - 1:y2, x1 - 1:x2].mean();
            lst.append(copy.deepcopy(ROI))

    df = pd.DataFrame(lst)

    # neighbour
    C2Lst = []
    for curRing in range(0, 105, 5):
        a1 = df[df['field'] == curRing]
        tMean = a1.mean()['val']
        c0 = [a1['val'].iloc[0] - a1['val'].iloc[-1]]
        c1 = a1['val'].iloc[1:].values - a1['val'].iloc[0:-1].values
        c1 = [x for x in c1]
        c1 = c0 + c1
        c2 = [100 * abs(x) / tMean for x in c1]
        C2Lst += c2

    df['NeighbourDif'] = C2Lst
    df.to_csv(rpath + '_EachROI.csv', index=False)
    print('saved ', rpath + '_EachROI.csv')
    print('finish')
    # end dd

    # Min /max /range .mean  for each field
    Lst = []
    for curRing in range(0, 95, 5):
        a1 = df[df['field'] == curRing]
        # Min /max /range .mean
        resDict = {}
        resDict['field'] = curRing
        resDict['Max'] = a1.max()['val']
        resDict['Min'] = a1.min()['val']
        resDict['Mean'] = a1.mean()['val']
        resDict['Range'] = 100 * (resDict['Max'] - resDict['Min']) / resDict['Mean']
        c1 = a1['val'].iloc[1:].values - a1['val'].iloc[0:-1].values
        c1 = [a1['val'].iloc[0] - a1['val'].iloc[-1]] + [x for x in c1]

        c2 = [100 * abs(x) / resDict['Mean'] for x in c1]

        resDict['Neighbours'] = str(c2)
        resDict['NeighbourMax'] = max(c2)
        resDict['Difference'] = 0
        if curRing >= 10:
            fieldMean = resDict['Mean']
            fieldMean10 = Lst[-2]['Mean']
            fieldMean5 = Lst[-1]['Mean']
            fieldPredicted = fieldMean5 + (fieldMean5 - fieldMean10)
            ringDifference = 100 * ((fieldMean - fieldPredicted) / fieldPredicted)
            resDict['Difference'] = ringDifference

        Lst.append(copy.deepcopy(resDict))

    df2 = pd.DataFrame(Lst)

    resDict = {}
    resDict['field'] = 110  # comment
    resDict['Max'] = df2.iloc[2:].max()['Difference']
    resDict['Min'] = df2.iloc[2:].min()['Difference']
    resDict['Mean'] = df2.iloc[2:].max()['Range']
    resDict['Range'] = df2.iloc[2:].max()['NeighbourMax']
    resDict['Neighbours'] = 'comment row: ru_ringdiff_max, ru_ringdiff_min,ru_fieldminmax_max, ru_fieldneighbor_max  '
    resDict['NeighbourMax'] = '8.22'
    resDict['Difference'] = 0

    df3 = pd.DataFrame([resDict])
    df4 = pd.concat([df2, df3], axis=0)

    df4.to_csv(rpath + '_EachField.csv', index=False)
    print('saved ', rpath + '_EachField.csv')
    print('finish2')


if __name__ == "__main__":
    print('Elephant_RU log v1 20220513')
    print('any question ,pls contact zhangbo@cowellchina.com')
    print('--------------------------------')
    main()




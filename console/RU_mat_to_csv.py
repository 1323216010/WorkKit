import copy
import scipy.io as io

import pandas as pd

path = r'C:\Users\pengcheng.yan\Desktop\6pcs fail+6pcs pass\mat\ROIs.mat'
tt = io.loadmat(path)
a1 = tt['ROIs']
# ('ROInum', 'field', 'angle', 'x', 'y', 'val')
print(a1[0].dtype.names)
print('records = ', len(a1))

lst = []
for i in range(len(a1)):
    mydict = {}
    mydict['ROInum'] = a1[i][0][0][0][0]
    mydict['field'] = a1[i][0][1][0][0]
    mydict['angle'] = a1[i][0][2][0][0]
    mydict['x'] = a1[i][0][3][0][0]
    mydict['y'] = a1[i][0][4][0][0]
    mydict['val'] = a1[i][0][5][0][0]
    lst.append(copy.deepcopy(mydict))

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
df.to_csv(path + '_EachROI.csv', index=False)
print('finish')

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
    c1 = [x for x in c1]
    c1.append(a1['val'].iloc[0] - a1['val'].iloc[-1])
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

df4.to_csv(path + '_EachField.csv', index=False)
print('finish2')


















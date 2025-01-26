#!/usr/bin/env python
__coding__ = "utf-8"
__author__ = "Ng WaiMing"

import kMeans
from numpy import *

if __name__ == '__main__':
    dataMat = mat(kMeans.loadDataSet('./testSet.txt'))
    print('min(dataMat[:, 0])', min(dataMat[:, 0]), '\n')
    print('min(dataMat[:, 1])', min(dataMat[:, 1]), '\n')
    print('max(dataMat[:, 0])', max(dataMat[:, 0]), '\n')
    print('max(dataMat[:, 1])', max(dataMat[:, 1]), '\n')
    print(kMeans.randCent(dataMat, 2),'\n')
    print(kMeans.distEclud(dataMat[0],dataMat[1]))
    centroids, clusterAssment = kMeans.kMeans(dataMat, 4)
    print('centroids:\n', centroids, '\n')
    print('clusterAssment:\n',clusterAssment, '\n')



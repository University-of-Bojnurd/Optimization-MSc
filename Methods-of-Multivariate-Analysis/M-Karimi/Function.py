# all functions in class
from numpy import linalg
from numpy import diag, cov, array, transpose, dot, corrcoef, mean
from statistics import stdev 
from math import sqrt


SampleArea = [[1, 2, 3, 4, 5, 6], 
              [5, 6, 4, 5, 8, 6], 
              [5, 8, 2, 6, 4, 7], 
              [6, 9, 7, 3, 4, 2],
              [5, 9, 1, 7, 5, 4], 
              [6, 3, 0, 1, 5, 6],]

Table_mu = [2, 6, 6, 8, 5, 8]              
ATable = [9, 8, 5, 3, 7, 8]
ATable1 = array([[9], [8], [5], [3], [7], [8],])



def diagArray():
    """
    >> diag()
    [A11, A22, A33, ..., Ann]
    """
    diag_Array = diag(SampleArea)
    
    return diag_Array

# print("Diag: {}".format(diagArray()))

def AAprime():
    """
    >> AAprime()
    aaprime and aprimea
    """
    aprimeA = dot(transpose(ATable), ATable)

    # Aaprime = dot(ATable1, ATable)
    

    return aprimeA

# print(AAprime())

def vectorLength():
    """
    >> vectorLength()
    sqrt(Sum(AAprime))
    """
    vecLen = sqrt(AAprime())

    return vecLen

# print(vectorLength())

def effectArray():
    """
    
    """

    effect = sum(diagArray())

    return effect

# print(effectArray())

def determin():
    """
    
    """
    deterArray = linalg.det(SampleArea)

    return deterArray

# print(determin())

def Rcorr(n, m):
    """
    
    """
    corrRnm = corrcoef(SampleArea[n-1], SampleArea[m-1])

    return corrRnm

# print(Rcorr(1, 3))

def TotalRcorr():
    """
    
    """

    TotalCorrC = corrcoef(SampleArea)

    return TotalCorrC

# print(TotalRcorr())






def yHad():
    """
    >> yHad()
    [Avg1, Avg2, ...]
    """
    level1 = range(len(SampleArea))

    yHad_Array = [mean(SampleArea[i]) for i in level1]


    return yHad_Array

# print(yHad())



def sampleCov():
    """
    >> sampleCov()
    [size = len(Table) * len(Table)]
    """
    return cov(SampleArea)

def calculateTsquar():
    """
    >> calculateTsquar()
    T-Squar
    """

    N = len(SampleArea[0])
    
    difrenceY = array(yHad()) - Table_mu

    transposDif = transpose(difrenceY)

    invSampl = linalg.inv(sampleCov())

    part1 = dot(transposDif, invSampl)

    part2 = dot(part1, difrenceY)

    TSquar = N * part2
    

    return TSquar

def student_t():
    """
    >> student_t()
    [t1, t2, ...]
    """
    level1 = len(SampleArea[0])
    St_T= [(yHad()[i] - Table_mu[i]) / (stdev(SampleArea[i]) / sqrt(level1)) for i in range(4)]

    

    return St_T







# Sample Print
# Result = "============= Result ============="

# print("{}\nY Had is: \n{} \nSample Covariance: \n{} \n\nT-Square is: \n{}".format(Result, yHad(), sampleCov(), calculateTsquar()))


# for i in range(4):
#     print("\nT-Student {} is: \n{}".format(str(i+1), student_t()[i]))

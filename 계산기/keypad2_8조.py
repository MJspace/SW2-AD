import calcFunctions_8조
numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = {
    'pi':'3.141592',
    '빛의 이동 속도 (m/s)':'3E+8',
    '소리의 이동 속도 (m/s)':'340',
    '태양과의 평균 거리 (km)':'1.5E+8',
}

functionList = {
    'factorial (!)': calcFunctions_8조.factorial,
    '-> binary': calcFunctions_8조.decToBin,
    'binary -> dec': calcFunctions_8조.binToDec,
    '-> roman': calcFunctions_8조.decToRoman,
}


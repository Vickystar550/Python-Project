def StringChallenge(strParam):
    # code goes here

    testParam = list(strParam)

    for i in range(0, int(len(strParam) / 2)):

        defect_str = []
        if strParam[i] != strParam[len(strParam) - i - 1]:
            y = testParam.index(i)
            defect_str += testParam.pop(y)

        return

    StringChallenge("abjchba")
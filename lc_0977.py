def sortedSquares(A):
    """
    :type A: List[int]
    """
    if A is None or len(A) == 0:
        return A

    firstPos = -1
    for i in range(len(A)):
        if A[i] >= 0:
            firstPos = i
            break

    neg = A[:i]
    neg = neg[::-1]
    pos = A[i:]

    posIndex = 0
    negIndex = 0

    nums = []

    while posIndex < len(pos) or negIndex < len(neg):
        if (posIndex == len(pos)):
            nums.extend([n*n for n in neg[negIndex:]])
            return nums
        elif (negIndex == len(neg)):
            nums.extend([p*p for p in pos[posIndex:]])
            return nums
        else:
            posSq = pos[posIndex] * pos[posIndex]
            negSq = neg[negIndex] * neg[negIndex]

            if posSq < negSq:
                nums.append(posSq)
                posIndex += 1
            else:
                nums.append(negSq)
                negIndex += 1

    return nums
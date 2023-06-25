def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # initialize the matrix
    lcs_matrix = [[0] * (n+1) for i in range(m+1)]

    # fill the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])

    # find the LCS
    lcs = ""
    i, j = m, n 
    while i > 0 and j>0:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return lcs

str1 = "ABCDGH"
str2 = "AEDFHR"
print(lcs(str1, str2))
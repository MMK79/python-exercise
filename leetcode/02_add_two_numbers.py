def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    i_dic = {}
    j_dic = {}
    l3 = []
    for i, i_digit in enumerate(l1):
        i_dic[i] = i_digit
    for j, j_digit in enumerate(l2):
        j_dic[j] = j_digit

    if len(l1) == len(l2):
        sum_dic = {}
        for k in i_dic.keys():
            if k not in sum_dic.keys():
                if i_dic[k] + j_dic[k] < 10:
                    sum_dic[k] = i_dic[k] + j_dic[k]
                else:
                    sum_dic[k] = (i_dic[k] + j_dic[k]) % 10
                    sum_dic[k + 1] = 1
            else:
                if i_dic[k] + j_dic[k] < 10:
                    sum_dic[k] = i_dic[k] + j_dic[k] + sum_dic[k]
                else:
                    sum_dic[k] = (i_dic[k] + j_dic[k]) % 10 + sum_dic[k]
                    sum_dic[k + 1] = 1

        print(sum_dic)


l1 = [2, 4, 3]
l2 = [5, 6, 4]

addTwoNumbers(l1, l2)

l1 = [0]
l2 = [0]
addTwoNumbers(l1, l2)

l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
addTwoNumbers(l1, l2)

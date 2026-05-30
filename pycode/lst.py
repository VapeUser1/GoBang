#这里仅提供列表处理的函数
def lst1_in_lst2(lst1, lst2):
    if len(lst1) > len(lst2):
        return False
    for i in range(len(lst2)-len(lst1)+1):
        if lst1 == lst2[i:i+len(lst1)]:
            return True
    lst2_ = lst2[::-1]
    for i in range(len(lst2)-len(lst1)+1):
        if lst1 == lst2_[i:i+len(lst1)]:
            return True
    return False

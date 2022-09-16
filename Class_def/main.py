# 快速排序
def quick_sort(lst):
    if len(lst)<2:
        return lst
    else:
        pirot = lst[0]
        small_lst = [i for i in lst[1:] if i<pirot]
        large_lst = [j for j in lst[1:] if j>pirot]
        qs = quick_sort(small_lst)
        ql = quick_sort(large_lst)
        return qs+[pirot]+ql

if __name__=='__main__':
    lst = [49,38,65,88]
    print(quick_sort(lst))
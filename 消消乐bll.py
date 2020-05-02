"""
    控制台消消乐核心代码
"""
import random
list_sample=[
    [1,1,1,2,3,2],
    [3,3,2,2,1,3],
    [2,1,3,2,1,3],
    [3,2,1,1,2,1],
    [1,1,1,2,3,2],
    [1,1,2,3,1,2]
 ]
# list_sample=[
#     [0,0,0,2,3,2],
#     [3,3,2,4,1,3],
#     [2,1,3,2,1,3],
#     [3,2,1,1,2,1],
#     [0,0,0,2,3,2],
#     [1,1,2,3,1,2]
# ]

list_replace=[]

def find_3_same_elements_inrow():
    """
        找出地图内3个连续相同的元素的位置
    :return:改变原列表, 没有返回值.
    """
    #判断横排有没有3个相同的.
    for c in range(len(list_sample)): #0,1,2,3,4,5
        for r in range(1,len(list_sample[c])-1):#每一排掐头去尾 1,2,3,4
            do_have_3_same_row(c, r)

def do_have_3_same_row(c, r):
    if list_sample[c][r] == list_sample[c][r + 1] and list_sample[c][r] == list_sample[c][r - 1]:
        # 横排比, 不用看c,因为都是c和c 比, r从0开始,之所以r-1下标不越界是因为Python有负标, 但是r+1就要关注越界问题.所以竖排比,把r和c指向的对象拿过来后,发现r少了末尾最后一排不能参与比较, 所以就要在if分支里把末尾补充进去.
        # 遇到一个bug:  for r in range(c, len(list_sample[c])-1)横排竖排找不全, 竖排完全没有, 经过shift+f9发现, 第三次循环的内层循环直接从3开始也就是r=3开始,所以取不到一大片.
        list_replace.append((c, r - 1))
        list_replace.append((c, r))
        list_replace.append((c, r + 1))

def find_3_same_elements_incolum():
    # 判断竖排有没有3个相同的.
    for c in range(len(list_sample)): #0,1,2,3,4,5
        for r in range(1,len(list_sample[c])-1): # 1,2,3,4
            do_have_3_same_colum(c, r)

def do_have_3_same_colum(c, r):
    if list_sample[r][c] == list_sample[r + 1][c] and list_sample[r][c] == list_sample[r - 1][c]:
        list_replace.append((r - 1, c))
        list_replace.append((r, c))
        list_replace.append((r + 1, c))

def replace_of_0():
    """
        替换为0
    """
    for i in list_replace:
        list_sample[i[0]][i[1]]=0
    list_replace.clear()

def falling_down():
    """
        下落
    """
    #按照列遍历二维数组，定义一个指针 t，指向上次不为 0 的方块位置，一旦遇到方块不为 0 的格子就将其与t所指的方块就行交换，一次类推
    # for c in range(1, len(list_sample)):
    #     for i in list_replace:
    #         if list_sample[i[0]-c][i[1]]!=0:
    #             list_sample[i[0] - c][i[1]],list_sample[i[0]][i[1]]=list_sample[i[0]][i[1]],list_sample[i[0] - c][i[1]]
    #     list_replace.clear()
    #     find_3_same_elements()
        # if list_sample[i[0] - 1][i[1]] != 0:
        #     list_sample[i[0] - 1][i[1]], list_sample[i[0]][i[1]] = list_sample[i[0]][i[1]], list_sample[i[0] - 1][i[1]]
    for i in range(len(list_sample)):
        for c in range(len(list_sample)):
            for r in range(len(list_sample[c])):
                if list_sample[c][r]==0 and c-1!=-1:
                    list_sample[c][r],list_sample[c-1][r]=list_sample[c-1][r],list_sample[c][r]

def generate_new():
    for c in range(len(list_sample)):
        for r in range(len(list_sample[c])):
            if list_sample[c][r] == 0:
                list_sample[c][r]=random.randint(1,3)

def is_list_empty():
    if len(list_replace)!=0:
        return False
    else:
        return True

def finish_eliminate():
    while True:
        find_3_same_elements_inrow()
        find_3_same_elements_incolum()
        if is_list_empty():
            break
        replace_of_0()
        falling_down()
        generate_new()

def exchange():
    pass

finish_eliminate()
print(list_sample)





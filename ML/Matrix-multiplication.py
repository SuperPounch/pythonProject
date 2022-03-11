# hw model - synthesizable operations only
def mat_mul(x, yt):
    res = []
    pp = []


    # stage 0 - partial products generation
    #logic 【】 pp_stage0_next[]
    #logic [] pp_stage0
    for row_x in x:
        pp_row = []
        #pp_stage0_next_row=[]
        for row_yt in yt:
            pp_partial = []
            #pp_stage0_next_partial=[]
            for elem_num in range(0, len(row_x)):
                pp_partial.append(row_x[elem_num] * row_yt[elem_num])
            pp_row.append(pp_partial)
        pp.append(pp_row)

    # stage 1: final sum generation
    for pp_row in pp:
        res_row = []
        for pp_col in pp_row:
            product = 0
            for pp_elem in pp_col:
                product = product + pp_elem
            res_row.append(product)
        res.append(res_row)
    return res
# generating test stimulus
x = [[1, 2, 3, 4], [5, 6, 7, 8]]
yt = [[1, 3, 5, 7], [2, 4, 6, 8]]
res = mat_mul(x, yt)
print("x: ", x)
print("yt: ", yt)
print("result: ", res)

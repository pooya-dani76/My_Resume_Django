def divideList(*, obj_list, division_to):
    result_list = []
    for i in range(0, len(obj_list), division_to):
        result_list.append(obj_list[i: i+division_to].copy())
    return result_list
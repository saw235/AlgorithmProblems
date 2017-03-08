
def reduce(list_arr, path_list=[]):

    
    path_list.append(list_arr[0])
    
    if len(list_arr) == 1:
        path = get_path(path_list[::-1])
        return list_arr, path

    
    for j, item in enumerate(list_arr[1]):
        temp = max(list_arr[0][j],list_arr[0][j+1])
        list_arr[1][j] += temp

    list_arr = list_arr[1:]
    ret = reduce(list_arr, path_list)

    return ret


def get_path(path_list):

    #remove the first row
    path_list = path_list[1:]

    #starting index
    i = 0

    path = [0]
    for j, item in enumerate(path_list):
        
        temp = max(path_list[j][i],path_list[j][i+1])
        i = path_list[j].index(temp)
        path.append(i)

    return path


f = open("text.txt", "r")

dat = []
for line in f:
    dat.append(line.rstrip().split(" "))


dat = dat[::-1]

data = []
for l in dat:
    data.append(list(map(lambda x: int(x), l)))

ans = reduce(data)

print(ans)


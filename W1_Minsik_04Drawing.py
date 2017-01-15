import matplotlib
list_of_lists = [[1,2],[3,3],[4,4],[5,2]]
x_list = [x for [x, y] in list_of_lists]
y_list = [y for [x, y] in list_of_lists]

plt.plot(x_list, y_list)

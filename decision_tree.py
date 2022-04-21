from imageio import imread
import matplotlib.pyplot as plt
import graphviz

ans =1*0.52*0.4*0.44+0*0.52*0.4*0.56+0.6*0.52*0.6*0.44+0.75*0.52*0.6*0.56+0+0.8*0.48*0.4*0.56+0.5*0.48*0.6*0.44+0
print(ans)
# 创建树对象
mygraph = graphviz.Digraph(node_attr={'shape': 'box'},
                           edge_attr={'labeldistance': "10.5"},
                           format="jpg")
# 构建节点
mygraph.node("0", "IB?")
mygraph.node("1", "LS?")
mygraph.node("2", "LS?")
mygraph.node("3", "S?")
mygraph.node("4", "S?")
mygraph.node("5", "S?")
mygraph.node("6", "S?")
mygraph.node("31", "GS")
mygraph.node("32", "﹁GS")
mygraph.node("33", "GS")
mygraph.node("34", "﹁GS")
mygraph.node("35", "GS")
mygraph.node("36", "﹁GS")
mygraph.node("37", "GS")
mygraph.node("38", "﹁GS")

mygraph.node("11", "2")
mygraph.node("12", "0")
mygraph.node("13", "0")
mygraph.node("14", "4")
mygraph.node("15", "4")
mygraph.node("16", "2")
mygraph.node("17", "3")
mygraph.node("18", "2")
mygraph.node("19", "0")
mygraph.node("20", "1")
mygraph.node("21", "4")
mygraph.node("22", "2")
mygraph.node("23", "2")
mygraph.node("24", "2")
mygraph.node("25", "0")
mygraph.node("26", "2")

# 构建边
mygraph.edge("0", "1", label="Yes")
mygraph.edge("0", "2", label="No")
mygraph.edge("1", "3", label="Yes")
mygraph.edge("1", "4", label="No")
mygraph.edge("2", "5", label="Yes")
mygraph.edge("2", "6", label="No")

mygraph.edge("3", "31", label="Yes")
mygraph.edge("3", "32", label="No")
mygraph.edge("4", "33", label="Yes")
mygraph.edge("4", "34", label="No")

mygraph.edge("5", "35", label="Yes")
mygraph.edge("5", "36", label="No")
mygraph.edge("6", "37", label="Yes")
mygraph.edge("6", "38", label="No")

mygraph.edge("31", "11", label="Yes")
mygraph.edge("31", "12", label="No")
mygraph.edge("32", "13", label="Yes")
mygraph.edge("32", "14", label="No")
mygraph.edge("33", "15", label="Yes")
mygraph.edge("33", "16", label="No")
mygraph.edge("34", "17", label="Yes")
mygraph.edge("34", "18", label="No")
mygraph.edge("35", "19", label="Yes")
mygraph.edge("35", "20", label="No")
mygraph.edge("36", "21", label="Yes")
mygraph.edge("36", "22", label="No")
mygraph.edge("37", "23", label="Yes")
mygraph.edge("37", "24", label="No")
mygraph.edge("38", "25", label="Yes")
mygraph.edge("38", "26", label="No")




# 渲染
mygraph.render("decisionTree")

# 图形显示
ax = plt.gca()  # 获取图形坐标轴
ax.imshow(imread("decisionTree.jpg"))  # 读取生成的图片
ax.set_axis_off()  # 图形不嫌弃是坐标
plt.show()  # 显示图形

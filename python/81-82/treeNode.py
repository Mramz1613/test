# """
# структура данных
#
# Дерово
# """
# #Создание дерева с помощью библиотеки
#
# from anytree import Node, RenderTree
#
#
#
#
# grand = Node("Дед")
# mother = Node("Мама",parent=grand)
# father = Node("Папа",parent=grand)
# me = Node("Я",parent=mother)
# for pre, fill, node in RenderTree(grand): #это вызов конситруктора __init__() из класса рендер три
#     print("%s%s" % (pre, node.name)) #вывод в строковом формате для отрисовки дерева
# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.children = []
#         print("Создали узел")
#
#     def add_child(self,node): #добавить дочерний узел
#         self.children.append(node)
#
#     def show(self):
#         print(self.children)
#
# objRoot = TreeNode(0)
# objRoot.add_child(TreeNode(1))
# objRoot.add_child(TreeNode(2))
# objRoot.add_child(TreeNode(4))
# objRoot.show()

#граф состоит из излов и ребер,кол - во ребер не ограничено
#библеотека для графф : networkx,

import networkx as nx
objGraf = nx.Graph()
objGraf.add_node(1)
objGraf.add_nodes_from([2,3,4])
objGraf.add_edge(1,2)
objGraf.add_edges_from([1,3])
print(objGraf.nodes.data())
print(objGraf.edges)


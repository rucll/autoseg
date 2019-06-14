import Autoseg


a1 = Autoseg.NewAutoSegRep("L0L")
print(a1.positions)
print(a1.orderEdges)
print(a1.assocEdges)
print(a1.labels)
a1.printDiag()
from manager.manager import Manager

manager = Manager()
manager.put("0", "0")
manager.put("1", "1")
manager.put("2", "2")
manager.put("3", "3")
manager.put("4", "4")
manager.put("5", "5")
manager.put("6", "6")
manager.put("7", "7")
manager.put("8", "8")
manager.put("9", "9")
manager.put("A", "A")
manager.put("B", "B")
manager.put("C", "C")
manager.put("D", "D")
manager.put("E", "E")
manager.put("F", "F")
manager.grow_nodes_by_factor(4)
manager.grow_nodes_by_factor(2)
manager.shrink_nodes_by_factor(0.5)
stop = True
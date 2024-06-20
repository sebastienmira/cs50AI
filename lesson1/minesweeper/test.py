for i in set():
    a=1
    print(a)

cells={(1,1), (1,2), (1,3)}
mines_found={(1,1) ,(1,2)}
cells_copy=cells.copy()

#print(cells<cells)

'''
cells=cells-cells.intersection(mines_found)
#print(cells)
#print(cells_copy)

from minesweeper import Sentence, MinesweeperAI
  
knowledge = []
s = Sentence(set([(0,0),(0,1),(1,0),(2,0)]), 2)
knowledge.append(s)
s = Sentence(set([(0,0),(0,1),(0,2)]), 3)
knowledge.append(s)

ai=MinesweeperAI()
ai.knowledge=knowledge
print(ai.make_safe_move())
'''
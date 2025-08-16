import os
import sys

class dirFind:
    @classmethod
    def addSpace(cls,level):
        sys.stdout.write(" " * level * 5)
    @classmethod
    def dirFind(cls,path, level=0):
        if os.path.exists(path):
            for i in (os.listdir(path)):
                new = os.path.join(path, i)
                if os.path.isfile(new):
                    dirFind.addSpace(level)
                    print(f"{i}")
                    # print("\n")
                elif os.path.isdir(new):
                    dirFind.addSpace(level)
                    print(f"{i}")
                    level += 1
                    # print("\n")
                    # path=path+'/'+i
                    cls.dirFind(new, level)
                    level -= 1



# #path=input("输入查询目录")
# path=r"F:/毕业/培训/四阶段"
# def addSpace(level):
#         sys.stdout.write(" " * level*5)
#
# def dirFind(path,level):
#     if  os.path.exists(path):
#         #print(os.listdir(path))
#         #length1=len(os.listdir(path))
#         for i in (os.listdir(path)):
#             new=os.path.join(path,i)
#             if os.path.isfile(new):
#                 addSpace(level)
#                 print(f"{i}")
#                 #print("\n")
#             elif os.path.isdir(new):
#                 addSpace(level)
#                 print(f"{i}")
#                 level += 1
#                 #print("\n")
#                 #path=path+'/'+i
#                 dirFind(new,level)
#                 level -= 1
#                 #os.path.join(path, os.listdir(path)[i])
#                 #return dirFind(os.path.join(path, os.listdir(path)[i]))
# dirFind(path,0)

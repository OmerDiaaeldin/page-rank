import os
from shutil import copytree

path1 = '/home/odaio/PycharmProjects/pagerank/'
path2 = '/home/odaio/PycharmProjects/competitve/'

x = os.listdir(path1)
y = os.listdir(path2)
print(x)
print(y)

copytree(path2,os.path.join(path1,'experiment'))
print(x)
print(y)
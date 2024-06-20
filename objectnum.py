#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にオブジェクト情報が表示される。

import bpy

length = len(bpy.data.objects)
print("Object Num "+str(length))

for o in range(0,length):
  name = bpy.data.objects[o].name
  print("Object {0}, Object Name {1}".format(o,name))

objs = [o for o in bpy.data.objects if o.type == "MESH"]
length = len(objs)
print("Mesh Object Num "+str(length))

for o in range(length):
  obj = objs[o]
  print("Mesh Object {0}, Mesh Name {1}".format(o,obj.data.name))

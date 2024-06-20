#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面に頂点情報が表示される。

import bpy

objs = []
for o in bpy.data.objects:
  if o.type == "MESH":
    objs.append(o)
    
for o in range(len(objs)):
  mesh = bpy.data.meshes[objs[o].data.name]
  print("Mesh Object {0}, Vertex Num {1}".format(o,len(mesh.vertices)))

for o in range(len(objs)):
  mesh = bpy.data.meshes[objs[o].data.name]
  for v in mesh.vertices:
    print("Mesh Object {0}, Vertex({1},{2},{3})".format(o,v.co.x,v.co.y,v.co.z))

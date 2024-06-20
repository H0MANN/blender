#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にマテリアル情報が表示される。

import bpy

length = len(bpy.data.materials)
print("Material Num "+str(length))

for m in range(length):
  ma = bpy.data.materials[m]
  print("Material {0}, Material Name {1}".format(m,ma.name))

o_num = 0
objs = [o for o in bpy.data.objects if o.type == "MESH"]
for o in objs:
  s_num = 0
  for m in o.material_slots:
    if not (m.material is None):
      s_num += 1
  print("Mesh Object {0}, Material Slot Num {1}".format(o_num,s_num))
  o_num += 1

for o in range(len(objs)):
  obj = objs[o]
  for m in obj.material_slots:
    if not (m.material is None):
      print("Mesh Object {0}, Material Name {1}".format(o,m.material.name))

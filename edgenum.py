#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面に辺情報が表示される。

import bpy
import bmesh

objs = [o for o in bpy.data.objects if o.type == "MESH"]
o_num = 0
for o in objs:
  bpy.context.view_layer.objects.active = o
  bpy.ops.object.mode_set(mode = 'EDIT')
  me = o.data
  bm = bmesh.from_edit_mesh(me)
  e_num = 0
  for e in bm.edges:
    e_num += 1
  print("Mesh Object {0}, Edge Num {1}".format(o_num,e_num))
  o_num += 1

bpy.ops.object.mode_set(mode = 'OBJECT')

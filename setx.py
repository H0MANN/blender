#オブジェクトをクリックし、「Edit Mode」で好きなだけ頂点を選択。
#スクリプトを実行すると、選択頂点のX座標が0になる。

import bpy
import bmesh

bpy.ops.object.mode_set(mode = 'EDIT')

object = bpy.context.active_object
bm = bmesh.from_edit_mesh(object.data)
for v in bm.verts:
  if v.select:
    v.co.x = 0

bpy.ops.object.mode_set(mode = 'OBJECT')


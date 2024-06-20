#「File」→「New」→「General」メニューを実行。
#スクリプトを実行すると、猿とアニメーションが作成される。
#「Animation」タブで、「▶」ボタンをクリックしたらアニメーションが再生される。

import bpy

for m in bpy.data.meshes:
  bpy.data.meshes.remove(m)

bpy.ops.mesh.primitive_monkey_add()

positions = (0,0,0),(5,5,0),(5,-5,0),(-5,5,0),(-5,-5,0),(0,0,0)
for o in bpy.data.objects:
  if o.type == "MESH":
    obj = o
obj.animation_data_clear()
frame = 0
for p in positions:
  bpy.context.scene.frame_set(frame)
  obj.location = p
  obj.keyframe_insert(data_path="location")
  frame += 50

bpy.context.scene.frame_set(0)

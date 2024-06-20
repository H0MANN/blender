#任意のメッシュオブジェクトをクリック。
#スクリプトを実行したら、DeltaX,DeltaY,DeltaZの増分をセットし、「OK」する。
#アクティブなオブジェクトの頂点が増分までランダムに平行移動される。

import bpy
import random

class DialogOperator(bpy.types.Operator):
  bl_idname = "object.dialog_operator"
  bl_label = "Random Move Dialog Operator"
  bl_options = {'REGISTER', 'UNDO'}

  def execute(self, context):
    self.random_move()
    return {'FINISHED'}

  def invoke(self, context, event):
    wm = context.window_manager
    return wm.invoke_props_dialog(self)

  def random_move(self):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    o = bpy.context.active_object
    if o.type == "MESH":
      mesh = bpy.data.meshes[o.data.name]
      for v in mesh.vertices:
        if v.select == True:
          v.co[0] += random.uniform(-1,1)
          v.co[1] += random.uniform(-1,1)
          v.co[2] += random.uniform(-1,1)


bpy.utils.register_class(DialogOperator)

bpy.ops.object.dialog_operator('INVOKE_DEFAULT')
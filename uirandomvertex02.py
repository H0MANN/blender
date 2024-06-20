#任意のメッシュオブジェクトをクリック。
#スクリプトを実行したら、DeltaX,DeltaY,DeltaZの増分をセットし、「OK」する。
#アクティブなオブジェクトの頂点が増分までランダムに平行移動される。

import bpy
import random

class DialogOperator(bpy.types.Operator):
  bl_idname = "object.dialog_operator"
  bl_label = "Random Move Dialog Operator"
  bl_options = {'REGISTER', 'UNDO'}

  delta_x: bpy.props.FloatProperty(name="DeltaX")
  delta_y: bpy.props.FloatProperty(name="DeltaY")
  delta_z: bpy.props.FloatProperty(name="DeltaZ")

  def execute(self, context):
    self.random_move()
    message = (
      "Popup Values: %f, %f, '%f'" %
      (self.delta_x, self.delta_y, self.delta_z)
    )
    self.report({'INFO'}, message)
    return {'FINISHED'}

  def invoke(self, context, event):
    wm = context.window_manager
    return wm.invoke_props_dialog(self)

  def random_move(self):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    o = bpy.context.active_object
    if o.type == "MESH":
      mesh = bpy.data.meshes[o.data.name]
      x = self.delta_x
      y = self.delta_y
      z = self.delta_z
      for v in mesh.vertices:
        if v.select == True:
          v.co[0] += random.uniform(-x,x)
          v.co[1] += random.uniform(-y,y)
          v.co[2] += random.uniform(-z,z)


bpy.utils.register_class(DialogOperator)

bpy.ops.object.dialog_operator('INVOKE_DEFAULT')
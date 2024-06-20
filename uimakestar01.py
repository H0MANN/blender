#このスクリプトを実行したら、「Object Mode」→「Add」→「Mesh」→「Make Star」メニューを実行
#「3Dビュー」の左下に「▶ Make Star」パネルが現れるのでクリック
#「star_num」「star_size」を左右にドラッグ

import bpy
from bpy.props import *
import math

class MakeStar(bpy.types.Operator):
  bl_idname = "make.makestar"
  bl_label = "Make Star"
  bl_options = {'REGISTER', 'UNDO'}

  def invoke(self, context, event):
    return self.execute(context)

  def execute(self, context):
    return {'FINISHED'}

def func_makestar(self, context):
  self.layout.operator(MakeStar.bl_idname, text="Make Star")

def register():
  bpy.utils.register_class(MakeStar)
  bpy.types.VIEW3D_MT_mesh_add.append(func_makestar)

def unregister():
  bpy.utils.unregister_class(MakeStar)
  bpy.types.VIEW3D_MT_mesh_add.remove(func_makestar)

if __name__ == "__main__":
  register()

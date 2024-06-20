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

  star_num: IntProperty(min=3)
  star_size: FloatProperty(min=1)
  
  def invoke(self, context, event):
    self.star_num = 5
    self.star_size = 2.0
    
    return self.execute(context)
  
  def execute(self, context):
    self.make()

    return {'FINISHED'}
 
  def make(self):
    name = "Star"
    verts = [(0,0,0)]
    faces = []
    for i in range(self.star_num):
      radian = math.radians(i*360/self.star_num)
      x = math.sin(radian)*self.star_size
      z = math.cos(radian)*self.star_size
      verts.append((x,0,z))
      radian = math.radians((i+0.5)*360/self.star_num)
      x = math.sin(radian)
      z = math.cos(radian)
      verts.append((x,0,z))
    num = self.star_num*2
    for i in range(1,num+1):
      index = (i%num)+1
      faces.append((0,i,index))
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(object)
    mesh.from_pydata(verts,[],faces)
    mesh.update()
    

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

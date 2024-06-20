#スクリプトを実行したら、各面の頂点から三角形が生成される。

import bpy
import random


class MakeFur():
  name = "Fur Polygon"

  def __init__(self):
    self.verts = []
    self.faces = []
    self.index = 0
    if self.name in bpy.data.meshes:
      bpy.data.meshes.remove(bpy.data.meshes[self.name])

  def make(self,num,min,max,size):
    o = bpy.context.active_object
    mesh = bpy.data.meshes[o.name]
    for f in range(len(mesh.polygons)):
      poly = mesh.polygons[f]
      vi = poly.vertices
      v0 = mesh.vertices[vi[0]].co
      v1 = mesh.vertices[vi[1]].co
      v2 = mesh.vertices[vi[2]].co
      n = poly.normal + v0
      self.verts.append(n)
      self.verts.append(v0)
      self.verts.append(v1)
      self.faces.append((f*3,f*3+1,f*3+2))
    mesh = bpy.data.meshes.new(self.name)
    object = bpy.data.objects.new(self.name, mesh)
    bpy.context.collection.objects.link(object)
    bpy.ops.object.mode_set(mode = 'OBJECT')
    mesh.from_pydata(self.verts,[],self.faces)
    mesh.update()

if __name__ == "__main__":
  fur = MakeFur()
  fur.make(5,0.5,1.0,0.1)

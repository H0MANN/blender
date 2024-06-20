#スクリプトを実行したら、毛を1本ずつ生成する。

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
    mesh = bpy.data.meshes[o.data.name]
    for f in range(len(mesh.polygons)):
      poly = mesh.polygons[f]
      if poly.select == False:
        continue
      vi = poly.vertices
      v0 = mesh.vertices[vi[0]].co
      v1 = mesh.vertices[vi[1]].co
      v2 = mesh.vertices[vi[2]].co
      n = poly.normal*random.uniform(min,max)
      self.make_polygon(v0,v1,v2,n,size)
    mesh = bpy.data.meshes.new(self.name)
    object = bpy.data.objects.new(self.name, mesh)
    bpy.context.collection.objects.link(object)
    bpy.ops.object.mode_set(mode = 'OBJECT')
    mesh.from_pydata(self.verts,[],self.faces)
    mesh.update()

  def make_polygon(self,p0,p1,p2,normal,size):
    center = (p0+p1+p2)/3
    v0 = center + (p0-center)*size
    v1 = center + (p1-center)*size
    v2 = center + (p2-center)*size
    n = center + normal
    self.verts.append(n)
    self.verts.append(v0)
    self.verts.append(v1)
    self.verts.append(v2)
    self.faces.append((self.index,self.index+1,self.index+2))
    self.faces.append((self.index,self.index+2,self.index+3))
    self.faces.append((self.index,self.index+3,self.index+1))
    self.index += 4

if __name__ == "__main__":
  fur = MakeFur()
  fur.make(5,0.5,1.0,0.1)

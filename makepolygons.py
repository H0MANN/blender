#スクリプトを実行すると、ピラミッドが表示される。

import bpy

verts = [(0,0,10),(10,10,-10),(-10,10,-10),
         (-10,-10,-10),(10,-10,-10)]
faces = [(0,1,2),(0,2,3),(0,3,4),(0,4,1),(4,3,2,1)]
name = "Polygons"

def delete_all():
  for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
  for item in bpy.data.materials:
    bpy.data.materials.remove(item)

def make_polygons():
  mesh = bpy.data.meshes.new(name)
  object = bpy.data.objects.new(name, mesh)
  bpy.context.collection.objects.link(object)
  mesh.from_pydata(verts,[],faces)
  mesh.update()

if __name__ == "__main__":
  delete_all()
  make_polygons()

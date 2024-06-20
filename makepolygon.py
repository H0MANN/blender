#スクリプトを実行すると、三角形が表示される。

import bpy


for item in bpy.data.meshes:
  bpy.data.meshes.remove(item)

verts = [(0,0,10),(10,0,-10),(-10,0,-10)]
faces = [(0,1,2)]
name = "Polygon"

mesh = bpy.data.meshes.new(name)
object = bpy.data.objects.new(name, mesh)
bpy.context.collection.objects.link(object)
mesh.from_pydata(verts,[],faces)
mesh.update()

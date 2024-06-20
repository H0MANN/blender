#スクリプトを実行すると、顔のテクスチャが貼られた正方形が表示される。

import bpy
import bmesh

verts = [(-10,0,10),(10,0,10),(10,0,-10),(-10,0,-10)]
faces = [(0,1,2,3)]
uvs = [(0,1),(1,1),(1,0),(0,0)]
name = "Triangle"

def make_quad():
  mesh = bpy.data.meshes.new(name)
  object = bpy.data.objects.new(name, mesh)
  bpy.context.collection.objects.link(object)
  mesh.from_pydata(verts,[],faces)
  me = object.data
  me.uv_layers.new(name=name)
  for i in range(len(uvs)):
    me.uv_layers[0].data[i].uv = uvs[i]
  mesh.update()

if __name__ == "__main__":
  make_quad()
  bpy.ops.object.mode_set(mode = 'OBJECT')

#スクリプトを実行すると、顔のテクスチャが貼られた正方形が表示される。

import bpy
import bmesh
import os
import sys
script_file = os.path.basename(__file__)
script_path = bpy.data.texts[script_file].filepath
script_dir = os.path.dirname(script_path)

verts = [(-10,0,10),(10,0,10),(10,0,-10),(-10,0,-10)]
faces = [(0,1,2,3)]
uvs = [(0,1),(1,1),(1,0),(0,0)]
name = "Triangle"

def delete_all():
  for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
  for item in bpy.data.materials:
    bpy.data.materials.remove(item)

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
  bpy.context.view_layer.objects.active = object
  bpy.ops.object.mode_set(mode = 'EDIT')
  mesh = bmesh.from_edit_mesh(object.data)
  mesh.select_mode = {'FACE'}
  mesh.faces.ensure_lookup_table()
  make_material("Color",(1,0,0,1))
  mesh.faces[0].material_index = 0
   
def make_material(name,color):
  ma = bpy.data.materials.new(name)
  ma.use_nodes = True
  bsdf = ma.node_tree.nodes["Principled BSDF"]
  bsdf.inputs[0].default_value = color
  img = ma.node_tree.nodes.new('ShaderNodeTexImage')
  path = script_dir+"/"+"../Assets/LadyEye.png"
  img.image = bpy.data.images.load(path)
  ma.node_tree.links.new(bsdf.inputs['Base Color'],img.outputs['Color'])
  bpy.context.object.data.materials.append(ma)
  ma.diffuse_color = color

if __name__ == "__main__":
  delete_all()
  make_quad()
  bpy.ops.object.mode_set(mode = 'OBJECT')

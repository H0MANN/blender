#スクリプトを実行すると、キューブがsinに沿って並ぶ。

import bpy
import math
import colorsys

HALF_NUM = 50

def delete_all():
  for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
  for item in bpy.data.materials:
    bpy.data.materials.remove(item)

def make_cube(x,y,z):
  loc = (x,y,z)
  cube = bpy.ops.mesh.primitive_cube_add(location=loc,size=2)
  bpy.ops.object.material_slot_add()

def make_cubes(num):
  for x in range(-num,num):
    z = math.sin(math.radians(x*10))*10
    make_cube(x,0,z)
   
def make_material(name,color):
  ma = bpy.data.materials.new(name)
  ma.use_nodes = True
  bsdf = ma.node_tree.nodes["Principled BSDF"]
  bsdf.inputs[0].default_value = color
  bsdf.inputs[4].default_value = 1
  bsdf.inputs[7].default_value = 0
  bpy.context.object.data.materials.append(ma)
  ma.diffuse_color = color
  return ma

def make_materials(num):
  mats = []
  for i in range(num):
    name = "Color"+str(i)
    rgb = colorsys.hsv_to_rgb(i/num,1,1)
    mats.append(make_material(name,(rgb[0],rgb[1],rgb[2],1)))
  return mats

def set_materials(mats):
  index = 0
  for o in bpy.data.objects:
    for m in o.material_slots:
      m.material = mats[index]
      index += 1
      break

if __name__ == "__main__":
  delete_all()    
  make_cubes(HALF_NUM)
  mats = make_materials(HALF_NUM*2)
  set_materials(mats)

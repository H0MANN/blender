#スクリプトを実行すると、球が7x7だけ作成される。

import bpy
import random


NUM_X = 7
NUM_Y = 7


def delete_all():
  for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
  for item in bpy.data.materials:
    bpy.data.materials.remove(item)

def make_sphere(x,y,z):
  loc = (x,y,z)
  cube = bpy.ops.mesh.primitive_uv_sphere_add(location=loc)
  bpy.ops.object.material_slot_add()
  r = random.random()
  g = random.random()
  b = random.random()
  ma = make_material("Color"+str(x)+str(y),(r,g,b,1))
  for m in bpy.context.active_object.material_slots:
    m.material = ma

def make_spheres(num_x,num_y):
  for x in range(num_x):
    for y in range(num_y):
      make_sphere(x*2-(num_x-1),y*2-(num_y-1),0)

def make_material(name,color):
  ma = bpy.data.materials.new(name)
  ma.diffuse_color = color
  bpy.context.object.data.materials.append(ma)
  return ma

if __name__ == "__main__":
  delete_all()    
  make_spheres(NUM_X,NUM_Y)

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

if __name__ == "__main__":
  delete_all()    
  make_cubes(HALF_NUM)

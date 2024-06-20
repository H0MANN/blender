#スクリプトを実行すると、球が7x7だけ作成される。

import bpy
import random

NUM_X = 7
NUM_Y = 7

def make_sphere(x,y,z):
  loc = (x,y,z)
  cube = bpy.ops.mesh.primitive_uv_sphere_add(location=loc)

def make_spheres(num_x,num_y):
  for x in range(num_x):
    for y in range(num_y):
      make_sphere(x*2-(num_x-1),y*2-(num_y-1),0)

if __name__ == "__main__":
  make_spheres(NUM_X,NUM_Y)

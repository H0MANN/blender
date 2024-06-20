#スクリプトを実行すると、面の色がバラバラのトーラスが作成される。

import bpy
import bmesh
import random

class Torus():

  def __init__(self):
    for item in bpy.data.meshes:
      bpy.data.meshes.remove(item)
    for item in bpy.data.materials:
      bpy.data.materials.remove(item)

  def make(self):
    bpy.ops.mesh.primitive_torus_add(
      major_segments=24,minor_segments=8,
      major_radius=5,minor_radius=2)

if __name__ == "__main__":
  torus = Torus()
  torus.make()
  bpy.ops.object.mode_set(mode = 'OBJECT')

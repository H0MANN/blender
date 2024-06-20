#スクリプトを実行すると、円筒とボーンアニメーションが作成される。
#「Animation」タブで、「▶」ボタンをクリックしたらボーンアニメーションが再生される。

import bpy
import math


class BoneAnimation():

  def __init__(self):
    for a in bpy.data.armatures:
      bpy.data.armatures.remove(a)
    for m in bpy.data.meshes:
      bpy.data.meshes.remove(m)

  def make_objects(self):
    bpy.ops.object.add(type='ARMATURE')
    self.amt = bpy.data.objects["Armature"]
    bpy.ops.mesh.primitive_cylinder_add()
    self.obj = bpy.data.objects["Cylinder"]
    bpy.context.view_layer.objects.active = self.amt

if __name__ == "__main__":
  bone = BoneAnimation()
  bone.make_objects()
  bpy.context.scene.frame_set(0)

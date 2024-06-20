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

  def make_bones(self):
    bpy.ops.object.mode_set(mode='EDIT')
    b = self.amt.data.edit_bones.new('Bone')
    b.head = (0,0,-1)
    b.tail = (0,0,0)
    b2 = self.amt.data.edit_bones.new('Bone2')
    b2.head = b.tail
    b2.tail = (0,0,1)
    b2.parent = b

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.objects.active = self.obj
    bpy.context.view_layer.objects.active = self.amt
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')


if __name__ == "__main__":
  bone = BoneAnimation()
  bone.make_objects()
  bone.make_bones()
  bpy.context.scene.frame_set(0)

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

  def animation(self):
    bone2 = self.amt.pose.bones['Bone2']
    rotations = (0,0,0),(90,0,0),(-90,0,0),(0,90,0),(0,-90,0),(0,0,90),(0,0,-90),(0,0,0)
    bone2.rotation_mode = "XYZ"
    frame = 0
    for r in rotations:
      bone2.rotation_euler.x = math.radians(r[0])
      bone2.rotation_euler.y = math.radians(r[1])
      bone2.rotation_euler.z = math.radians(r[2])
      bone2.keyframe_insert("rotation_euler",frame=frame)
      frame += 35


if __name__ == "__main__":
  bone = BoneAnimation()
  bone.make_objects()
  bone.make_bones()
  bone.animation()
  bpy.context.scene.frame_set(0)

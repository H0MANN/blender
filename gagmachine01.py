#スクリプトを実行したら、アニメーションタブをクリック
#「▶」ボタンをクリックしてアニメーションを再生すればランダムに動くギャグ製造機

import bpy
import math
import random

objs = []
rot_range = (10,45,90,90,90,90,90,90,90,90)

def make_cube(parent,loc,scale,pivot):
    bpy.ops.mesh.primitive_cube_add(location=loc,scale=scale)
    obj = bpy.context.active_object
    x = obj.location.x + pivot[0]
    y = obj.location.y + pivot[1]
    z = obj.location.z + pivot[2]
    bpy.context.scene.cursor.location=(x,y,z)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    if parent is not None:
        obj.parent = parent
    return obj

loc = (0,0,0)
scale = (3,1.5,4)
pivot = (0,0,-2)
objs.append(make_cube(None,loc,scale,pivot))

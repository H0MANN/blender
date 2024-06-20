#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にアニメーション情報が表示される。

import bpy

WXYZ = ("w","x","y","z")
XYZ = ("x","y","z")

def search_keyframes(obj):
  if obj.animation_data == None:
    return
  fcurves = obj.animation_data.action.fcurves
  for fc in fcurves:
    if "rotation_quaternion" in fc.data_path:
      print_keyframes(fc,WXYZ,"quaternion")
    elif "rotation_axis_angle" in fc.data_path:
      print_keyframes(fc,WXYZ,"axis_angle")
    elif "rotation_euler" in fc.data_path:
      print_keyframes(fc,XYZ,"rotation")
    elif "scale" in fc.data_path:
      print_keyframes(fc,XYZ,"scale")
    elif "location" in fc.data_path:
      print_keyframes(fc,XYZ,"location")

def print_keyframes(fc,array,trans):
  for kp in fc.keyframe_points:
    frame = int(kp.co[0])
    axis = array[fc.array_index]
    v = kp.co[1]
    print("key {}, {} {} = {}".format(frame,trans,axis,v))

for o in bpy.data.objects:
  if o.type == "MESH" or o.type == "ARMATURE":
    print(o.name)
    search_keyframes(o)

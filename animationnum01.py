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
    print(fc.data_path)

for o in bpy.data.objects:
  if o.type == "MESH" or o.type == "ARMATURE":
    print(o.name)
    search_keyframes(o)

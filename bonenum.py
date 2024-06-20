#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にボーン情報が表示される。

import bpy #①

for o in bpy.data.objects: #②
  if o.pose == None: #③
    continue #④
  bpy.context.view_layer.objects.active = o #⑤
  bpy.ops.object.mode_set(mode='POSE') #⑥
  for b in o.pose.bones: #⑦
    loc = b.location #⑧
    if 'QUATERNION' in b.rotation_mode: #⑨
      rot = b.rotation_quaternion #⑩
    elif 'AXIS_ANGLE' in b.rotation_mode: #⑪
      rot = b.rotation_axis_angle #⑫
    else: #⑬
      rot = b.rotation_euler #⑭
    print("Bone Name {}, {}, {}".format(b.name,loc,rot)) #⑮

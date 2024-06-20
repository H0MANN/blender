#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にUV情報が表示される。

import bpy


objs = [o for o in bpy.data.objects if o.type == "MESH"]
for o in objs:
  mesh = bpy.data.meshes[o.data.name]
  for layer in mesh.uv_layers:
    for idx, dat in enumerate(mesh.uv_layers[layer.name].data):
      s = ",".join([str(uv) for uv in dat.uv])
      print("UV Index {}, UV({})".format(idx,s))

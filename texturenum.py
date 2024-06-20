#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にテクスチャ情報が表示される。

import bpy

for o in bpy.data.objects:
  for m in o.material_slots:
    if m.material.node_tree is not None:
      nodes = m.material.node_tree.nodes
      for n in nodes:
        if n.type == 'TEX_IMAGE':
          print(n.image.filepath)

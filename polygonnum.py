#PyTest.blendファイルを開く。
#スクリプトを実行し、システムコンソール画面がなければ「Window」→「Toggle System Console」メニュー実行。
#システムコンソール画面にメッシュ情報が表示される。

import bpy

for m in range(len(bpy.data.meshes)):
  mesh = bpy.data.meshes[m]
  print("Mesh Object {0}, Polygon Num {1}".format(m,len(mesh.polygons)))
  for p in range(len(mesh.polygons)):
    verts = mesh.polygons[p].vertices
    s = str(verts[0])
    for v in range(1,len(verts)):
      s = s +","+str(verts[v])
    print("Polygon {}, Index({})".format(p,s));

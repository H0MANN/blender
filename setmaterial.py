#スクリプトを実行すると、表示オブジェクトがランダムな色に変更される。

import bpy
import random


for m in bpy.data.materials:
  r = random.random()
  g = random.random()
  b = random.random()
  color = (r,g,b,1)
  m.use_nodes = True
  bsdf = m.node_tree.nodes["Principled BSDF"]
  bsdf.inputs[0].default_value = color
  bsdf.inputs[4].default_value = 1
  bsdf.inputs[7].default_value = 0
  m.diffuse_color = color

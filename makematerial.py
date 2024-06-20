#「File」→「New」→「General」メニューを実行。
#スクリプトを実行すると、キューブが青いマテリアルになる。

import bpy
   
def make_material(name,color):
  ma = bpy.data.materials.new(name)
  ma.use_nodes = True
  bsdf = ma.node_tree.nodes["Principled BSDF"]
  bsdf.inputs[0].default_value = color
  bsdf.inputs[4].default_value = 1
  bsdf.inputs[7].default_value = 0
  bpy.context.object.data.materials.append(ma)
  ma.diffuse_color = color
  return ma

def set_material(ma):
  for o in bpy.data.objects:
    for m in o.material_slots:
      m.material = ma

if __name__ == "__main__":
  ma = make_material("Color",(0,0,1,1))
  set_material(ma)

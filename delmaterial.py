#スクリプトを実行したら、オブジェクトに使われていないマテリアルをマテリアルスロットから削除

import bpy


def delete():
  objs = [o for o in bpy.data.objects if o.type == "MESH"]
  for obj in objs:
    m_count = []
    mesh = bpy.data.meshes[obj.data.name]
    for m in mesh.materials:
      m_count.append(0)
    for face in mesh.polygons:
      m_count[face.material_index] += 1

    for i in range(0,len(obj.material_slots))[::-1]:
      if m_count[i] == 0:
        obj.active_material_index = i
        bpy.ops.object.material_slot_remove({'object': obj})
      
      
if __name__ == '__main__':
  delete()

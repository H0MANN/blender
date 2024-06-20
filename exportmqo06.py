import bpy

class SaveMQO():

  def save_mqo(self,context, filepath, scale_setting):
    count = 0
    for o in bpy.data.objects:
      for m in o.material_slots:
        count += 1

    with open(filepath, 'w') as file:
      file.write("Metasequoia Document\n")
      file.write("Format Text Ver 1.0\n\n")

      file.write("Scene {\n")
      file.write("}\n")

      file.write("Material "+format(count)+" {\n")
      for o in bpy.data.objects:
        for m in o.material_slots:
          if m.material.node_tree is None:
            col = m.material.diffuse_color
            file.write(
              '\t"{0}" shader(3) col({1} {2} {3} 1) '.format(
              m.name,col[0],col[1],col[2]))
            file.write('dif(1) amb(0) emi(0) spc(0) power(5)\n')
          else:
            self.col = (1,1,1)
            nodes = m.material.node_tree.nodes
            for mat_node in nodes:
              if mat_node.type == 'OUTPUT_MATERIAL':
                self.follow_links(mat_node)
            file.write(
              '\t"{0}" shader(3) col({1} {2} {3} 1) '.format(
              m.name,self.col[0],self.col[1],self.col[2]))
            file.write('dif(1) amb(0) emi(0) spc(0) power(5)')
            for n in nodes:
              if n.type == 'TEX_IMAGE':
                file.write(' tex("{0}")'.format(n.image.filepath))
                break
            file.write('\n')
      file.write("}\n")

      objs = [o for o in bpy.data.objects if o.type == "MESH"]
      m_count = 0
      for o in objs:
        mesh = bpy.data.meshes[o.data.name]
        file.write('Object "'+o.name+'" {\n')
        file.write("\tfacet {0}\n".format(89.5))
        file.write("\tvertex "+str(len(mesh.vertices))+" {\n")
        for v in mesh.vertices:
          x = (v.co[0]+o.location[0])*scale_setting
          y = (v.co[2]+o.location[2])*scale_setting
          z = -(v.co[1]+o.location[1])*scale_setting
          file.write("\t\t{0} {1} {2}\n".format(x,y,z))
        file.write("\t}\n")
        file.write("\tface 1 {\n")
        file.write("\t\t3 V(2 1 0) M(0) UV(0 0 1 0 1 1)\n")
        file.write("\t}\n")
        file.write("}\n")
      file.write("Eof\n")

    return {'FINISHED'}

  def follow_links(self,node_in):
    for n_inputs in node_in.inputs:
      for node_links in n_inputs.links:
        node = node_links.from_node
        if "Color" in node.inputs:
          self.col = node.inputs["Color"].default_value
          return
        elif "Base Color" in node.inputs:
          self.col = node.inputs["Base Color"].default_value
          return
        self.follow_links(node_links.from_node)

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, FloatProperty
from bpy.types import Operator
      
class ExportSomeData(Operator, ExportHelper):
  bl_idname = "export_mqo.some_data"
  bl_label = "Export MQO Data"

  filename_ext = ".mqo"

  filter_glob: StringProperty(
    default="*.mqo",
    options={'HIDDEN'},
    maxlen=255,
  )

  scale_setting: FloatProperty(
    name="Scale",
    description="Scale",
    default=100.0,
		min=0.01
  )

  def execute(self, context):
    model = SaveMQO()
    return model.save_mqo(
      context,self.filepath,self.scale_setting)


def menu_func_export(self, context):
  self.layout.operator(
    ExportSomeData.bl_idname, text="Metasequoia Exporter (.mqo)")


def register():
  bpy.utils.register_class(ExportSomeData)
  bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
  bpy.utils.unregister_class(ExportSomeData)
  bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
  register()

  bpy.ops.export_mqo.some_data('INVOKE_DEFAULT')

import bpy

class SaveMQO():

  def save_mqo(self,context, filepath, scale_setting):
    with open(filepath, 'w') as file:
      file.write("Metasequoia Document\n")
      file.write("Format Text Ver 1.0\n\n")

      file.write("Scene {\n")
      file.write("}\n")

      file.write("Material 1 {\n")
      file.write('\t"material" shader(3) col(1 0 0 1) ')
      file.write('dif(1) amb(0) emi(0) spc(0) power(5)\n')
      file.write("}\n")
      file.write("Eof\n")

    return {'FINISHED'}


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

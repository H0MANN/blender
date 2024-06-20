import bpy
from bpy_extras.object_utils import AddObjectHelper
from bpy_extras import object_utils
from bpy_extras.io_utils import ImportHelper
from bpy.props import *
from bpy.types import Operator


class ImportSomeData(Operator, ImportHelper):
  bl_idname = "import_mqo.some_data"
  bl_label = "Import MQO Data"

  filename_ext = ".mqo"

  filter_glob: StringProperty(
    default="*.mqo",
    options={'HIDDEN'},
    maxlen=255,
  )

  scale_setting: FloatProperty(
    name="Scale",
    description="Scale",
    default=0.01,
		min=0.01
  )

  def execute(self, context):
    return {'FINISHED'}

def menu_func_import(self, context):
  self.layout.operator(
    ImportSomeData.bl_idname, text="Metasequoia Importer (.mqo)")


def register():
  bpy.utils.register_class(ImportSomeData)
  bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
  bpy.utils.unregister_class(ImportSomeData)
  bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
  register()

  bpy.ops.import_mqo.some_data('INVOKE_DEFAULT')

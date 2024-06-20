#スクリプトを実行したら、ファイルダイアログでMQOファイルを保存する。

import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty,FloatProperty
from bpy.types import Operator
import os
import sys
script_file = os.path.basename(__file__)
script_path = bpy.data.texts[script_file].filepath
script_dir = os.path.dirname(script_path)
sys.path += [script_dir]
from savemqo import SaveMQO
import delmaterial

class ExportSomeData(Operator, ExportHelper):
  bl_idname = "save_mqo.some_data"
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
    delmaterial.delete()
    return model.save_mqo(
      context, self.filepath, self.scale_setting)

def menu_func_export(self, context):
  self.layout.operator(
    ExportSomeData.bl_idname, text="Metasequoia (.mqo)")

def register():
  bpy.utils.register_class(ExportSomeData)
  bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
  bpy.utils.unregister_class(ExportSomeData)
  bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
  register()

  bpy.ops.save_mqo.some_data('INVOKE_DEFAULT')

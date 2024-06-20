#スクリプトを実行したら、ファイルダイアログでMQOファイルを読み込む。

import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, FloatProperty
from bpy.types import Operator
import os
import sys
script_file = os.path.basename(__file__)
script_path = bpy.data.texts[script_file].filepath
script_dir = os.path.dirname(script_path)
sys.path += [script_dir]
from loadmqo import LoadMQO
import delmaterial


class ImportSomeData(Operator, ImportHelper):
    bl_idname = "load_mqo.some_data"
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
        model = LoadMQO()
        result = model.load_mqo(
            context, self.filepath, self.scale_setting)
        delmaterial.delete()
        return result

def menu_func_import(self, context):
    self.layout.operator(
        ImportSomeData.bl_idname, text="Metasequoia (.mqo)")


def register():
    bpy.utils.register_class(ImportSomeData)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportSomeData)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    bpy.ops.load_mqo.some_data('INVOKE_DEFAULT')

#オブジェクトを選択し、「Edit Mode」で1つ以上の頂点を選択
#スクリプトを実行したら、「3Dビュー」→「サイドバー」→「Set X」をクリック
#「set_x」を左右ドラッグし、「execute」ボタンをクリック

import bpy
from bpy.props import *
import bmesh

class SET_X_PANEL_PT_ui(bpy.types.Panel):
  bl_label = "Set X Panel"
  bl_idname = "SET_X_PT_UI"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "Set X"

  def draw(self, context):
    layout = self.layout
    obj = context.object
    props = context.scene.myfloatproperty
    row = layout.row()
    row.prop(props, "set_x")

class MyFloatPropertyGroup(bpy.types.PropertyGroup):
  set_x : FloatProperty(
    name="set_x",
    description="Set vertex x pos",
    default=0,
  )


regist_classes = (
  SET_X_PANEL_PT_ui,
  MyFloatPropertyGroup
)

def register():
  for regist_cls in regist_classes:
    bpy.utils.register_class(regist_cls)
  bpy.types.Scene.myfloatproperty = \
    PointerProperty(type=MyFloatPropertyGroup)

def unregister():
  for regist_cls in regist_classes:
    bpy.utils.unregister_class(regist_cls)
  del bpy.types.Scene.myfloatproperty

if __name__ == "__main__":
  register()

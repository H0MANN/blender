#複数のメッシュオブジェクトが3Dビューにあるか確認
#「Object Mode」で1個オブジェクトをクリックしてアクティブに
#このスクリプトを実行したらオブジェクトのリストから1つを選択
#選択したオブジェクトの頂点の位置にアクティブなオブジェクトが複製される

import bpy
from bpy.props import EnumProperty


class SearchEnumOperator(bpy.types.Operator):
  bl_idname = "object.search_enum_operator"
  bl_label = "Search Enum Operator"
  bl_property = "dst_search"
  bl_options = {'REGISTER', 'UNDO'}

  model = []
  for o in bpy.data.objects:
    if o.type == "MESH":
      model.append((str(o.name),str(o.data.name),""))
  dst_search: EnumProperty(
    name="My Search",
    items=model,
  )

  def execute(self, context):
    return {'FINISHED'}

  def invoke(self, context, event):
    context.window_manager.invoke_search_popup(self)
    return {'RUNNING_MODAL'}


bpy.utils.register_class(SearchEnumOperator)

# test call
bpy.ops.object.search_enum_operator('INVOKE_DEFAULT')
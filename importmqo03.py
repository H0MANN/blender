import bpy
import bmesh
from bpy_extras.object_utils import AddObjectHelper
from bpy_extras import object_utils
from bpy_extras.io_utils import ImportHelper
from bpy.props import *
from bpy.types import Operator
import os

class LoadMQO():
  
  def __init__(self):
    for item in bpy.data.meshes:
      bpy.data.meshes.remove(item)
    for item in bpy.data.materials:
      bpy.data.materials.remove(item)
    for item in bpy.data.armatures:
      bpy.data.armatures.remove(item)

  def load_mqo(self,context,filepath,scale_setting):
    dir = os.path.split(filepath)[0]+"/"

    with open(filepath) as file:
      lines = file.read()

    lines = lines.split('\n')
    for i in range(len(lines)):
      line = lines[i].split(' ')
      if line[0] == "Material":
        pass
      elif line[0] == "Object":
        name = line[1].replace('"','')
      elif line[0] == "\tvertex":
        verts = self.add_vertex(lines,i,scale_setting)
      elif line[0] == "\tface":
        faces = self.add_face(lines,i)
        mesh = bpy.data.meshes.new(name)
        object = bpy.data.objects.new(name, mesh)
        bpy.context.collection.objects.link(object)
        mesh.from_pydata(verts,[],faces[0])

    return {'FINISHED'}

  def add_vertex(self,lines,index,scale_setting):
    verts = []
    verts.append((0,0,1))
    verts.append((0,-1,-1))
    verts.append((0,1,-1))

    return verts

  def add_face(self,lines,index):
    faces = []
    m_indices = []
    uvs = []
    m_indices.append(0)
    faces.append((2,1,0))
    uvs.append((0,0))
    uvs.append((1,0))
    uvs.append((1,1))

    return faces,m_indices,uvs

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
    model = LoadMQO()
    return model.load_mqo(
      context, self.filepath, self.scale_setting)

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

#「load.py」から呼ばれるモジュール

import bpy
import bmesh
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
        materials = self.add_material(lines,i,dir)
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
        for p in mesh.polygons:
          p.use_smooth = True
        me = object.data
        me.uv_layers.new(name=name)
        for i in range(len(faces[2])):
          me.uv_layers[-1].data[i].uv = faces[2][i]
        mesh.update(calc_edges=True)
        bpy.context.view_layer.objects.active = object
        bpy.ops.object.mode_set(mode = 'EDIT')
        mesh = bmesh.from_edit_mesh(object.data)
        mesh.select_mode = {'FACE'}
        mesh.faces.ensure_lookup_table()
        for m in materials:
          object.data.materials.append(m)
        for i in range(len(faces[0])):
          mesh.faces[i].material_index = faces[1][i]
    bpy.ops.object.mode_set(mode = 'OBJECT')

    return {'FINISHED'}

  def add_material(self,lines,index,dir):
    materials = []
    line = lines[index].split(' ')
    num = int(line[1])
    for i in range(index+1,num+index+1):
      line = lines[i].split(' ')
      name = line[0].replace('\t','').replace('"','')
      index = 1
      if 'shader' in line[1]:
        index += 1
      if 'vcol' in line[2]:
        index += 1
      if 'dbls' in line[2]:
        index += 1
      if 'dbls' in line[3]:
        index += 1
      one = float(line[index].replace('col(',''))
      two = float(line[index+1])
      three = float(line[index+2])
      four = float(line[index+3].replace(')',''))
      dif = float(
        line[index+4].replace('dif(','').replace(')',''))
      amb = float(
        line[index+5].replace('amb(','').replace(')',''))
      emi = float(
        line[index+6].replace('emi(','').replace(')',''))
      spc = float(
        line[index+7].replace('spc(','').replace(')',''))
      power = float(
        line[index+8].replace('power(','').replace(')',''))
      tex = None
      if len(line) == index+10:
        tex = line[index+9].replace('tex("','').replace('")','')
      materials.append(
        self.make_material(name,(one,two,three,four),tex,dir))
    return materials

  def make_material(self,name,col,tex,dir):
    ma = bpy.data.materials.new(name)
    ma.use_nodes = True
    bsdf = ma.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = col
    bsdf.inputs[4].default_value = 1.0
    bsdf.inputs[7].default_value = 0.8
    if tex != None:
      img = ma.node_tree.nodes.new('ShaderNodeTexImage')
      if tex.lower().startswith("c:\\") or tex.startswith("/"):
        img.image = bpy.data.images.load(tex)
      else:
        img.image = bpy.data.images.load(dir+tex)
      ma.node_tree.links.new(
        bsdf.inputs['Base Color'],img.outputs['Color'])
    ma.diffuse_color = col
    return ma

  def add_vertex(self,lines,index,scale_setting):
    verts = []
    line = lines[index].split(' ')
    num = int(line[1])
    for i in range(index+1,num+index+1):
      line = lines[i].split(' ')
      x = scale_setting*float(line[0])
      y = -scale_setting*float(line[2])
      z = scale_setting*float(line[1])
      verts.append((x,y,z))

    return verts

  def add_face(self,lines,index):
    faces = []
    m_indices = []
    uvs = []
    line = lines[index].split(' ')
    num = int(line[1])
    for i in range(index+1,num+index+1):
      line = lines[i].split(' ')
      if line[0] == "\t\t3":
        one   = int(line[1].replace('V(',''))
        two   = int(line[2])
        three = int(line[3].replace(')',''))
        material = line[4].replace('M(','')
        m_indices.append(int(material.replace(')','')))
        u1 = v1 = u2 = v2 = u3 = v3 = 0
        if len(line) >= 6:
          u1 = float(line[5].replace('UV(',''))
          v1 = float(line[6])
          u2 = float(line[7])
          v2 = float(line[8])
          u3 = float(line[9])
          v3 = float(line[10].replace(')',''))
        faces.append((three,two,one))
        uvs.append((u3,1-v3))
        uvs.append((u2,1-v2))
        uvs.append((u1,1-v1))
      elif line[0] == "\t\t4":
        one = int(line[1].replace('V(',''))
        two = int(line[2])
        three = int(line[3])
        four = int(line[4].replace(')',''))
        material = line[5].replace('M(','')
        m_indices.append(int(material.replace(')','')))
        u1 = v1 = u2 = v2 = u3 = v3 = u4 = v4 = 0
        if len(line) >= 7:
          u1 = float(line[6].replace('UV(',''))
          v1 = float(line[7])
          u2 = float(line[8])
          v2 = float(line[9])
          u3 = float(line[10])
          v3 = float(line[11])
          u4 = float(line[12])
          v4 = float(line[13].replace(')',''))
        faces.append((four,three,two,one))
        uvs.append((u4,1-v4))
        uvs.append((u3,1-v3))
        uvs.append((u2,1-v2))
        uvs.append((u1,1-v1))

    return faces,m_indices,uvs

# Imports
import graphviz
import importlib
import inspect
import pydclass.class_library as library
import os

def render(format, module):
    file_path = os.path.realpath(__file__)
    module = importlib.import_module(module, package=file_path)
    print(module)

    dot = graphviz.Digraph('structs', filename='structs_revisited.gv',
                     node_attr={'shape': 'record'})

    template_node = """<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
    <TR>
    <TD fontcolor=\"red\"><font color=\"red\" style=\"Arial\">{title}</font></TD></TR>
    <TR><TD></TD></TR>
    {attr_liststr}
    {attrib_template}
  
    </TABLE>>"""

    meth_template = "<TR><TD> Meth: {meth}</TD></TR>"
    attr_template = "<TR><TD>Attr: {attr}</TD></TR>"

    members = inspect.getmembers(module)

    class_list = []
    for m in members:
        if inspect.isclass(m[1]):
            class_list.append(m[1])

    attributes_h_list = []
    methods_h_list = []
    final_dict = []
    meth = []

    for c in class_list:
        ci = library.class_infos(c, module, methods_h_list, attributes_h_list)
        meth_list = ci.class_methods()
        for m in meth_list:
            meth.append(m.__name__)
        attr_list = ci.class_atributes(meth)
        parents_list = ci.class_parents()

        dictionary = {"name": c.__name__, "methods": meth_list, "attributes": attr_list, "parents": parents_list}
        attributes_h_list += ci.get_attributes_list()
        methods_h_list += ci.get_methods_list()
        final_dict.append(dictionary)



    for c in final_dict:
        attrib = []
        meth = []
        parents_attr_list = []


        for m in c['methods']:
            print(m.__name__)
            meth.append(meth_template.format(meth=m.__name__))
        meth = "".join(meth)
        for a in c['attributes']:

            attrib.append(attr_template.format(attr=a))
        attrib = "".join(attrib)

        dot.node(c['name'], label=template_node.format(title=c['name'], attr_liststr=meth, attrib_template=attrib))

    for c in final_dict:
        for p in c['parents']:
            dot.edge(p.__name__, c['name'])



    dot.render(os.path.dirname(os.path.realpath(__file__))+"/graph", format=format).replace('\\', '/')

def get_svg_datas(module, format):
    render(format, module)
    render_datas = open(os.path.dirname(os.path.realpath(__file__))+'/graph.svg', 'r').read()
    print(render_datas)
    return render_datas 
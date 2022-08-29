# Imports
import graphviz
import importlib
import inspect
import pydclass.class_library as library
import os
import yaml

def render(format):
    try:
        file_path = os.path.realpath(__file__)

        dot = graphviz.Digraph('structs', filename='structs_revisited.gv',
                     node_attr={'shape': 'record'})

        template_node = """<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
        <TR>
        <TD ALIGN="CENTER" CELLPADDING="4" CELLSPACING="5" BGCOLOR="blue" COLSPAN="3"><font color=\"white\">{title}</font></TD></TR>
        <TR><TD>    </TD></TR>
        {meth_list}
        {attr_list}
  
        </TABLE>>"""

        file_list = os.listdir('.')
        try:
            with open(os.getcwd()+'/pydclass-config.yaml') as file: 
                config = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print('[!] No configuration file found; Using the default configuration.')
            config = {"attributs_color": "blue", "methods_color": "orange", 'text_color': 'white', 'attributs_name': 'Attributs', 'methods_name': 'Methods:'}
        try:
            meth_template = "<TR><TD ALIGN='left' BGCOLOR='"+config['methods_color']+"' CELLPADDING='5'><font color='"+config['text_color']+"'>"+config['methods_name']+": </font></TD><TD>{meth}</TD></TR>"
            attr_template = "<TR><TD ALIGN='left' BGCOLOR='"+config['attributs_color']+"' CELLPADDING='5'><font color='"+config['text_color']+"'>"+config['attributs_name']+": </font></TD><TD>{attr}</TD></TR>"
        except KeyError:
            print('[!] The program cannot read the pydclass-config.yaml file; There is some information missing. Automatic switch to default configuration.')
            config = {"attributs_color": "blue", "methods_color": "orange", 'text_color': 'white', 'attributs_name': 'Attributs', 'methods_name': 'Methods:'}
            meth_template = "<TR><TD ALIGN='left' BGCOLOR='"+config['methods_color']+"' CELLPADDING='5'><font color='"+config['text_color']+"'>"+config['methods_name']+": </font></TD><TD>{meth}</TD></TR>"
            attr_template = "<TR><TD ALIGN='left' BGCOLOR='"+config['attributs_color']+"' CELLPADDING='5'><font color='"+config['text_color']+"'>"+config['attributs_name']+": </font></TD><TD>{attr}</TD></TR>"
        module_list = []
        for f in file_list:
            if f.split('.')[-1] == "py":
                module_list.append(f.split('.')[0])

        members = []

        for m in module_list:
            members += inspect.getmembers(importlib.import_module(m))

        class_list = []
        for m in members:
            if inspect.isclass(m[1]):
                class_list.append(m[1])

        attributes_h_list = []
        methods_h_list = []
        final_dict = []
        meth = []

        for c in class_list:
            ci = library.class_infos(c, importlib.import_module(module_list[0]), methods_h_list, attributes_h_list)
            meth_list = ci.class_methods()
            for m in meth_list:
                meth.append(m.__name__)
            attr_list = ci.class_atributes(meth)
            parents_list = ci.class_parents()

            dictionary = {"class": c, "name": c.__name__, "methods": meth_list, "attributes": attr_list, "parents": parents_list}
            attributes_h_list += ci.get_attributes_list()
            methods_h_list += ci.get_methods_list()
            final_dict.append(dictionary)


        for c in final_dict:
            attrib = []
            meth = []
            parents_attr_list = []


            for m in c['methods']:
                
                meth.append(meth_template.format(meth=m.__name__))
            meth = "".join(meth)
            for a in c['attributes']:

                attrib.append(attr_template.format(attr=a))
            attrib = "".join(attrib)
            dot.node(str(c['class']), label=template_node.format(title=inspect.getmodule(c['class']).__name__+" - "+c['name'], meth_list=meth, attr_list=attrib), fontname="Courier New", fontsize="10px")

        for c in final_dict:
            for p in c['parents']:
                dot.edge(str(p), str(c['class']), color="blue")



        dot.render(os.path.dirname(os.path.realpath(__file__))+"/graph", format=format).replace('\\', '/')
    except BaseException as err:
        dot.node('Error occured', label="<TR><TD fill='red'>An error occurred during the build.</TR></TD><TR><TD>You can make a request on GitHub clearly stating this: "+str(err)+".</TD></TR>")
        dot.render(os.path.dirname(os.path.realpath(__file__))+"/graph", format=format)
def get_svg_datas(format):
    render(format)
    render_datas = open(os.path.dirname(os.path.realpath(__file__))+'/graph.svg', 'r').read()
    return render_datas 

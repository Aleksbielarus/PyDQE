# import xml.etree.ElementTree as ElementTree
from xml.etree import ElementTree as ElementTree


tree = ElementTree.parse('xml_file.xml')
root = tree.getroot()


def xml_to_list_of_dicts(root, note):
    note_list = []
    for item in root.findall(note):
        note_dict = {}
        note_item = item.attrib
        note_dict.update(note_item)
        for child in item:
            note_dict[child.tag] = child.text
        note_list.append(note_dict)
    return note_list

print(xml_to_list_of_dicts(root, './note'))
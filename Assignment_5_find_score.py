import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    
    count = 0 + len(node.attrib)
    for nod in node:
        if etree.ElementTree(etree.fromstring(etree.tostring(nod))):
            child_node = etree.ElementTree(etree.fromstring(etree.tostring(nod)))
            children = child_node.getroot()
            count += len(children.attrib)
            for child in children:
                count += len(child.attrib)
    return count
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
import xml.etree.ElementTree as ET

# Parse an XML file and get the root element
tree = ET.parse('data.xml')
root = tree.getroot()

# Print the root element
print(root.tag)

# Access specific data from the XML tree
for child in root:
    print(child.tag, child.attrib)

# Create a new XML tree and write it to a file
new_root = ET.Element('data')
new_child = ET.SubElement(new_root, 'name')
new_child.text = 'Bob'

ET.ElementTree(new_root).write('new_data.xml')

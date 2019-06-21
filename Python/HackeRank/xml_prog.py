import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()



def func(ele):
	if len(ele) != 0:
		pass


depth = func(ele)

for child in root:
	print(child.tag, "  ", child.attrib)
	if len(child) != 0:
		for chill in child:
			print("\t",chill.tag)
			print("\t",len(chill))
			if len(chill) != 0:
				for bill in chill:
					print("\t\t",bill.tag)


"""max_depth = 0

def func(root):
	global max_depth"""
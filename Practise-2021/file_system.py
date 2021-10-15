"""
- Aim is to develop an in-memory file system
- Can be visualized as a linux filesystem
- Key value store with path being the key and value being the file
- So if a path doesn't exist during write operation  (mkdir or write) then throw exception, 
- if the key doesn't exist then throw exception
- if the path exists and it's a file during mkdir then throw exception

mkdir(path: String)
write(path: String, value: String)
read(filepath:String): String

Trie: 
   Node: {
	  value: curDirName
	  children: Map<Key,Node>
   }
 Root Node: value: "/"
 Mkdir: Iterate till the last but path to check whether the path exists if so create a new path

HashMap:
 - Repeating the diretory structure
 - 
 - Is not consistent with the real world view, so not so easy to visualize

 /a/b/c
"""

DIR_DELIMETER = "/"

class Node:
	value = None
	children = {}
	isDir = False
	contents = None

	def __init__(self, value, children, isDir, contents=None):
		self.value = value
		self.isDir = isDir
		self.children = children
		self.contents = contents


class FileSystem:
	root_node = Node("/",{}, True)

	def mkdir(self, full_path): 
		parent_path, new_dir_name = self.get_parent_path_and_rem(full_path)
		parent_node = self.is_path_exists(parent_path, self.root_node)
		if (parent_node == None):
			raise Exception("Parent node doesn't exist")
		if new_dir_name in parent_node.children:
			if not parent_node.children[new_dir_name].isDir:
				raise Exception("Already directory exists and it's a file")
		else:
			parent_node.children[new_dir_name] = Node(new_dir_name, {}, True)
		return parent_node.children[new_dir_name]

	def write(self, full_path, contents):
		parent_path, file_name = self.get_parent_path_and_rem(full_path)
		parent_node = self.is_path_exists(parent_path, self.root_node)
		if (parent_node == None):
			raise Exception("Parent node doesn't exist")
		if file_name in parent_node.children:
			raise Exception("FileName already exists")
		parent_node.children[file_name] = Node(file_name,{}, False, contents)
		return parent_node.children[file_name]

	def read(self, full_path):
		parent_path, file_name = self.get_parent_path_and_rem(full_path)
		parent_node = self.is_path_exists(parent_path, self.root_node)
		if (parent_node == None):
			raise Exception("Parent node doesn't exist")
		if file_name not in parent_node.children:
			raise Exception("FileName doesn't exists")
		return parent_node.children[file_name].contents

	def get_parent_path_and_rem(self, full_path):
		paths = full_path.split(DIR_DELIMETER)
		parent_path = DIR_DELIMETER.join(paths[:-1])
		new_dir_name = paths[-1]
		return (parent_path, new_dir_name)

	def is_path_exists(self, path, root_node):
		if (len(path) <= 0):
			return root_node
		paths = path.split("/")
		if(paths[0] in root_node.children):
			return self.is_path_exists(DIR_DELIMETER.join(paths[1:]),root_node.children[paths[0]])
		else:
			return None



file_system = FileSystem()
file_system.mkdir("a")
file_system.mkdir("a/b")
try:
	file_system.mkdir("a/b/c/d")
except:
	print("pass")
file_system.write("a/b/c.txt", "c contents")
print(file_system.read("a/b/c.txt"))

try:
	file_system.write("a/b/d/c.txt", "c contents")
except:
	print("pass")
try:
	file_system.write("a/b", "c contents")
except:
	print("pass")

try:
	file_system.read("a/b/d/c.txt", "c contents")
except:
	print("pass")

try:
	file_system.read("a/b/d.txt", "c contents")
except:
	print("pass")

try:
	file_system.write("a/b/c.txt", "c contents")
except:
	print("pass")
# https://drive.google.com/file/d/1yHjk00nAWeT1YCeGGeOk__C8SA899Eqf/view



class TrieNode(object):
    value = None
    key = None
    children = {}
    watchers = []
    def __init__(self, key, value=None, children={}, watchers=[]):
        self.key = key
        self.value = value
        self.children = children
        self.watchers = watchers
    def __str__(self):
        return "Key={},value={}".format(self.key, self.value)
    def __repr__(self):
        return self.__str__()

class Zookeeper(object):
    def __init__(self):
        self.ROOT_KEY = "/"
        self.root = TrieNode(self.ROOT_KEY, None, {},[])
    def watch(self, path, watcher):
        path = path[1:]
        paths = path.split(self.ROOT_KEY)
        parent = self.findParent(self.root, paths)
        if not parent:
            raise Exception("Parent Not found " + path)
        parent.watchers.append(watcher)
        
    def create(self, path, value):
        # Last nod e won't exist
        """
        /a/b/c
        """
        path = path[1:]
        paths = path.split(self.ROOT_KEY)
        parent = self.findParent(self.root, paths[:-1])
        print "The Parent", parent
        if not parent:
            raise Exception("Parent Not found " + path)
        newNode = TrieNode(paths[-1], value, {},[])
        parent.children[paths[-1]] = newNode
        self.notify(self.ROOT_KEY.join(paths), paths, value)
    
    def notify(self, fullPath, paths, value):  
        if len(paths) <= 0:
            return      
        curPath = self.findParent(self.root, paths)    
        for watcher in curPath.watchers:
            watcher(fullPath, value)
        self.notify(fullPath, paths[:-1], value)
            
    def read(self, path):
        path = path[1:]
        paths = path.split(self.ROOT_KEY)
        parent = self.findParent(self.root, paths)
        if not parent:
            raise Exception("Parent Not found " + path)
        return parent.value
    def update(self, path, value):
        path = path[1:]
        paths = path.split(self.ROOT_KEY)
        parent = self.findParent(self.root, paths)
        if not parent:
            raise Exception("Parent Not found " + path)
        parent.value = value
        self.notify(self.ROOT_KEY.join(paths), paths, value)

        
    def findParent(self, root, path):
        if len(path) <= 0:
            return root
        # paths = path.split(self.ROOT_KEY)
        if path[0] in root.children:
            return self.findParent(root.children[path[0]], path[1:])
        else:
            return None
        
def callbackFn(path, value):
    print("In callback:", path, value)
            
if __name__ == "__main__":
    zookeeper = Zookeeper()
    zookeeper.create("/a", "10")
    zookeeper.create("/a/b", "20")
    print(zookeeper.read("/a") == "10")
    print(zookeeper.read("/a/b") == "20")
    try:
        zookeeper.create("/a/b/c/d", 30)
    except Exception:
        print "Ok create working"
    try:
        zookeeper.read("/a/b/c/d")
    except Exception:
        print "Ok read working"
    zookeeper.update("/a/b", "40")
    print(zookeeper.read("/a/b") == "40")
    try:
        zookeeper.update("/a/b/c/d","40")
    except Exception:
        print "Ok update working"
        
    zookeeper.watch("/a", callbackFn) # doesn't print anything
    zookeeper.update("/a", "30") # print
    zookeeper.update("/a/b", "40") # also print
    zookeeper.create("/a/b/c", "50") # also prints
    
    
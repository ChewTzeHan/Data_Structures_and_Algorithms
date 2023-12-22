## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        
        
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for i in path:
            if i not in current_node.children:
                current_node.children[i] = RouteTrieNode(None)
            
            current_node = current_node.children[i]
        
        current_node.handler = handler

    def find(self, path, error_msg):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        if len(path) == 0:
            return self.root.handler
        
        current_node = self.root
        
        for i in path:
            if i not in current_node.children:
                return error_msg
            else:
                current_node = current_node.children[i] 
        
        if current_node.handler == None:
            return error_msg
        else:
            return current_node.handler


## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler):
        # Insert the node as before
        self.children[path] = RouteTrie(handler)
        

## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, error_msg = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler)
        self.error_msg = error_msg
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if type(path) != str:
            return
        
        split_path = self.split_path(path)
        
        current_node = self.root
        
        current_node.insert(split_path, handler)
        
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        split_path = self.split_path(path)
        
        current_node = self.root
        
        handler = current_node.find(split_path, self.error_msg)
        
        return handler
        
    
    def split_path(self, full_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if full_path == '/':
            return []
        path = full_path.split('/')
        
        for i in path:
            if i == '':
                path.remove('')
                
        return path
        
   
## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


print('----------------')
#TEST CASE 1

router_1 = Router("root handler", "not found handler")
router_1.add_handler("/home/Terakomari/Sakuna/Villhaze/Karla/Nelia", "Nelia handler")
router_1.add_handler("/home/Terakomari/Sakuna/Villhaze", "Villhaze handler")
router_1.add_handler("/home/Terakomari", "Terakomari handler")

print(router_1.lookup("/"))
print(router_1.lookup("/home/Terakomari/Sakuna/Villhaze/Karla/Nelia"))
print(router_1.lookup("/home/Terakomari/Sakuna/Villhaze"))
print(router_1.lookup("/home/Terakomari/Sakuna"))
print(router_1.lookup("/home/Terakomari/"))

'''
Expected output:
    root handler
    Nelia handler
    Villhaze handler
    not found handler
    Terakomari handler
'''
print('----------------')
#TEST CASE 2 - NULL VALUES

router_2 = Router("root handler", None)
router_2.add_handler("/CLaire/Rei/Manaria/Misha", "Misha handler")
router_2.add_handler("/CLaire/Rei", None)
router_2.add_handler(None, "Manaria handler")

print(router_2.lookup("/"))
print(router_2.lookup("/CLaire/Rei/Manaria"))
print(router_2.lookup("/CLaire/Rei"))
print(router_2.lookup("/CLaire/Rei/Manaria/Misha"))


'''
Expected output:
    root handler
    None
    None
    Misha handler
'''

print('----------------')
#TEST CASE 3 - VERY LARGE PATHS

router_3 = Router("root handler", "not found handler")
router_3.add_handler("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis/Jade/Amber/Fogado/Timerra/Seadall/Merrin/Panette/Pandreo/Bunet/Veyle/Yunaka", "Yunaka handler")
router_3.add_handler("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis/Jade/Amber/Fogado/Timerra", 'Timerra handler')
router_3.add_handler("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis", "Lapis handler")

print(router_3.lookup("/"))
print(router_3.lookup("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis/Jade/Amber/Fogado/Timerra/Seadall/Merrin/Panette/Pandreo/Bunet/Veyle/Yunaka"))
print(router_3.lookup("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis/Jade/Amber/Fogado/Timerra/Seadall/Merrin"))
print(router_3.lookup("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis/Jade/Amber/Fogado/Timerra/"))
print(router_3.lookup("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/"))
print(router_3.lookup("/Ivy/Hortensia/Rosado/Goldmary/Kagetsu/Zelkov/Celine/Alfred/Etie/Louis/Chloe/Boucheron/Diamant/Alcryst/Citrinne/Lapis"))

'''
Expected output:
    root handler
    Yunaka handler
    not found handler
    Timerra handler
    not found handler
    Lapis handler
'''
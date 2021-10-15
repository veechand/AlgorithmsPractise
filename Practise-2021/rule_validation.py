"""
You have a table :
Rule1 Rule2 Rule3 Value
A1 B2 C3 40
A1 B1 C1 20
A2 B2 C2 10
A1 B1 C1 40
* B1 * 20
A5 B2 * 10

Now if I have a condition A1 && B2 && C3 i will get output as 40.
If I input A1 && B1 && C1 I will get two results 40 and 20 here there the rule is ambiguous.
"-" in table means any rule, 5th row matches with any row with B1 as rule2, so there is also ambiguity in result.

- Always can we assume there are only 3 rules - Yes
- There can be more than one rule but the values are same does this mean the rules are ambiguous - None
- Do we say the rule is ambigous when parsing the table or when input is given - While parsing the table

create a MAP:
 with key as rule concatenated "A1-B2-C3"
 When ever adding a new rule we can check whether such rule exists in the map
 Now when we parse something like *
 * - B1 - * - O(N) operation. We need to find index
 * - * - C3
 A1 B1 C3

 Trie

Node:
  name
  value
  children={}

Before adding a node, will check if there's any children of the current node
than matches with the to be added node value
 if True:
 	  is_ambiguous(node, rule_from_node)
 if False:
 	  add_current_node as child
 	  do_same(newly_added_node, rule.remove(current_rule)
      
 root = <>
 check_ambiguous(rules):
   for rule in rules:
   	   result = check_is_this_rule_ambiguous(root, rule)
   	   if result:
   	   	  return result
 check_is_this_rule_ambiguous(root, rule):
      splitted_rule = rule.split(" ")
      if len(splitted_rule) == 1:
      	if root.value is not None and root.value != int(rule):
      	   return True
      	else:
      	 return False
      cur_node, remaining = splitted_rule[0], splitted_rule[1:]
      //cur_node can be the last rule
      if cur_node in root.children || "*" in root.children:
      	#if (len(Remaining) == 1):
      	#	root.children[cur_node].value != int(Remaining)
      	#	return True
        result = check_is_this_rule_ambiguous(root.children[cur_node], remaining) if cur_node in root.children else False
        result1 = check_is_this_rule_ambiguous(root.children["*"], remaining) if * in root.children and cur_node != "*" else False
      	if result || result1:
      		return True
      else: //cur_node not in root.children:
      	node = Node(cur_node)
      	root.children[cur_node] = node
      	return check_is_this_rule_ambiguous(node, remaining)
"""
class TrieNode(object):
	name = None
	value = None
	children = {}
	def __init__(self, name, value=None, children={}):
		self.name = name
		self.value = value
		self.children = children

class Solution(object):
	def __init__(self):
		self.root = TrieNode("R", value=None, children={})
		self.ANY = "*"
	def check_ambiguous(self, rules):
		for rule in rules:
			result = self.check_is_the_rule_ambiguous(self.root, rule)
			if result:
				print("The rule is ambiguous ",rule)

	def check_is_the_rule_ambiguous(self, root, rule):
		# Not expecting rule to None anytime
		splitted_rule = rule.split(" ")
		if len(splitted_rule) == 1:
			if root.value is not None and root.value != int(splitted_rule[0]):
				return True
			else:
				root.value = int(x=splitted_rule[0])
				return False
		cur_node, remaining = splitted_rule[0], " ".join(splitted_rule[1:])
		if cur_node == self.ANY:
			results = []
			for key, child in root.children.items():
				results.append(self.check_is_the_rule_ambiguous(child, remaining))
			if any(results):
				return True
		if cur_node in root.children or self.ANY in root.children:
			result1 = self.check_is_the_rule_ambiguous(root.children[cur_node], remaining) if cur_node in root.children else False
			result2 = self.check_is_the_rule_ambiguous(root.children[self.ANY], remaining) if self.ANY in root.children and self.ANY != cur_node else False
			return result1 or result2
		else:
			node = TrieNode(cur_node, value=None, children={})
			root.children[cur_node] = node
			return self.check_is_the_rule_ambiguous(node, remaining)

if __name__ == "__main__":
	solution = Solution()
	rules = [
		"* B2 C1 40",
		"A1 * C1 10",
		"A1 B1 C1 20",
		"* B2 C2 20",
		"A2 B2 C2 10",
	]
	solution.check_ambiguous(rules)

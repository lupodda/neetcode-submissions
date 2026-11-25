
class Dsu:
    def __init__(self,):
        self.parent = {} #node to representative
        self.node_to_name={}
        
    def find(self, node):
        if node!= self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self, node1,node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1!=root2:
            self.parent[root1] = root2

from collections import defaultdict       
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        dsu = Dsu()
        
        for name, *emails in accounts:
            for email in emails:
                dsu.parent[email]=email
                dsu.node_to_name[email] = name
                
                
        for account in accounts:
            first=account[1]
            for email in account[2:]:
                dsu.union(first, email)
                
        groups = defaultdict(list)
        for email in dsu.parent:
            root=dsu.find(email)
            groups[root].append(email)
            
        res=[]
        for emails in groups.values():
            name=dsu.node_to_name[emails[0]]
            res.append([name]+sorted(emails))
        return res
            
        
        
                
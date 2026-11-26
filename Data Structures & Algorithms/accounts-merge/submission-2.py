class Dsu:
    def __init__(self,):
        self.parent = {} #emial: representative
        self.email_to_name = {}

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            self.parent[root2] = root1

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = Dsu()

        # initialization -> each email with itself as representative
        for name, *emails in accounts:
            for email in emails:
                dsu.parent[email] = email
                dsu.email_to_name[email] = name

        #union of the representative for each email
        for _, *emails in accounts:
            first = emails[0]
            for email in emails[1:]:
                dsu.union(first, email)

        #grouping emails with the same representative
        groups = defaultdict(list)
        for email in dsu.parent:
            root = dsu.find(email)
            groups[root].append(email)

        #create the output sorting the emails
        res = []
        for emails in groups.values():
            name = dsu.email_to_name[emails[0]]
            merged_account = [name]+sorted(emails)
            res.append(merged_account)
            
        return res



        

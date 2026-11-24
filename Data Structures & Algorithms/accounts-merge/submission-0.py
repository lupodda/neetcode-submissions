
from collections import defaultdict
class Dsu:
    def __init__(self):
        self.parents = {}#email: representative
        self.email_to_name = {}        

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        self.parents[root1] = root2           


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # we use dsu to find the connected components:
        # a connected component is an account having a common email
        # if two accounts are connected, we merge them by putting the emils in the same list
        # at the end for all the new connected components we sort the email values
        dsu = Dsu()

        #initialization
        for name, *emails in accounts:
            for email in emails:
                dsu.parents[email] = email
                dsu.email_to_name[email] = name

        # union
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                dsu.union(first_email, email)

        #group emails with the same representative
        group = defaultdict(list)
        for email in dsu.parents:
            root = dsu.find(email)
            group[root].append(email)
        
        #create the output
        res = []
        for emails in group.values():
            name = dsu.email_to_name[emails[0]]
            account = [name]+sorted(emails)
            res.append(account)

        return res

        

        

        


        

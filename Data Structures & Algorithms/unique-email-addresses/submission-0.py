class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        uniqueEmails = set()

        for email in emails:
            domain = email[email.find("@"):]
            loname = email[:email.find("+")]
            loname = loname.replace(".", "")
            uniqueEmails.add(loname + domain)

        return len(uniqueEmails)
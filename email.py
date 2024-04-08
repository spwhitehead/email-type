class Email:
    def __init__(self, content: str):
        if not isinstance(content, str):
            raise TypeError("Please provide a string")

        if "@" not in content:
            raise TypeError("Doesn't have an '@' sign")

        valid_tlds: list[str] = [".com", ".edu", ".net", ".org"]
        tld = content[-4:]
        if tld not in valid_tlds:
            raise TypeError("Invalid TLD")

        # Check for domain (stuff between @ and .com
        domain_start = content.find("@") + 1
        domain = content[domain_start:-4]
        if domain =="":
            raise TypeError("Invalid domain")

        if content.find("@") == 0:
            raise TypeError("Invalid username")
            

        self.content = content

    def __str__(self) -> str:
        return self.content


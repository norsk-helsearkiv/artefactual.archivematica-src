from urllib.parse import quote

class FilterModule(object):
    def filters(self):
        return {
            "uri_quote": self.uri_quote
        }

    def uri_quote(self, value):
        return quote(str(value), safe="")

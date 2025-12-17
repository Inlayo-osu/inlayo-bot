from urllib.parse import urlencode


class URIBuilder:
    def __init__(self, base_url):
        self.base_url = base_url
        self.params = {}
    
    def add_param(self, key, value):
        if value is not None:
            self.params[key] = value
        return self
    
    def add_params(self, params_dict):
        for key, value in params_dict.items():
            self.add_param(key, value)
        return self
    
    def build(self):
        if self.params:
            return f"{self.base_url}?{urlencode(self.params)}"
        return self.base_url
    
    def __str__(self):
        return self.build()

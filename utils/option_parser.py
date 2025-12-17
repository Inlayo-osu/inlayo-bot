import shlex


class OptionParser:
    def __init__(self, text):
        self.text = text
        self.options = {}
        self._parse()
    
    def _parse(self):
        try:
            parts = shlex.split(self.text)
            i = 0
            while i < len(parts):
                if parts[i].startswith('-'):
                    key = parts[i].lstrip('-')
                    if i + 1 < len(parts) and not parts[i + 1].startswith('-'):
                        self.options[key] = parts[i + 1]
                        i += 2
                    else:
                        self.options[key] = True
                        i += 1
                else:
                    i += 1
        except:
            pass
    
    def get(self, key, default=None):
        return self.options.get(key, default)
    
    def has(self, key):
        return key in self.options

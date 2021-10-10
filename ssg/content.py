import re

from yaml import load, FullLoader


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classMethod
        def load(cls, string):
            _, fm, content = clas.__regex.split(string, 2)
            metadata = load(fm, Loader=FullLoader)
            return cls(metdata, content)

from typing import Any


class ProtoAttributes:
    def __init__(self,**kwargs) -> None:# type: ignore
        self.values:dict[str,Any]=kwargs
        self.proto_name='proto'
    def __str__(self) -> str:
        values_string={i:str(self.values[i]) if not (type(self.values[i])==list) else str(self.values[i]).replace(","," ").replace("[","").replace("]","") for i in self.values}
        string:str = (self.proto_name + str(values_string)).replace("'","").replace('"',"").replace(":","")
        return string
    def proto(self,tabs:int=1)->str:
        text=str(self)
        text=text.replace(', ','\n')
        if tabs>1:
            text=text.replace("{","\n"+"  "*(tabs-1)+"{")
            text=text.replace("}","\n"+"  "*(tabs-1)+"}")
        if tabs<2:
            text=text.replace("{","{\n")
            text=text.replace("}","\n}")
        text="\n".join([("  "*tabs+i if not (( "{" in i) or ("}" in i)) else i) for i in text.splitlines()])
        return text
    def __getime__(self, name: str) -> Any:# type: ignore
        if type(name)!=str:
            return None
        if name in self.values:
            return self.values[name]
        return None
    def __setitem__(self, name: str, value: Any) -> None:
        if type(name)!=str:
            return None
        self.values[name]=value
    def __delattr__(self, name: str) -> None:
        del self.values[name]
    def define(self,world:Any,name:str)->None:
        world.define(self,name)
    def proto_from_defined(self,world:Any,name:str)->None:
        self=world.proto_from_defined(self,name)
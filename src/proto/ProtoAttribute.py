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
    """def __getattribute__(self, name: str) -> Any:# type: ignore
        if name in self.values:
            return self.values[name]
        return super().__getattribute__(self,name) # type: ignore
    def __setattr__(self, name: str, value: Any) -> None:
        self.values[name]=value"""
    def __delattr__(self, name: str) -> None:
        del self.values[name]
    def define(self,world:Any)->None:
        world.define(self)
    def proto_from_defined(self,world:Any)->None:
        ...
print(ProtoAttributes(translation=[7,3,4],controller="arm_hand").proto())
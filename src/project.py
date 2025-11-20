""""""
import os
from typing import Any
from vControllers import Session

class project:
    def __init__(self,world_name:str,dir:str|os.PathLike[str],*args:list[Any],session_type:Any=Session,**kwargs:dict[str,Any]) -> None:
        self.session_type:Any=session_type
        self.session=session_type(*args,**kwargs)
        self.world_name=world_name
        self.dir=dir
    def check_tree(self)->None:
        subfolders:list[str]=["controllers","libraries","plugins","protos","worlds"]
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        for i in subfolders:
            if not os.path.exists(os.path.join(self.dir,i)):
                os.mkdir(os.path.join(self.dir,i))
    def update_world(self):
        world_dir=os.path.join(self.dir,"worlds",self.world_name)
        if not os.path.exists(world_dir):
            os.mkdir(world_dir)
        
        
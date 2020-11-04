from typing import TypeVar, Generic, List, cast
import json
import operator
import inspect
import random
from pyjeasy.check_utils import check_dir_exists, check_file_exists, check_required_keys, check_type, check_type_from_list
import printj

T = TypeVar('T')
H = TypeVar('H')

class BasicObject(Generic[T]):
    # @abstractmethod
    def __str__(self) -> str:
        ''' To override '''
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()
    
    def __key(self) -> tuple:
        return tuple([self.__class__.__name__] + list(self.__dict__.values()))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__key() == other.__key()
        return NotImplemented

    @classmethod
    def get_constructor_params(cls) -> list:
        return [param for param in list(inspect.signature(cls.__init__).parameters.keys()) if param != 'self']

    def to_constructor_dict(self) -> dict:
        constructor_dict = {}
        for key, val in self.__dict__.items():
            if key in self.get_constructor_params():
                constructor_dict[key] = val
        return constructor_dict

    @classmethod
    def buffer(cls: T, obj) -> T:
        return obj

    def copy(self: T) -> T:
        return type(self)(**self.to_constructor_dict())

class BasicLoadableObject(BasicObject[T]):
    """
    Assumptions:
    ===========
        1. self.__dict__ matches constructor parameters perfectly.
        2. Any to_dict or to_dict_list methods of any class object in the class variable list doesn't take any parameters.
        3. No special id class variable.
        4. Non-trivial classmethods must be defined in child class
    """
    def __init__(self):
        super().__init__()

    def __key(self) -> tuple:
        return tuple([self.__class__.__name__] + list(self.to_dict()))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__key() == other.__key()
        return NotImplemented

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.to_dict()})'

    @classmethod
    def get_constructor_params(cls) -> list:
        return [param for param in list(inspect.signature(cls.__init__).parameters.keys()) if param != 'self']

    def to_dict(self: T) -> dict:
        result = {}
        for key, val in self.to_constructor_dict().items():
            if hasattr(val, 'to_dict') and callable(val.to_dict):
                result[key] = val.to_dict()
            elif hasattr(val, 'to_dict_list') and callable(val.to_dict_list):
                result[key] = val.to_dict_list()
            else:
                result[key] = val
        return result
    
    @classmethod
    def from_dict(cls: T, item_dict: dict) -> T:
        """
        Note: It is required that all class constructor parameters be of a JSON serializable datatype.
              If not, it is necessary to override this classmethod.
        """
        constructor_dict = {}
        constructor_params = cls.get_constructor_params()
        unnecessary_params = []
        for key, value in item_dict.items():
            if key in constructor_params:
                constructor_dict[key] = value
            else:
                unnecessary_params.append(key)
        if len(unnecessary_params) > 0:
            printj.yellow(f'Received unnecessary parameters in {cls.__name__}.from_dict')
            printj.yellow(f'Received: {list(item_dict.keys())}')
            printj.yellow(f'Expected: {constructor_params}')
            printj.yellow(f'Extra: {unnecessary_params}')
        check_required_keys(constructor_dict, required_keys=constructor_params)
        return cls(*constructor_dict.values())

    def save_to_path(self: T, save_path: str, overwrite: bool=False, indent=2):
        if check_file_exists(file_path=save_path, raise_error=False) and not overwrite:
            printj.red(f'File already exists at save_path: {save_path}')
            raise Exception
        json_dict = self.to_dict()
        json.dump(json_dict, open(save_path, 'w'), indent=indent, ensure_ascii=False)
    
    @classmethod
    def load_from_path(cls: T, json_path: str) -> T:
        check_file_exists(json_path)
        json_dict = json.load(open(json_path, 'r'))
        return cls.from_dict(json_dict)

class BasicLoadableIdObject(BasicLoadableObject[T]):
    """
    Assumptions:
    ===========
        1. self.__dict__ matches constructor parameters perfectly.
        2. Any to_dict or to_dict_list methods of any class object in the class variable list doesn't take any parameters.
        3. Non-trivial classmethods must be defined in child class
        4. Must implement __str__
    """
    def __init__(self, id: int):
        super().__init__()
        self.id = id

class BasicHandler(Generic[H, T]):
    """
    Assumptions:
        1. Handler has only one class parameter: the object list.
        2. All contained objects are of type obj_type.
    """
    def __init__(self: H, obj_type: type, obj_list: List[T]=None):
        check_type(obj_type, valid_type_list=[type])
        self.obj_type = obj_type
        if obj_list is not None:
            check_type_from_list(obj_list, valid_type_list=[obj_type])
        self.obj_list = obj_list if obj_list is not None else []

    def __key(self) -> tuple:
        return tuple([self.__class__] + list(self.__dict__.values()))

    def __hash__(self):
        return hash(self.__key())

    def __add__(self, other: H) -> H:
        if isinstance(other, type(self)):
            if self.obj_type == other.obj_type:
                return type(self)(self.obj_list + other.obj_list)
            else:
                raise TypeError(
                    f"""
                    Cannot add {type(self).__name__} of {self.obj_type.__name__} and {type(other).__name__} of {other.obj_type.__name__}
                    """
                )
        else:
            raise TypeError(
                f"""
                Cannot add {type(self).__name__} and {type(other).__name__}
                """
            )

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__key() == other.__key()
        return NotImplemented

    def __str__(self: H):
        return f'{self.__class__.__name__}({[obj for obj in self]})'

    def __repr__(self: H):
        return self.__str__()

    def __len__(self: H) -> int:
        return len(self.obj_list)

    def __getitem__(self: H, idx: int) -> T:
        if type(idx) is int:
            if len(self.obj_list) == 0:
                printj.red(f"{type(self).__name__} is empty.")
                raise IndexError
            elif idx < -len(self.obj_list) or idx >= len(self.obj_list):
                printj.red(f"Index out of range: {idx}")
                raise IndexError
            else:
                return self.obj_list[idx]
        elif type(idx) is slice:
            return type(self)(self.obj_list[idx.start:idx.stop:idx.step])
        else:
            printj.red(f'Expected int or slice. Got type(idx)={type(idx)}')
            raise TypeError

    def __setitem__(self: H, idx: int, value: T):
        if type(idx) is int:
            check_type(value, valid_type_list=[self.obj_type])
            self.obj_list[idx] = value
        elif type(idx) is slice:
            check_type_from_list(value, valid_type_list=[self.obj_type])
            self.obj_list[idx.start:idx.stop:idx.step] = value
        else:
            printj.red(f'Expected int or slice. Got type(idx)={type(idx)}')
            raise TypeError

    def __delitem__(self: H, idx: int):
        if type(idx) is int:
            if len(self.obj_list) == 0:
                printj.red(f"{type(self).__name__} is empty.")
                raise IndexError
            elif idx < 0 or idx >= len(self.obj_list):
                printj.red(f"Index out of range: {idx}")
                raise IndexError
            else:
                del self.obj_list[idx]
        elif type(idx) is slice:
            del self.obj_list[idx.start:idx.stop:idx.step]
        else:
            printj.red(f'Expected int or slice. Got type(idx)={type(idx)}')
            raise TypeError

    def __iter__(self: H) -> H:
        self.n = 0
        return self

    def __next__(self: H) -> T:
        if self.n < len(self.obj_list):
            result = self.obj_list[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    @classmethod
    def buffer(cls: H, obj) -> H:
        return obj

    def copy(self: H) -> H:
        return type(self)(self.obj_list.copy())

    def append(self: H, item: T):
        check_type(item, valid_type_list=[self.obj_type])
        self.obj_list.append(item)

    def extend(self: H, item_list: List[T]):
        for item in item_list:
            self.append(item)

    def sort(self: H, attr_name: str, reverse: bool=False):
        if len(self) > 0:
            attr_list = list(self.obj_list[0].__dict__.keys())
            property_names = [p for p in dir(type(self.obj_list[0])) if isinstance(getattr(type(self.obj_list[0]), p), property)]
            attr_list.extend(property_names)
            if attr_name not in attr_list:
                printj.red(f"{self.obj_type.__name__} class has not attribute: '{attr_name}'")
                printj.red(f'Possible attribute names:')
                for name in attr_list:
                    printj.red(f'\t{name}')
                raise Exception

            self.obj_list.sort(key=operator.attrgetter(attr_name), reverse=reverse)
        else:
            printj.red(f"Cannot sort. {type(self).__name__} is empty.")
            raise Exception

    def shuffle(self: H):
        random.shuffle(self.obj_list)

class BasicLoadableHandler(BasicHandler[H, T]):
    """
    Assumptions:
        1. Handler has only one class parameter: the object list.
        2. All contained objects are of type obj_type.
        3. Any to_dict or to_dict_list methods of any class object in the object list doesn't take any parameters.
    """
    def __init__(self: H, obj_type: type, obj_list: List[T]=None):
        super().__init__(obj_type=obj_type, obj_list=obj_list)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.to_dict_list()})'

    def to_dict_list(self: H) -> List[dict]:
        return [item.to_dict() if not isinstance(item, tuple([dict, list, tuple, str, int, float, bool, type(None)])) else item for item in self]

    @classmethod
    # @abstractmethod
    def from_dict_list(cls: H, dict_list: List[dict]) -> H:
        """
        To Override
        """
        raise NotImplementedError

    def save_to_path(self: H, save_path: str, overwrite: bool=False):
        if check_file_exists(file_path=save_path, raise_error=False) and not overwrite:
            printj.red(f'File already exists at save_path: {save_path}')
            raise Exception
        json_data = self.to_dict_list()
        json.dump(json_data, open(save_path, 'w'), indent=2, ensure_ascii=False)
    
    @classmethod
    def load_from_path(cls: H, json_path: str) -> H:
        check_file_exists(json_path)
        json_dict = json.load(open(json_path, 'r'))
        return cls.from_dict_list(json_dict)

class BasicLoadableIdHandler(BasicLoadableHandler[H, T], BasicHandler[H, T]):
    """
    TODO: Figure out why VSCode shows syntax error unless I explicitly inherit from all levels of nested parent classes.

    Assumptions:
        1. Handler has only one class parameter: the object list.
        2. All contained objects are of type obj_type.
        3. Any to_dict or to_dict_list methods of any class object in the object list doesn't take any parameters.
        4. All objects in handler must have an id class variable.
    """
    def __init__(self: H, obj_type: type, obj_list: List[T]=None):
        super().__init__(obj_type=obj_type, obj_list=obj_list)
    
    def get_obj_from_id(self: H, id: int) -> T:
        id_list = []
        for obj in self:
            if id == obj.id:
                return obj
            else:
                id_list.append(obj.id)
        id_list.sort()
        printj.red(f"Couldn't find {self.obj_type.__name__} with id={id}")
        printj.red(f"Possible ids: {id_list}")
        raise Exception
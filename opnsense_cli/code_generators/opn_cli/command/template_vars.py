from dataclasses import dataclass
from typing import Callable, List, Literal, Tuple, Type


@dataclass
class Method:
    name: str
    http_method: Literal["get"] | Literal["post"]


@dataclass
class CommandTemplateVars:
    get_methods: Callable[[Type], List[Tuple[str, Callable]]]
    get_parameters: Callable
    controller: Type
    methods: List[Method]
    click_command: str
    click_group: str
    click_options_create: list
    click_options_update: list
    column_names: list
    column_list: str
    module_type: str


@dataclass
class CommandInitTemplateVars:
    click_group: str

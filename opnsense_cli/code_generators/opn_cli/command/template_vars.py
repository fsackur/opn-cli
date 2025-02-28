from dataclasses import dataclass
from typing import Callable, List, Tuple, Type


@dataclass
class CommandTemplateVars:
    get_methods: Callable[[Type], List[Tuple[str, Callable]]]
    get_parameters: Callable
    controller: Type
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

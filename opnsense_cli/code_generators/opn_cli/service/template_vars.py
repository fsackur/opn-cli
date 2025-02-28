from dataclasses import dataclass
from typing import Callable, List, Tuple, Type


@dataclass
class CommandServiceTemplateVars:
    get_methods: Callable[[Type], List[Tuple[str, Callable]]]
    controllers: List[Type]
    click_command: str
    click_group: str
    model_xml_tag: str
    resolver_map: dict
    module_type: str

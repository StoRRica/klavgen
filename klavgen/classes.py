from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

from .rendering import Renderable


@dataclass
class LocationOrientation:
    x: float
    y: float
    z: float = 0.0
    rotate: float = 0.0  # CCW
    rotate_around: Optional[Tuple[float, float]] = None


@dataclass
class Key(LocationOrientation):
    keycap_width: Optional[float] = None
    keycap_depth: Optional[float] = None


@dataclass
class RenderedKey:
    case_column: Any
    case_clearance: Any
    switch_rim: Any
    keycap_clearance: Any
    switch_hole: Any
    debug: Any


@dataclass
class RenderedKeyTemplates:
    switch_hole: Any
    case_clearance: Any
    keycap_clearance: Any


@dataclass
class ScrewHole:
    x: float
    y: float
    z: float = 0


@dataclass
class RenderedScrewHole:
    rim: Any
    hole: Any
    debug: Any


@dataclass
class Patch:
    points: List[Tuple[float, float]]
    height: float


@dataclass
class Cut:
    points: List[Tuple[float, float]]
    height: float


@dataclass
class Text(LocationOrientation):
    text: str = ""
    font_size: float = 6
    extrude: float = 0.4


@dataclass
class RenderedSideHolder:
    case_column: Any
    rail: Any
    hole: Any
    debug: Any


@dataclass
class Controller(LocationOrientation):
    pass


@dataclass
class TrrsJack(LocationOrientation):
    pass


@dataclass
class USBCJack(Renderable, LocationOrientation):
    name = "usbc_jack"
    render_func_name: str = "usbc_jack"


@dataclass
class PalmRest:
    points: List[Tuple[float, float]]
    height: float
    connector_locations_x: Optional[List[float]] = None


@dataclass
class RenderedSwitchHolder:
    switch_holder: Any
    socket: Any

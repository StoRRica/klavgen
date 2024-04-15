from klavgen import *
from klavgen.classes import Key
import time

import cadquery as cq

config = Config(case_config=CaseConfig(
        side_fillet=4,
        # palm_rests_top_fillet=5,
        switch_type=SwitchType.MX,
        case_base_height = 11.5,
        case_thickness=1.8,
    ),
    mx_key_config=MXKeyConfig(
        case_tile_margin=7.5,
    ),
    choc_key_config=ChocKeyConfig(case_tile_margin=7.6),
    controller_config=ControllerConfig(case_tile_margin=5),
    usbc_jack_config=USBCJackConfig(case_tile_margin=5),
    kailh_mx_socket_config=KailhMXSocketConfig(
        socket_height=2,
    )
)

keys : Key = generate_keys_from_kle_json("./resources/oppodox-layout.json")

key: Key
for key in keys:
    print(key)

controller = Controller(x=154, y=14)

usbc_jack = USBCJack(x=161, y=-51, rotate=-180)

screw_holes = [  # Clockwise
    ScrewHole(x=-3, y=8.5, z=0),
    ScrewHole(x=86, y=9.5, z=0),
    ScrewHole(x=172.5, y=8.5, z=0),
    ScrewHole(x=172.5, y=-45.5, z=0),
    ScrewHole(x=143, y=-86, z=0),
    ScrewHole(x=145, y=-133.5, z=0),
    ScrewHole(x=86, y=-92, z=0),
    ScrewHole(x=-3, y=-95, z=0),
]

patches = [
    Patch(
        points=[
            (-9.85, 14.5),
            (178, 14.5),
            (178, -51),
            (150, -51),
            (150, -100),
            (163, -116),
            (148, -143),
            (135, -135),
            (75, -100),
            (-9.85, -100),
        ],
        height=config.case_config.case_base_height,
    ),

]


case_extras = [
    (
        cq.Workplane("XY")
        .workplane(offset=-config.case_config.case_base_height)
        .center(69.75, -4)
        .circle(15)
        .extrude(config.case_config.case_base_height)
    )
]

texts = [
    Text(x=16, y=5, z=0, text=time.strftime("%H:%M - %d %m, %Y"), font_size=2, extrude=0.4),
    Text(x=155, y=-20, z=0, rotate=-45, text="OppoDox", font_size=8, extrude=0.4)
]


render_and_save_keyboard(keys=keys,
                         controller=controller,
                         patches=patches,
                        #  case_extras=case_extras,
                        #  texts=texts,
                         render_standard_components=True,
                         # components=[usbc_jack],
                         config=config,
                         screw_holes=screw_holes
                         )

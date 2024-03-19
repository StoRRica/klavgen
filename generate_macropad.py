from klavgen import *
from klavgen.classes import Key

import cadquery as cq

config = Config(case_config=CaseConfig(
        side_fillet=4,
        palm_rests_top_fillet=5,
        switch_type=SwitchType.MX,
    ),
    mx_key_config=MXKeyConfig(case_tile_margin=7.5),
    choc_key_config=ChocKeyConfig(case_tile_margin=7.6),
    controller_config=ControllerConfig(case_tile_margin=5),
    usbc_jack_config=USBCJackConfig(case_tile_margin=5),
)

keys : Key = generate_keys_from_kle_json("./keyboard-layout.json")

key: Key
for key in keys:
    print(key)

controller = Controller(x=47.5, y=34)

# screw_holes = [  # Clockwise from top left
#     ScrewHole(x=-11.4, y=30.4),
#     ScrewHole(x=30.5, y=30.4),
#     ScrewHole(x=78.4, y=30.4),
#     ScrewHole(x=78.4, y=9.5),
#     ScrewHole(x=30.5, y=-15),
#     ScrewHole(x=-11.5, y=-15),
# ]

patches = [
    Patch(
        points=[
            (-15, 34),
            (82, 34),
            (82, 7),
            (57.5, -15),
            (30.5, -15),
            (9.5, -18),
            (-15, -15),
        ],
        height=config.case_config.case_base_height,
    ),
    Patch(
        points=[
            (140, 14),
            (171.9, 14),
            (171.9, -43.9),
            (140, -43.9),
        ],
        height=config.case_config.case_base_height,
    )
]

cuts = [
    Cut(
        points=[(57.5, -15), (82, 7), (82, -15)],
        height=config.case_config.case_base_height,
    )
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


render_and_save_keyboard(keys=keys,
                         controller=controller,
                        #  patches=patches,
                        #  cuts=cuts,
                        #  case_extras=case_extras,
                        #  screw_holes=screw_holes
                         )

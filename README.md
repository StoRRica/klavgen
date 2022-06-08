# Klavgen: handwired keyboard generator

Klavgen is a handwired keyboard generator written in Python, on top of [CadQuery](https://github.com/CadQuery/cadquery).
It produces keyboards (like on the left) and optionally makes handwiring easy and organized via switch holders (on the
right):

<p align="center">
<img src="img/klavyl/front.png" alt="Klavyl" width="350"/>
<img src="img/switch_holders.jpg" alt="Switch holders after soldering" width="350"/>
</p>

**Note:** Klavgen is heavily work-in-progress and lots of stuff may not be working. If you experience issues, please
submit a Github issue.

Klavgen benefits:

- **Generates the full keyboard**, including plate, bottom, palm rests and holders for the controller and TRRS jack
- All models are optimized for home **FDM printing with no supports**
- Produces **slim keyboards**: only 11 mm high in the default configuration
- Support Kailh **hotswap sockets**, with support for both **MX** and **Choc** switches
- Makes it **easy to solder** things, and requires no glue whatsoever
- Uses **uninsulated wires**, thus no tedious wire stripping
- Makes it easy to **reposition the keys after making the keyboard**
- Produces a sturdy build that **doesn't flex** when typed on

The last 5 benefits are achieved by optionally using switch holders (MX/Choc) that organize the wires, hold the Kailh
sockets and diodes, support the switches, enable soldering everything in place, and allow moving keys later (they even
have wire slack so that you can space keys further apart).

Klavgen can also skip the usage of switch holders to generate just a case with normal switch holes.

Limitations:

- Configuring a keyboard requires code, it's not as easy as YAML
- Docs are scarce (as you'll see below)

# What's new

- Jun 7, 2022: Add support for not using switch holders, therefore generating simple switch holes
- May 20, 2022: Add support for Choc switches and refactor switch holder generation
- May 10, 2022: Improve generation from KLE (http://www.keyboard-layout-editor.com/) (thanks @Tructruc) and support case
  geometry via the new `case_extras` parameter
- Apr 25, 2022: Add example STLs and improce docs
- Mar 31, 2022: Initial check-in

# Example STL outputs

See the [`example_stls`](example_stls) directory for example STL outputs. These were generated by
[`example.py`](example_5__all_features.py), see more about that below.

| Component                                                                                                                                                                                                 | STL file (for MX build)                                       | Preview                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Bottom**                                                                                                                                                                                                | [`keyboard_bottom.stl`](example_stls/keyboard_bottom.stl)     | <p align="center"><img src="img/components/bottom.png" alt="Bottom" width="300"/></p>                      |
| **Top plate**: flat with simple holes so that it can be made with a laser cutter or a CNC machine                                                                                                         | [`keyboard_top.stl`](example_stls/keyboard_top.stl)           | <p align="center"><img src="img/components/top.png" alt="Top" width="300"/></p>                            |
| **Palm rest**: attaches to the bottom via connectors (can also be fused with the bottom, see below)                                                                                                       | [`palm_rest.stl`](example_stls/palm_rest.stl)                 | <p align="center"><img src="img/components/palm_rest.png" alt="Palm rest back" width="300"/></p>           |
| **Switch holder**: Holds the Kailh hotswap socket (MX or Choc) and allows you to solder the diode, column and row wires in-place. These  should be printed in ABS since the soldering iron will be close. | [`switch_holder.stl`](example_stls/switch_holder.stl)         | <p align="center"><img src="img/components/switch_holder.png" alt="Switch holder" width="200"/></p>        |
| **Pro Micro controller holder**: holds the Arduino Pro Micro                                                                                                                                              | [`controller_holder.stl`](example_stls/controller_holder.stl) | <p align="center"><img src="img/components/controller_holder.png" alt="Pro Micro holder" width="200"/></p> |
| **TRRS jack holder**: holds the TRRS jack                                                                                                                                                                 | [`trrs_jack_holder.stl`](example_stls/trrs_jack_holder.stl)   | <p align="center"><img src="img/components/trrs_jack_holder.png" alt="TRRS jack holder" width="150"/></p>  |
| **Connector**: connects the palm rest to the bottom                                                                                                                                                       | [`connector.stl`](example_stls/connector.stl)                 | <p align="center"><img src="img/components/connector.png" alt="Connector" width="150"/></p>                |

# Keyboards generated with Klavgen

## Klavyl

[Klavyl](https://github.com/klavgen/klavyl) is my personal keyboard, a modification to
[Redox](https://github.com/mattdibi/redox-keyboard). It uses most of Klavgen's capabilities, including screw holes,
manually defined case outlines, Pro Micro and TRRS jack cutouts and holders, and palm rests. Check out the repo for the
full config.

<p align="center">
<img src="img/klavyl/front.png" alt="Klavyl" width="700"/>
</p>

# Installing

## 1. Install CadQuery

Install Miniconda and create an environment for CadQuery, following the
[official instructions](https://cadquery.readthedocs.io/en/latest/installation.html#installation).

## 2. Get comfortable using CadQuery

Get familiar with either of CadQuery's UIs: [CQ-editor](https://github.com/CadQuery/CQ-editor) or
[jupyter-cadquery](https://github.com/bernhard-42/jupyter-cadquery) (which I prefer).

Ensure that you know how to view objects returned from code, using `show_object()` in CQ-editor or `show()` in Jupyter
Lab (from `jupyter_cadquery.cadquery`).

## 3. Download Klavgen

Klavgen is not yet packaged, so you need to download and use it locally within a project (clone or download and extract
the ZIP file; example assumes cloning).

```
git clone git@github.com:klavgen/klavgen.git
```

Start your project in the `klavgen` repo directory. This is where you'll have to write your scripts for now, since you
need to import the `klavgen` package (which is in a sub-dir):

# WARNING!!!

CadQuery is very finicky when it comes to filleting (the `fillet()` command), and sometimes when it comes to shelling
(the `shell()` command). Klavgen tries to provide helpful error messages when CadQuery fails, please follow them. In
general, it is highly recommended to always provide the `case_extras` parameter or use a `Patch` object to define the
outline of your case to ensure there are no small features or holes that can trip filleting or shelling.

If rendering fails in a shell, you should try `render_case()` with `debug=True`, which skips the shell step.

The 2 most important fillet settings, `CaseConfig.side_fillet` and `CaseConfig.palm_rests_top_fillet` are disabled by
default, which makes default keyboards ugly.

These are the main gotchas:

- Shelling fails because your case is not continuous (e.g. the thumb cluster doesn't connect to the main body), has very
  sharp corners, or has small features.
- Filleting fails because the object has features smaller than the fillet size.
- Filleting succeeds but produces an invalid shape that later on causes errors when operated on (e.g. via a `.cut()`).

# Tutorial

Note that all the `show()` commands below are meant to illustrate the use in Jupyter Lab. If you use CQ-editor, the
commands may differ.

## 1. Generate a 1-key keyboard case

Run the following code to generate a single-key keyboard
([`example_1__single_key_render.py`](example_1__single_key_render.py)):

```
from klavgen import *

keys = [Key(x=0, y=0)]

case_result = render_case(keys=keys)
```

The `render_case()` method is the method you'll use most often while designing the keyboard. It returns a fairly complex
`RenderCaseResult` object which tracks the full progress of the keyboard construction to help you in fixing issues.

**Note**: You can pass in a `RenderCaseResult` object as the `result` parameter. Then, `render_case()` will save
intermediate objects to the passed-in variable while rendering is taking place, allowing you to observe what happened if
rendering raises an exception.

Here, we'll only focus on these 3 keys part in the `result` object:

- `case_result.top` is the top plate (`show(case_result.top)`)

<p align="center">
<img src="img/simple/simple_top.png" width="350"/>
</p>

- `case_result.bottom` is the case bottom (`show(case_result.bottom)`)

<p align="center">
<img src="img/simple/simple_bottom.png" width="350"/>
</p>

- `case_result.debug` shows keycap and holder outlines, helping you debug designs. This part should not be saved or
  used. By default, the outlines use the keycap width and depth from the configuration, but you can also pass in
  `keycap_width` and `keycap_depth` parameters to `Key()` to adjust these per key.

Rendering all 3 shows you the bottom, top and the debug outline in the air
((`show(case_result.top, case_result.bottom, case_result.debug)`):

<p align="center">
<img src="img/simple/simple_all.png" width="350"/>
</p>

## 2. Save the 1-key keyboard case

You can now export the dummy "keyboard" you created, via the `render_and_save_keyboard()` method, which takes the same
parameters as `render_case()` (see full code in [`example_2__single_key_save.py`](example_2__single_key_save.py)):

```
from klavgen import *

keys = [Key(x=0, y=0)]

keyboard_result = render_and_save_keyboard(keys=keys)
```

You should see a series of `.stl` files in your working directly. The files depend on the features your keyboard uses.
For now, you will only see the top plate, the case bottom, and the switch holder. For a complete keyboard, you may also
see the controller holder, the TRRS jack holder, palm rest(s), and the palm rests connector.

The `render_and_save_keyboard()` method renders the case (and takes the same parameters as `render_case()`) and then
saves all relevant components to `.stl` files. It returns an object of type `RenderKeyboardResult`. In the current
example, that object contains only the `.case_result`, `.top`, `.bottom`, and `.switch_holder` items. See below for the
full list of members.

By default, Klavgen generates keyboards for MX switches, where `switch_holder.stl` looks like this:

<p align="center">
<img src="img/components/switch_holder_mx.png" width="350"/>
</p>

This is what the switch holder looks like when put in place:

<p align="center">
<img src="img/simple/simple_top_with_switch_holder_from_top.png" alt="Switch holder in position, from top" height="220"/>
<img src="img/simple/simple_top_with_switch_holder_from_bottom.png" alt="Switch holder in position, from bottom" height="220"/>
</p>

See below on how to make your keyboard use Kailh Choc switches.

## 3. Generate a more complex case

This is a more complex "keyboard", with screw holes and a palm rest
([`example_3__screw_holes_and_palm_rest.py`](example_3__screw_holes_and_palm_rest.py):

```
from klavgen import *

config = Config()

keys = [Key(x=0, y=0)]

screw_holes = [
    ScrewHole(x=13, y=13),
    ScrewHole(x=13, y=-13),
    ScrewHole(x=-13, y=-13),
]

palm_rests = [
    PalmRest(
        points=[(13, -5), (13, -30), (-13, -30), (-13, -5)],
        height=config.case_config.case_base_height + 2,
        connector_locations_x=[0],
    ),
]

case_result = render_case(keys=keys, palm_rests=palm_rests, screw_holes=screw_holes, config=config)
```

This time, besides the `case_result.top` and `case_result.bottom` objects, you can also check out the
`case_result.palm_rests[0]` one to see the palm rest.

This is the result (`show(result.top, result.bottom, result.palm_rests[0])`):

<p align="center">
<img src="img/complex/complex_all_front.png" width="350"/>
<img src="img/complex/complex_all_side.png" width="350"/>
</p>

Note that the palm rest is detachable.

### Fixed palm rests

You can make the palm rest a part of the bottom by changing the config (see full code in
[`example_3__screw_holes_and_palm_rest_non_detachable.py`](example_3__screw_holes_and_palm_rest_non_detachable.py)):

```
config = Config(case_config=CaseConfig(detachable_palm_rests=False))
```

Now the `case_result.palm_rests` object is `None` so don't try to view it. Instead, just check out the case bottom
(`show(result.bottom)`):

<p align="center">
<img src="img/complex/complex_bottom_non_detachable_palm_rests.png" width="350"/>
</p>

### Do not use switch holders

If you do not want to use switch holders, you can disable them (see full code in
[`example_3__screw_holes_and_palm_rest_no_holder.py`](example_3__screw_holes_and_palm_rest_no_holder.py)):

```
config = Config(case_config=CaseConfig(use_switch_holders=False))
```

Now the plate only has a square hole (`show(result.top, result.bottom, result.palm_rests[0])`):

<p align="center">
<img src="img/complex/complex_all_front_no_switch_holder.png" width="350"/>
</p>

## 4. Let's use Choc switches

Let's change the config of the previous example to use Choc switches. This will change the size of the plate holes and
will produce Choc switch holders (see full code in
[`example_4__screw_holes_and_palm_rest_choc.py`](example_4__screw_holes_and_palm_rest_choc.py)):

```
config = Config(case_config=CaseConfig(switch_type=SwitchType.CHOC))
```

The output `switch_holder.stl` file now looks like this:

<p align="center">
<img src="img/components/switch_holder_choc.png" width="350"/>
</p>

## 5. Generate a keyboard with all of Klavgen's features

Let's build a dummy keyboard using all of Klavgen's features
([`example_5__all_features.py`](example_5__all_features.py)):

```
import cadquery as cq

from klavgen import *

config = Config(case_config=CaseConfig(side_fillet=1, palm_rests_top_fillet=2))

keys = [  # By columns from bottom left
    Key(x=0, y=0),
    Key(x=0, y=19),
    Key(x=19, y=0),
    Key(x=19, y=19),
]

controller = Controller(x=47.5, y=34)

trrs_jack = TrrsJack(x=68, y=34)

screw_holes = [  # Clockwise from top left
    ScrewHole(x=-11.4, y=30.4),
    ScrewHole(x=30.5, y=30.4),
    ScrewHole(x=78.4, y=30.4),
    ScrewHole(x=78.4, y=9.5),
    ScrewHole(x=30.5, y=-15),
    ScrewHole(x=-11.5, y=-15),
]

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
        .circle(5)
        .extrude(config.case_config.case_base_height)
    )
]

palm_rests = [
    PalmRest(
        points=[(-15, 0), (34, 0), (34, -35), (-15, -35)],
        height=config.case_config.case_base_height + 10,
        connector_locations_x=[0, 20],
    ),
]

texts = [
    Text(x=45, y=-8.5, text="Plate", font_size=6, extrude=0.4),
    Text(x=10, y=-26, z=10, text="Palm rest", font_size=6, extrude=0.4),
]

keyboard_result = render_and_save_keyboard(
    keys=keys,
    screw_holes=screw_holes,
    controller=controller,
    trrs_jack=trrs_jack,
    patches=patches,
    cuts=cuts,
    case_extras=case_extras,
    palm_rests=palm_rests,
    texts=texts,
    debug=False,
    config=config,
)

print("Done")
```

This is the result (`show(keyboard_result.top, keyboard_result.bottom, keyboard_result.palm_rests[0])`):

<p align="center">
<img src="img/full/full_all.png" width="700"/>
</p>

# Extras

## Use a Keyboard Layout Editor export

You can build a keyboard from a [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/) layout. Do the
following:

1. Ensure the layout is contiguous. If it's a split keyboard, manually remove all the keys from one of the splits before
   exporting.

1. Go to the "Raw Data" tab and click "Download JSON" on the bottom right.

1. Run code like the following to generate the list of keys:

   ```
   from klavgen import *

   keys = generate_keys_from_kle_json("<path to downloaded json file>")
   ```

By default, keys are spaced 19.05mm apart. You can adjust this by passing the `step_size` parameter.

You can then use the standard `render_case()` or `render_and_save_keyboard()` methods to render the keyboard (see
above).

# Important constructs

## Important configs

- `CaseConfig.switch_type` allows you to set the type of switches (`SwithType.MX` or `SwithType.CHOC`)
- `CaseConfig.use_switch_holders` determines whether the keyboard will use switch holders (affects the cutouts and
  whether a switch holder is returned when rendering the keyboard).
- `CaseConfig.detachable_palm_rests` allows you to set whether palm rests should be detachable, or part of the case
  bottom.
- `CaseConfig.side_fillet` sets a fillet on the case vertical edges. You should likely always use it in the final
  product, but it's very prone to failure, see warning above.
- `CaseConfig.palm_rests_top_fillet` sets a fillet on the palm rest top edges. You should likely always use it the final
  product if you have palm rests (so they don't dig in your hands), but it's very prone to failure, see warning above.
- `ScrewHoleConfig.screw_insert_hole_width` sets the size of the hole for screws and defaults to a value suitable for
  melting inserts. If you don't use inserts, you should lower the value.
- `KeyConfig.case_tile_margin`, `ControllerConfig.case_tile_margin` and `TrrsJackConfig.case_tile_margin` is the size of
  the case generated around keys, controller holders, and TRRS jack holders. If you use `case_extras` or a `Patch`
  object to define your case outlines, you can freely lower these.
- `MXSwitchHolderConfig.switch_hole_tolerance` and `ChocSwitchHolderConfig.switch_hole_tolerance` sets (in mm) how much
  smaller the switch holes should be made to account for imperfections in 3D printing. Defaults to 0.05.

## The `render_standard_components` parameter

When `render_standard_components` is set to `True` in a call to `render_case`, all holders (switch, controller, TRRS
jack) and palm rest connectors are returned in the `.standard_components` object. These help you see what the final
keyboard will look like.

This is what `example.py` looks like with standard components added
(`show(keyboard_result.top, keybaord_result.bottom, keyboard_result.palm_rests[0], keyboard_result.case_result.standard_components)`):

<p align="center">
<img src="img/full/full_all_with_standard_components.png" width="700"/>
</p>

## The `RenderCaseResult` object returned from `render_case()`

This object contains the individual steps when constructing the case. They key outputs are 3:

- `case_result.top` is the top plate
- `case_result.bottom` is the case bottom
- `case_result.palm_rests` is a **list** of palm rest objects
- `case_result.standard_components` is a rendering of all holders (switch, controller, TRRS jack) and palm rest
  connectors (see above).

Additionally, there are many intermediate objects that are useful for troubleshooting and auditing when something is not
going right.

## The `RenderKeyboardResult` object returned from `render_and_save_keyboard()`

This object contains the final keyboard components:

- `keyboard_result.case_result` is the `RenderCaseResult` returned from the inner `render_case()` method. Always
  present.
- `keyboard_result.top` is the top plate (same as `case_results.top`). Always present.
- `keyboard_result.bottom` is the case bottom (same as `case_results.bottom`). Always present.
- `keyboard_result.switch_holder` is the switch holder. Present if switch holders are used
  (`CaseConfig.use_switch_holders`).
- `keyboard_result.connector` is the palm rests to case bottom connector. Present only if palm rests are defined and
  `CaseConfig.detachable_palm_rests` is `True`.
- `keyboard_result.controller_holder` is the controller holder. Present only if a controller is defined.
- `keyboard_result.trrs_jack_holder` is the TRRS jack holder. Present only if a TRRS jack is defined.
- `keyboard_result.palm_rests` is a **list** of palm rest objects (same as `case_results.palm_rests`). Present only if
  at least one palm rest is defined.

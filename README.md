# Creative Iterate Starter

Open-source starter kit for Creative scripts running inside Helios II.

This repository turns the runtime notes into a practical project layout with:

- README documentation
- ready-to-run examples
- reusable script templates
- helper utilities for state machines, deadzones, edges, and timing

## What this is

Creative scripts run a user-defined function:

```python
from gtuner import *
from creative_helper import *

combo = Combo()

def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes
    return combo.buttons, combo.sticks
```

Mental model:

```text
get_actual() -> your logic -> combo.set_val() -> return arrays
```

## Core rules

1. Create `combo = Combo()` at module level.
2. At the start of every frame, assign `combo.buttons, combo.sticks = button_bytes, stick_bytes`.
3. Read physical input with `get_actual()`.
4. Write output with `combo.set_val()`.
5. Always return `combo.buttons, combo.sticks`.

## Verified runtime assumptions

These files are written against the runtime behavior documented from Creative v0.4.2 inside Helios II.
Where behavior was not fully specified by runtime logs, the starter keeps things conservative.

## Important mapping notes

- Indices `0-8` match the expected button area.
- Indices `9-16` differ from the official GPC Xbox layout.
- In Creative:
  - `9-12` are D-pad
  - `13-16` are face buttons
- `STICK_1_*` is the RIGHT stick.
- `STICK_2_*` is the LEFT stick.

See `docs/INDEX_MAP.md` for the verified map.

## Repository layout

```text
creative-open-project/
  README.md
  LICENSE
  .gitignore
  docs/
    INDEX_MAP.md
    BEST_PRACTICES.md
  templates/
    basic_passthrough.py
    state_machine_template.py
    frame_overlay_template.py
    rhythm_template.py
  examples/
    button_to_right_stick.py
    timed_hold.py
    rhythm_pattern.py
    deadzone_debug_overlay.py
  utils/
    helpers.py
```

## Using a template

1. Pick a file from `templates/`.
2. Copy it into your Creative scripts directory.
3. Rename it.
4. Keep the file ASCII-only.
5. Edit only the logic section first.

## Example list

- `button_to_right_stick.py`: press RB, drive right stick Y.
- `timed_hold.py`: edge-triggered timed button hold.
- `rhythm_pattern.py`: dictionary-driven sequence using `set_val_from_dict()`.
- `deadzone_debug_overlay.py`: shows live stick values on the preview frame.

## Script authoring rules

### Input

Use:

```python
get_actual(index)
get_val(index)
```

Do not use `button_bytes` or `stick_bytes` as live input sources.

### Output

Use:

```python
combo.set_val(index, value)
```

### State

Store state on:

- the module-level `combo` object, or
- other module-level variables

### Timing

Creative runs about 120 times per second.
Useful conversions:

- 1 frame ~= 8.3 ms
- 12 frames ~= 100 ms
- 30 frames ~= 250 ms
- 60 frames ~= 500 ms
- 120 frames ~= 1 second

## Development pattern

Recommended frame structure:

```python
from gtuner import *
from creative_helper import *

combo = Combo()
combo.state = 0
combo.timer = 0
combo.prev_rb = 0.0


def iterate(button_bytes, stick_bytes, **kwargs):
    combo.buttons, combo.sticks = button_bytes, stick_bytes

    # Read
    rb = get_actual(3)

    # Logic
    if rb and not combo.prev_rb:
        combo.state = 1
        combo.timer = 30

    if combo.state == 1:
        combo.set_val(STICK_1_Y, 100)
        combo.timer -= 1
        if combo.timer <= 0:
            combo.state = 0

    # Update previous inputs
    combo.prev_rb = rb

    # Return
    return combo.buttons, combo.sticks
```

## Common mistakes

### 1. Using non-ASCII characters in script files

Keep Creative script files ASCII-only.

### 2. Reading from output buffers

Wrong:

```python
if button_bytes[3]:
    pass
```

Correct:

```python
if get_actual(3):
    pass
```

### 3. Using button-space indices for signed stick output

Wrong:

```python
combo.set_val(12, -100)
```

Correct:

```python
combo.set_val(STICK_1_Y, -100)
```

### 4. Forgetting to deep-copy rhythm dictionaries

`set_val_from_dict()` mutates its input.

### 5. Forgetting to reset combo state

Any activated, completed, timer, or phase values must be reset when your action finishes.

## Helper utilities

`utils/helpers.py` contains pure-Python helper functions for:

- deadzone filtering
- edge detection
- frame time conversion
- clamping
- polar stick math

Use them as a copy source when building larger scripts.

## License

MIT

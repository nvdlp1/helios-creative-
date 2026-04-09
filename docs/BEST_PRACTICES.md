# Best Practices

## Frame structure

Every script should follow this shape:

1. Assign output buffers to `combo`
2. Read physical inputs
3. Run logic
4. Update previous-frame state
5. Return arrays

## State machines

For anything more complex than a simple remap, use explicit states.

Suggested state names:

- IDLE
- STARTUP
- RUNNING
- COOLDOWN
- COMPLETE

## Edge-triggered buttons

Use press edges for one-shot actions.
Do not activate a one-shot every frame while a button is held.

## Deadzones

Treat small stick noise as neutral.
Suggested threshold: `8-12`.

## Output ownership

If multiple code paths write the same output index, the last write wins.
For larger scripts, calculate desired values first, then write once.

## Frame overlays

If you use `kwargs['frame']`, return it as the third value.
Overlay state, timers, and live inputs to debug behavior quickly.

## ASCII-only script files

Creative script files should stay ASCII-only to avoid runtime encoding errors.

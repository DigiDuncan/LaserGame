# LaserGame TODO

*Remove stuff from this list as it's completed.*

- Add mask-based collisions as well as the current box-based collisions.
- Clean up menu abstraction.
  - XML?
- Begin enemies.
- Move weapon colors to constants. [kinda done]
- Add current collisions to debug screen.
- Add hit-boxes to debug screen.
- Move tests to their own folder.
- Add debug menu.
  - Only show debug menu when in debug mode.
  - Menu items:
    - Show/Hide hit-boxes
    - Show/Hide UUIDs
    - Show/Hide collisions
- Use ConfigDicts.
- Rework the object heirarchy so that each object that's rectangley has a...
  - x, y, center attribute
  - left, top, right, and bottom property
  - topleft, topright, bottomleft, and bottomright property
  - setters for those
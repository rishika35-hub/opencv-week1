# OpenCV Window Differences (Linux vs Windows)

## Linux
- GUI windows must run in main thread
- cv2.waitKey() needed to update events
- Multiple windows require careful handling

## Windows
- Windows are thread-safe
- Multiple windows easier to manage

## Workarounds
- Always use cv2.waitKey() in loops
- Avoid heavy processing in main thread for Linux

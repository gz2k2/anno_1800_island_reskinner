# Changelog

## [v0.81.5]

### Added
- **Regional Settings Tab:** Added a darker Enbesa preset (needs testing).
- **Object Configuration Tab:** Added the ability to add, remove and change the density of placed objects. Settings are available in *Show Object Map* (includes help text explaining how it works).
- **Settings Tab:** Added a new folder configuration option: *"Map export folder"*.

### Changed
- **Settings Tab:** Renamed *"Custom map folder"* to *"Temporary map folder"*.
- **Finalize Tab:**
  - Renamed the *"Finalize"* button to *"Pack Island Data"*.
  - Added a new *"Export Map"* button, which copies the newly packed island map to the destination folder (*Map export folder*) without temporary files, leaving a clean, organized island file.

### Fixed & Improved
- **Performance Improvements:** Added background workers and progress bars. Several operations are now processed in RAM and saved later to enhance performance.
- **Slot Map & Object Map:** Corrected map dot positions so they now align properly on the map image.

### Experimental / Unstable
- **Slot Configuration:** Should not be used in this version. (Note: The *Slot Map* for viewing slots works correctly.)

### Known Issues
- Some tables and pop-up windows are not fully polished yet. You can manually resize the windows to display all UI elements correctly.
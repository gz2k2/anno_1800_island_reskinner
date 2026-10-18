# Anno 1800 Island Reskinner

**Anno 1800 Island Reskinner** is a specialized utility designed to streamline and automate the process of skinning and converting island maps for *Anno 1800*. 

This application translates the core concepts, manual patching steps, and file manipulations detailed in the official modding tutorials into a simplified user interface.

---

## 📌 Background & Credits

This tool is heavily based on the comprehensive **Skinning an Island Guide** created by **Hier0nimus**. 
* **Original Guide:** [Hier0nimus Island Skinning Tutorial](https://github.com)
* **Special Thanks:** Groundwork, file formats, and research credits go to **Taube**, **Taludas**, and **VALiiiUM** for making island skinning possible.

---

## 📦 What's Included

Everything you need to get started is packed directly into the distributed `.zip` file, including the app binaries and the foundational templates required for file conversion.

### Required Executables
The app utilizes standard community tools to decompress, patch, and recompress island database files:
* `rdaconsole.exe` — For packing and extracting `.a7m` island files.
* `filedbreader.exe` — For compressing and decompressing `.data` logic files into editable XML structure.

### Required XML Schemas
These specific file formats and mapping files are extracted from the skinning guide to ensure accurate parsing:
* `Island_Gamedata_v3.xml`
* `Island_RD3D.xml`
* `a7minfo.xml`
* `tmc.xml`

---

## ⚙️ Configuration & Setup

1. **Extract the Zip:** Unpack the contents of the download file into your preferred workspace directory.
2. **Configure Settings:** Open the application and navigate to the **Settings** tab.
3. **Map the Paths:** Ensure all executable files (`.exe`) and schema files (`.xml`) listed above are properly linked to their corresponding paths within the UI.

---

## 🎨 Custom Material Sets

Integrated material sets can be selected from the dropdown menu in the **"Material Sets"** tab and exported using the **"Save as..."** option. 

You can also integrate your own material sets into the application:
* Create a new folder named `custom_material_sets` directly inside the main application directory.
* The tool will automatically detect and load any valid material sets placed within this folder.

---

## Known Bugs

- If a folder contains two island variants (normal/river), both variants are copied and incorrectly interpreted.
  **Workaround:** Place each island variant in its own folder.
- The "dot" placement on the map is incorrect and does not match the zoom/pan.
- Automatic TMC data loading is buggy. In some cases, you need to manually select the meshes folder and click reload.      

---

## Contributing

The config and database files are available on the GitHub page. If you have additional settings or would like to improve the categories, feel free to do so. I also welcome optimized `material_sets` — just submit your new files as a pull request (PR).   


---

## 📖 Usage Guide (Community Call)

> 💡 **Note from the Developer:** 
> Due to time constraints, an official, step-by-step application user manual is currently unavailable. 
> 
> If you are familiar with the app workflow and the underlying mechanics of `FileDBReader` / `RdaConsole`, **contributions are highly welcome!** Please feel free to write up a usage guide and submit a Pull Request to help out your fellow modders.

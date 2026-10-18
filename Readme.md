# Anno Island Reskinner

**Anno Island Reskinner** is a specialized utility designed to streamline and automate the process of skinning and converting island maps for *Anno 1800*. 

This application translates the core concepts, manual patching steps, and file manipulations detailed in the official modding tutorials into a simplified user interface.

---

## 📌 Background & Credits

This tool is heavily based on the comprehensive **Skinning an Island Guide** created by **Hier0nimus**. 
* **Original Guide:** [Hier0nimus Island Skinning Tutorial](https://github.com/anno-mods/modding-guide/blob/main/hier0nimus-tutorials/07-skinning-island/readme.md)
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

## 📖 Usage Guide (Community Call)

> 💡 **Note from the Developer:** 
> Due to time constraints, an official, step-by-step application user manual is currently unavailable. 
> 
> If you are familiar with the app workflow and the underlying mechanics of `FileDBReader` / `RdaConsole`, **contributions are highly welcome!** Please feel free to write up a usage guide and submit a Pull Request to help out your fellow modders.

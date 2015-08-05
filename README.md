# Material Spacegray Theme
A fusion between [Material](https://github.com/equinusocio/material-theme) and [Spacegray](https://github.com/kkga/spacegray), two of the most popular themes for Sublime Text.

## Screenshots

### Material Spacegray

![](https://raw.githubusercontent.com/saadq/Material-Spacegray/master/screenshots/Material%20Spacegray.png)

### Material Spacegray Darker

![](https://raw.githubusercontent.com/saadq/Material-Spacegray/master/screenshots/Material%20Spacegray%20Darker.png)

#### You can also mix and match

![](https://raw.githubusercontent.com/saadq/Material-Spacegray/master/screenshots/Material%20Spacegray%20Mixed.png)

*The font used in the screenshot is [__Fira Mono__](https://mozilla.github.io/Fira/).*

## Installation

### Via Package Control

The easiest way to install is using [Sublime Package Control](https://sublime.wbond.net), where Material Spacegray is listed as `Material Spacegray`.

1. Open Command Palette using menu item `Tools -> Command Palette...` (<kbd>⇧</kbd><kbd>⌘</kbd><kbd>P</kbd> on Mac)
2. Choose `Package Control: Install Package`
3. Find `Material Spacegray` and hit <kbd>Enter</kbd>


### Manually

You can also install the theme manually:

1. Download the [latest release](https://github.com/saadq/Material-Spacegray/releases/latest), extract and rename the folder to **"Material Spacegray"**.

2. Move the folder inside your sublime Packages directory. **(Preferences > Browse packages...)**

3. Activate the theme with the following preferences at  **(Preferences > Setting - User)**:

#### Material Spacegray:
```json
"theme": "Material Spacegray.sublime-theme",
"color_scheme": "Packages/Material Spacegray/schemes/Material Spacegray.tmTheme",
```

#### Material Spacegray Darker:
```json
"theme": "Material Spacegray Darker.sublime-theme",
"color_scheme": "Packages/Material Spacegray/schemes/Material Spacegray Darker.tmTheme",
```

***Note*** : Remember to restart Sublime Text after activating the theme.

## Theme options

```json
"material_spacegray_small_tab": true,                // Set small tabs
"material_spacegray_disable_fileicons": true,        // Hide siderbar file type icons
"material_spacegray_disable_folder_animation": true, // Disable folder animation
"material_spacegray_small_statusbar": true,          // Set small status bar
"material_spacegray_disable_tree_indicator": true,   // Disable sidebar file indicator
"material_spacegray_bold_tab": true,                 // Make the tab labels bolder
"material_spacegray_accent_lime": true,              // set green lime accent color
"material_spacegray_accent_purple": true,            // set purple accent color
"material_spacegray_accent_red": true,               // set pale red accent color
"material_spacegray_accent_orange": true,            // set orange accent color
"material_spacegray_accent_yellow": true,            // set yellow accent color
```

## Recommended UI and font settings
Here are some recommendations for your custom settings to make a better experience with the theme:

```json
"overlay_scroll_bars": "enabled",
"line_padding_top": 1,
"line_padding_bottom": 1,
"font_options": [ "gray_antialias" ], // On retina Mac
"always_show_minimap_viewport": true,
"bold_folder_labels": true,
```

## Credits
Thanks to the original creators of the [Material](https://github.com/equinusocio/material-theme) and [Spacegray](https://github.com/kkga/spacegray) theme.

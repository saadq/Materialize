# Materialize
Bringing Material to the some of the most popular color schemes for Sublime:

* Spacegray
* Solarized
* Monokai
* Oceanic Next
* Seti
* Twilight
* Zenburn

## Click [here](/screenshots.md) to see some screenshots.

---

## Installation

### Via Package Control

The easiest way to install is using [Sublime Package Control](https://sublime.wbond.net), just search for "Materialize".

1. Open Command Palette using menu item `Tools -> Command Palette...` (<kbd>⇧</kbd><kbd>⌘</kbd><kbd>P</kbd> on Mac)
2. Choose `Package Control: Install Package`
3. Find `Materialize` and hit <kbd>Enter</kbd>


### Manually

You can also install the theme manually:

1. Download the [latest release](https://github.com/saadq/Material-Spacegray/releases/latest), extract and rename the folder to **"Material Spacegray"**.

2. Move the folder inside your sublime Packages directory. **(Preferences > Browse packages...)**


## Activation
Activate the theme with the following preferences at  **(Preferences > Setting - User)**:

#### Material Spacegray:
```json
"theme": "Material Spacegray.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Spacegray.tmTheme",
```

#### Material Solarized:
```json
"theme": "Material Solarized.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Solarized.tmTheme",
```

#### Material Monokai:
```json
"theme": "Material Monokai.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Monokai.tmTheme",
```

#### Material Oceanic Next:
```json
"theme": "Material Oceanic Next.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Oceanic Next.tmTheme",
```

#### Material Seti:
```json
"theme": "Material Seti.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Seti.tmTheme",
```

#### Material Twilight:
```json
"theme": "Material Twilight.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Twilight.tmTheme",
```

#### Material Zenburn:
```json
"theme": "Material Zenburn.sublime-theme",
"color_scheme": "Packages/Materialize/schemes/Material Zenburn.tmTheme",
```

***Note*** : Remember to restart Sublime Text after activating the theme.

## Theme options

```json
"material_theme_small_tab": true,                // Set small tabs
"material_theme_disable_fileicons": true,        // Hide siderbar file type icons
"material_theme_disable_folder_animation": true, // Disable folder animation
"material_theme_small_statusbar": true,          // Set small status bar
"material_theme_disable_tree_indicator": true,   // Disable sidebar file indicator
"material_theme_bold_tab": true,                 // Make the tab labels bolder
"material_theme_accent_lime": true,              // set green lime accent color
"material_theme_accent_purple": true,            // set purple accent color
"material_theme_accent_red": true,               // set pale red accent color
"material_theme_accent_orange": true,            // set orange accent color
"material_theme_accent_yellow": true,            // set yellow accent color
```

## Recommended UI and font settings
Here are some recommendations for your user settings to make a better experience with the theme:

```json
"overlay_scroll_bars": "enabled",
"line_padding_top": 1,
"line_padding_bottom": 1,
"font_options": [ "gray_antialias" ], // On retina Mac
"always_show_minimap_viewport": true,
"bold_folder_labels": true,
```

## Credits
Thanks to the original [creator](https://github.com/equinusocio) of the [Material](https://github.com/equinusocio/material-theme) theme.
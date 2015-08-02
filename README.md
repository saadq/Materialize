# Spacegray Material Theme for Sublime Text 3
A fusion between [Material](https://github.com/equinusocio/material-theme) and [Spacegray](https://github.com/kkga/spacegray), two of the most popular themes for Sublime Text.


## Screenshots

![](https://raw.githubusercontent.com/saadq/Material-Spacegray/master/screenshots/Material-Spacegray.png?token=AFamZkMOMtkS--ADNagQYSBQuN9JJ3eJks5Vx7zKwA%3D%3D)

## Easy installation
You can install this awesome theme through the [Package Control](https://packagecontrol.io/installation). Search for *"Material-Spacegray"*, install, **restart Sublime Text** and enjoy!

--

**Manual installation**

1. Download the [latest release](https://github.com/saadq/Material-Spacegray/releases/latest), extract and rename the folder to **"Material-Spacegray"**.

2. Move the folder inside your sublime Packages directory. **(Preferences > Browse packages...)**

3. Activate the theme with the following preferences at  **(Preferences > Setting - User)**:

```json
"theme": "Material-Spacegray.sublime-theme",
"color_scheme": "Packages/Material-Spacegray/schemes/base16-ocean.tmTheme",
```

***Note*** : Remember to restart Sublime Text after activating the theme.


## Theme options

```json
"material_spacegray_small_tab": true,                  // Set small tabs
"material_spacegray_disable_fileicons": true,          // Hide siderbar file type icons
"material_spacegray_disable_folder_animation": true,   // Disable folder animation
"material_spacegray_small_statusbar": true,            // Set small status bar
"material_spacegray_disable_tree_indicator": true,		// Disable sidebar file indicator
"material_spacegray_bold_tab": true,							// Make the tab labels bolder
"material_spacegray_accent_lime": true,						// set green lime accent color
"material_spacegray_accent_purple": true,					// set purple accent color
"material_spacegray_accent_red": true,						// set pale red accent color
"material_spacegray_accent_orange": true,					// set orange accent color
"material_spacegray_accent_yellow": true,					// set yellow accent color
```

## Recommended UI and font settings
I suggest you to use this custom settings for a better experience with the theme:

```json
"overlay_scroll_bars": "enabled",
"line_padding_top": 1,
"line_padding_bottom": 1,
"font_options": [ "gray_antialias" ], // On retina Mac
"always_show_minimap_viewport": true,
"bold_folder_labels": true,
```

The font used for the code is "[Fira Mono](https://mozilla.github.io/Fira/)".


## Credits
Thanks to the original creators of the [Material](https://github.com/equinusocio/material-theme) and [Spacegray](https://github.com/kkga/spacegray) theme!


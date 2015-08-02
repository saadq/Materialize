# Spacegray Material Theme for Sublime Text 3
This theme is meant to be a nice blend between [Material]() and [Spacegray](), two of the most popular themes for Sublime Text.


## Screenshots

![Default version](http://equinusocio.github.io/material-theme/assets/materialtheme.png)

![Darker version](http://equinusocio.github.io/material-theme/assets/img/darker1.png)

![Lighter version](https://transfer.sh/CyRdb/screen-shot-2015-07-11-at-15.52.39.png)

More screenshots [here](http://equinusocio.github.io/material-theme/)

## Easy installation
You can install this awesome theme through the [Package Control](https://packagecontrol.io/installation). Search for *"Material Theme"*, install, **restart Sublime Text** and enjoy!

--

**Manual installation**

1. Download the [latest release](https://github.com/equinusocio/material-theme/releases/latest), extract and rename the folder to **"Material Theme"**.

2. Move the folder inside your sublime Packages directory. **(Preferences > Browse packages...)**

3. Activate the theme with the following preferences at  **(Preferences > Setting - User)**:

```json
"theme": "Material-Theme.sublime-theme",
"color_scheme": "Packages/Material Theme/schemes/Material-Theme.tmTheme",
```

***Note*** : Remember to restart Sublime Text after activating the theme.


## Theme options

```json
"material_theme_small_tab": true,                  // Set small tabs
"material_theme_disable_fileicons": true,          // Hide siderbar file type icons
"material_theme_disable_folder_animation": true,   // Disable folder animation
"material_theme_small_statusbar": true,            // Set small status bar
"material_theme_disable_tree_indicator": true,		// Disable sidebar file indicator
"material_theme_bold_tab": true,							// Make the tab labels bolder
"material_theme_accent_lime": true,						// set green lime accent color
"material_theme_accent_purple": true,					// set purple accent color
"material_theme_accent_red": true,						// set pale red accent color
"material_theme_accent_orange": true,					// set orange accent color
"material_theme_accent_yellow": true,					// set yellow accent color
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

The font used for the code is "[Fira Mono]()" with code ligatures (not supported in Sublime Text).


## Other Resources

**App icon**

[Download](https://dribbble.com/shots/2104476-Material-Theme-for-Sublime-Text-3/attachments/380650) the official Material Theme icon.


## Credits
Thanks to the original creators of the [Material]() and [Spacegray]() theme!


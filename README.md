# Materialize
Bringing [Material theme](https://github.com/equinusocio/material-theme) to the some of the most popular color schemes for Sublime. Click [here](/Screenshots.md) to see some more screenshots.

![](/screenshots/material-spacegray.png)

Availabile themes/color schemes:

* Behave
* Brogrammer
* Cobalt
* Flatland
* Glacier
* Monokai
* Oceanic Next
* One Dark
* Seti
* Solarized Dark
* Solarized Light
* Spaceblack
* Spacegray
* Spacegray Eighties
* Spacegray Light
* Spacegray Mocha
* Stereokai
* Toy Chest
* Twilight
* Vim Blackboard
* Primer Light
* Zenburn

## Installation

### Via Package Control

The easiest way to install is using [Sublime Package Control](https://packagecontrol.io/installation), just search for "Materialize".

1. Open Command Palette using menu item `Tools -> Command Palette...` (<kbd>⇧</kbd><kbd>⌘</kbd><kbd>P</kbd> on Mac)
2. Choose `Package Control: Install Package`
3. Find `Materialize` and hit <kbd>Enter</kbd>


### Manually

You can also install the theme manually:

1. Download the [latest release](https://github.com/saadq/Materialize/releases/latest), extract and rename the folder to **"Materialize"**.

2. Move the folder inside your sublime Packages directory. **(Preferences > Browse packages...)**


## Activation
Activate the theme with the following preferences at  **(Preferences > Setting - User)**, based on the theme you want to use. If you wanted to use Brogrammer for example, you would need to do:

```json
{
    "color_scheme": "Packages/Materialize/schemes/Material Brogrammer.tmTheme",
    "theme": "Material Brogrammer.sublime-theme"
}
```

***Note*** : Remember to restart Sublime Text after activating the theme.

## Theme options

```json
{
    "material_theme_contrast_mode": true,
    "material_theme_small_tab": true,
    "material_theme_disable_fileicons": true,
    "material_theme_disable_folder_animation": true,
    "material_theme_small_statusbar": true,
    "material_theme_disable_tree_indicator": true,
    "material_theme_bold_tab": true,
    "material_theme_accent_lime": true,
    "material_theme_accent_purple": true,
    "material_theme_accent_red": true,
    "material_theme_accent_orange": true,
    "material_theme_accent_yellow": true
}
```

## Recommended UI and font settings
Here are some recommendations for your user settings to make a better experience with the theme:

```json
{
    "overlay_scroll_bars": "enabled",
    "line_padding_top": 1,
    "line_padding_bottom": 1,
    "always_show_minimap_viewport": true,
    "bold_folder_labels": true
}
```

Additionally, if you are on Retina:

```json
{
    "font_options": [ "gray_antialias" ]
}
```

## Known Issues
Please see the issue [#67](https://github.com/equinusocio/material-theme/issues/67) in the original Material theme if you can't see the bottom panel (find/replace, rename, move, can't see the box inputs in SidebarEnhancement, etc..). The quick fix is to just grab the border of the panel and move it:

![Drag the top edge](https://cloud.githubusercontent.com/assets/474329/8178894/a0dd09c0-1412-11e5-8ecf-f7f9ade439ae.gif)

## Custom Requests
If you have a color scheme that you would like me to create a Material theme for, I'd be happy to oblige. Simply [create a request](https://github.com/saadq/Materialize/issues/new) in the issues section and use the *theme request* label, and I'll try to get to it as soon as possible.

## Credits
**Thanks first and foremost to the original creator of the [Material](https://github.com/equinusocio/material-theme) theme, [equinusocio](https://github.com/equinusocio)**.

A big thanks also goes to the creators of the color schemes:

* [fnky](https://github.com/fnky) for creating [Behave](https://github.com/fnky/behave-theme)
* [kenwheeler](https://github.com/kenwheeler) for creating [Brogrammer](https://github.com/kenwheeler/brogrammer-theme)
* [thinkpixellab](https://github.com/thinkpixellab) for creating [Flatland](https://github.com/thinkpixellab/flatland)
* [voronianski](https://github.com/voronianski) for creating [Oceanic Next](https://github.com/voronianski/oceanic-next-color-scheme)
* [IceTimux](https://github.com/IceTimux) for creating [One Dark](https://github.com/IceTimux/one-dark-sublime-text-3-color-scheme)
* [ctf0](https://github.com/ctf0) for creating [Seti](https://github.com/ctf0/Seti_ST3)
* [TheBaronHimself](https://github.com/TheBaronHimself) for creating [Spaceblack](https://github.com/TheBaronHimself/Spaceblack)
* [kkga](https://github.com/kkga) for creating [the Spacegray themes](https://github.com/kkga/spacegray)
* [carlcalderon](https://github.com/carlcalderon) for creating [Stereokai](https://github.com/carlcalderon/sublime-color-schemes)
* [JacksonGariety](https://github.com/JacksonGariety) for creating [Toy Chest](https://github.com/JacksonGariety/Toy-Chest-Theme)
* [colinta](https://github.com/colinta) for creating [Zenburn](https://github.com/colinta/zenburn)
* [joeyfigaro](https://github.com/joeyfigaro) for creating [Glacier](https://github.com/shovelandsandbox/glacier-theme)

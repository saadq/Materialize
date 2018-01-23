# Materialize

## Deprecation Notice
This project is no longer under active development. Due to the fact that the original [Material Theme](https://github.com/equinusocio/material-theme) is no longer being developed and the fact that I switched from Sublime to [Atom](https://atom.io), Materialize will no longer be maintained. However, the project will continue to accept Pull Requests.

[![Packagecontrol total downloads](https://img.shields.io/packagecontrol/dt/Materialize.svg?style=flat-square)](https://packagecontrol.io/packages/Materialize/)
[![GitHub license](https://img.shields.io/github/license/saadq/materialize.svg?style=flat-square)](https://github.com/saadq/materialize/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/saadq/materialize.svg?style=flat-square)](https://github.com/saadq/materialize/issues?utf8=✓&q=is%3Aissue+is%3Aopen)
[![GitHub watchers](https://img.shields.io/github/watchers/saadq/materialize.svg?style=flat-square)](https://github.com/saadq/materialize/watchers)
[![GitHub stars](https://img.shields.io/github/stars/saadq/materialize.svg?style=flat-square)](https://github.com/saadq/materialize/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/saadq/materialize.svg?style=flat-square)](https://github.com/saadq/materialize/network)

Bringing [Material theme](https://github.com/equinusocio/material-theme) to the some of the most popular color schemes for [Sublime Text 3](https://www.sublimetext.com/3) and [Sublime Text 3 dev](https://www.sublimetext.com/3dev). Click [here](/Screenshots.md) to see some more screenshots.

![Material Spacegray](https://raw.githubusercontent.com/saadq/Materialize/master/screenshots/material-spacegray.png)

**Materialize** is based upon the [Material](https://github.com/equinusocio/material-theme) theme created by [@equinusocio](https://github.com/equinusocio) and the following themes / color schemes:

* [Augmented Reaction](https://github.com/ESWAT/augmentedreaction-theme) by [ESWAT](https://github.com/ESWAT)
* [Behave](https://github.com/fnky/behave-theme) by [@fnky](https://github.com/fnky)
* [Brogrammer](https://github.com/kenwheeler/brogrammer-theme) by [@kenwheeler](https://github.com/kenwheeler)
* [Cobalt](https://github.com/wesbos/cobalt2) by [@kyleknighted](https://github.com/kyleknighted)
* [Dracula](https://github.com/zenorocha/dracula-theme) by [@Zeno Rocha](http://zenorocha.com)
* [Facebook](https://github.com/mbixby/facebook-color-scheme) by [@mbixby](https://github.com/mbixby)
* [Flatland](https://github.com/thinkpixellab/flatland) by [@thinkpixellab](https://github.com/thinkpixellab)
* [Glacier](https://github.com/shovelandsandbox/glacier-theme) by [@joeyfigaro](https://github.com/joeyfigaro)
* [Monokai](http://www.monokai.nl/blog/2006/07/15/textmate-color-theme) by [@sublimehq](https://github.com/sublimehq), [Wimer Hazenberg](http://www.monokai.nl)
* [Oceanic Next](https://github.com/voronianski/oceanic-next-color-scheme) by [@voronianski](https://github.com/voronianski)
* [One Dark](https://github.com/IceTimux/one-dark-sublime-text-3-color-scheme) by [@IceTimux](https://github.com/IceTimux)
* [Primer Light](https://github.com/karelvuong/st-primer) by [@karelvuong](https://github.com/karelvuong)
* [Seti](https://github.com/ctf0/Seti_ST3) by [@ctf0](https://github.com/ctf0)
* [Solarized](https://github.com/altercation/solarized) by [@altercation](https://github.com/altercation/solarized)
* [Spaceblack](https://github.com/TheBaronHimself/Spaceblack) by [@TheBaronHimself](https://github.com/TheBaronHimself)
* [Spacegray](https://github.com/kkga/spacegray) by [@kkga](https://github.com/kkga)
* [Stereokai](https://github.com/carlcalderon/sublime-color-schemes) by [@carlcalderon](https://github.com/carlcalderon)
* [Toy Chest](https://github.com/JacksonGariety/Toy-Chest-Theme) by [@JacksonGariety](https://github.com/JacksonGariety)
* Twilight by [@sublimehq](https://github.com/sublimehq)
* [Vim Blackboard](https://github.com/lisposter/vim-blackboard) by [@lisposter](https://github.com/lisposter), [@nelstrom](https://github.com/nelstrom)
* [Zenburn](https://github.com/colinta/zenburn) by [@colinta](https://github.com/colinta)

## Installation

### Via Package Control

The easiest way to install is using [Will Bond](https://wbond.net)'s [Sublime Package Control](https://packagecontrol.io/installation), just search for `Materialize`.

1. Open Command Palette using menu item `Tools -> Command Palette...` (or <kbd>⇧</kbd><kbd>⌘</kbd><kbd>P</kbd> on Mac, <kbd>Ctrl</kbd><kbd>Shift ⇧</kbd><kbd>P</kbd> on Windows)
2. Choose `Package Control: Install Package`
3. Find `Materialize` and hit <kbd>Enter</kbd>

### Manually

You can also install the theme manually:

1. Download the [latest release](https://github.com/saadq/Materialize/releases/latest), extract and rename the folder to **"Materialize"**.
2. Move the folder inside your sublime Packages directory. **(Preferences > Browse packages...)**

## Activation

Activate the theme with the following preferences at  **(Preferences > Setting - User)**, based on the theme you want to use. If you wanted to use `Brogrammer` for example, you would need to do:

```json
    "color_scheme": "Packages/Materialize/schemes/Material Brogrammer.tmTheme",
    "theme": "Material Brogrammer.sublime-theme"
```

***Note*** : Remember to restart Sublime Text after activating the theme.

## Theme Addons
Be sure to check out [Materialize-Appbar](https://github.com/saadq/Materialize-Appbar) and [Materialize-White-Panels](https://github.com/saadq/Materialize-White-Panels) to add even more customization to your theme!

## Theme options

```json
    "material_theme_tabs_autowidth" : true,
    "material_theme_contrast_mode": true,
    "material_theme_compact_sidebar": true,
    "material_theme_compact_panel": true,
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
    "material_theme_accent_yellow": true,
    "material_theme_accent_indigo": true
```

## Recommended UI and font settings

Here are some recommendations for your user settings to make a better experience with the theme:

```json
    "always_show_minimap_viewport": true,
    "bold_folder_labels": true,
    "caret_extra_bottom": 2,
    "caret_extra_top": 2,
    "caret_extra_width": 2,
    "caret_style": "phase",
    "drag_text": false,
    "line_padding_bottom": 1,
    "line_padding_top": 1,
    "overlay_scroll_bars": "enabled"
```

Additionally, if you are on a Mac with Retina try:

```json
    "font_options": [ "gray_antialias" ]
```

or on a Windows PC with high resolution try:

```json
    "font_options": [ "directwrite" ]
```

## Known issues

Please see the issue [equinusocio/material-theme#67](https://github.com/equinusocio/material-theme/issues/67) if you cannot see the bottom panel (find/replace, rename, move, cannot see the box inputs in SidebarEnhancement, etc..). The quick fix is to just grab the border of the panel and move it like so:

![Drag the top edge](https://cloud.githubusercontent.com/assets/474329/8178894/a0dd09c0-1412-11e5-8ecf-f7f9ade439ae.gif)

## Custom requests

If you have a color scheme that you would like me to create a Material theme for, I'd be happy to oblige. Simply [create a new issue](https://github.com/saadq/Materialize/issues/new) and use the theme request template provided, and I'll try to get to it as soon as possible.

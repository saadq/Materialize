# How to Contribute
Everyone is welcome to contribute towards Materialize. Depending on the change you want to add, please follow the appropriate guide.

## Documentation Changes
When changing documentation, please make sure that any links you add are not broken. If you are updating the credits section, please make sure to include a link to both the color scheme itself as well as a link to the author.

## Adding a Theme
> This section will soon be updated once the tutorial for creating a Material theme has been finished.

Before adding a theme, make sure that the color scheme you are using has an open source license (please message the author of the color scheme if you are unsure). After that, make sure you stay consistent with the format of a theme. Assuming that the theme we wanted to add was Material Monokai, we would want to create the following: 

* A theme file (themes/Material Monokai.sublime-theme)
* A color scheme file (schemes/Material Monokai.tmTheme)
* An assets folder with appropriately colored assets for the theme (assets/monokai/)
* A widgets folder (widgets/monokai/)

Be sure to update the credits page in the README as well as updating the `themes.json` with the new theme (make sure it remains in alphabetical order).

## Changing existing themes
It is important that any change you make to a theme is consistent across all themes. It's generally advised to use a script when making changes in order to ensure consistency.

Here is an example script written in Node that will change the sidebar padding for every theme:

```javascript
const fs = require('fs')

// Old setting for each theme
const currentPadding = `
      "class": "sidebar_tree",
      "row_padding": [24, 8],
`

// New setting for each theme
const newPadding = `
      "class": "sidebar_tree",
      "row_padding": [24, 12],
`

// Loop through each file in the themes folder, 
// replace the padding, and then save the file
fs.readdir('./themes', (_, files) => {
  files.forEach(file => {
    const filePath = `./themes/${file}`
    fs.readFile(filePath, 'utf8', (_, data) => {
      const newData = data.replace(currentPadding, newPadding)
      fs.writeFile(filePath, newData)
    })
  })
})
```

## Creating a Theme Request
When making a theme request, make sure to do the following:

1. Make sure the theme doesn't already exist.
2. Make sure that the color scheme you are requesting has an open source license.
3. Provide a link to the color scheme you want a theme for.

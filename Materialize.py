import re
import sublime
import sublime_plugin

class ActivateMaterializeThemeCommand(sublime_plugin.TextCommand):
    def run(self, action):

        names = [
            "Material Augmented Reaction",
            "Material Behave",
            "Material Brogrammer",
            "Material Cobalt",
            "Material Dracula",
            "Material Facebook",
            "Material Firewatch",
            "Material Flatland",
            "Material Glacier",
            "Material Monokai Soda",
            "Material Monokai",
            "Material Oceanic Next",
            "Material One Dark",
            "Material Primer Light",
            "Material Seti",
            "Material Solarized Dark",
            "Material Solarized Light",
            "Material Spaceblack Ocenic",
            "Material Spaceblack",
            "Material Spacegray Eighties",
            "Material Spacegray Light",
            "Material Spacegray Mocha",
            "Material Spacegray",
            "Material Stereokai",
            "Material Toy Chest",
            "Material Twilight",
            "Material Vim Blackboard",
            "Material Zenburn",
        ]
        self.themes = [
            "Material Augmented Reaction.sublime-theme",
            "Material Behave.sublime-theme",
            "Material Brogrammer.sublime-theme",
            "Material Cobalt.sublime-theme",
            "Material Dracula.sublime-theme",
            "Material Facebook.sublime-theme",
            "Material Firewatch.sublime-theme",
            "Material Flatland.sublime-theme",
            "Material Glacier.sublime-theme",
            "Material Monokai Soda.sublime-theme",
            "Material Monokai.sublime-theme",
            "Material Oceanic Next.sublime-theme",
            "Material One Dark.sublime-theme",
            "Material Primer Light.sublime-theme",
            "Material Seti.sublime-theme",
            "Material Solarized Dark.sublime-theme",
            "Material Solarized Light.sublime-theme",
            "Material Spaceblack.sublime-theme",
            "Material Spaceblack.sublime-theme",
            "Material Spacegray Eighties.sublime-theme",
            "Material Spacegray Light.sublime-theme",
            "Material Spacegray Mocha.sublime-theme",
            "Material Spacegray.sublime-theme",
            "Material Stereokai.sublime-theme",
            "Material Toy Chest.sublime-theme",
            "Material Twilight.sublime-theme",
            "Material Vim Blackboard.sublime-theme",
            "Material Zenburn.sublime-theme",
        ]
        self.schemes = [
            "Packages/Materialize/schemes/Material Augmented Reaction.tmTheme",
            "Packages/Materialize/schemes/Material Behave.tmTheme",
            "Packages/Materialize/schemes/Material Brogrammer.tmTheme",
            "Packages/Materialize/schemes/Material Cobalt.tmTheme",
            "Packages/Materialize/schemes/Material Dracula.tmTheme",
            "Packages/Materialize/schemes/Material Facebook.tmTheme",
            "Packages/Materialize/schemes/Material Firewatch.tmTheme",
            "Packages/Materialize/schemes/Material Flatland.tmTheme",
            "Packages/Materialize/schemes/Material Glacier.tmTheme",
            "Packages/Materialize/schemes/Material Monokai Soda.tmTheme",
            "Packages/Materialize/schemes/Material Monokai.tmTheme",
            "Packages/Materialize/schemes/Material Oceanic Next.tmTheme",
            "Packages/Materialize/schemes/Material One Dark.tmTheme",
            "Packages/Materialize/schemes/Material Primer Light.tmTheme",
            "Packages/Materialize/schemes/Material Seti.tmTheme",
            "Packages/Materialize/schemes/Material Solarized Dark.tmTheme",
            "Packages/Materialize/schemes/Material Solarized Light.tmTheme",
            "Packages/Materialize/schemes/Material Spaceblack Oceanic.tmTheme",
            "Packages/Materialize/schemes/Material Spaceblack.tmTheme",
            "Packages/Materialize/schemes/Material Spacegray Eighties.tmTheme",
            "Packages/Materialize/schemes/Material Spacegray Light.tmTheme",
            "Packages/Materialize/schemes/Material Spacegray Mocha.tmTheme",
            "Packages/Materialize/schemes/Material Spacegray.tmTheme",
            "Packages/Materialize/schemes/Material Stereokai.tmTheme",
            "Packages/Materialize/schemes/Material Toy Chest.tmTheme",
            "Packages/Materialize/schemes/Material Twilight.tmTheme",
            "Packages/Materialize/schemes/Material Vim Blackboard.tmTheme",
            "Packages/Materialize/schemes/Material Zenburn.tmTheme",
        ]

        self.view.window().show_quick_panel(names, self.on_done, on_highlight=self.on_highlighted)

    def on_done(self, index):
        scheme = self.schemes[index]
        theme = self.themes[index]
        self.set_scheme(scheme)
        self.set_theme(theme)
        self.save_settings(theme)

    def on_highlighted(self, index):
        scheme = self.schemes[index]
        theme = self.themes[index]
        self.set_scheme(scheme)
        self.set_theme(theme)

    def set_scheme(self, scheme):
        self.get_settings().set('color_scheme', scheme)

    def set_theme(self, theme):
        self.get_settings().set('theme', theme)

    def get_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')

    def save_settings(self, theme):
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('Materialize: ' + theme)
        print('')
        print('[Materialize] ' +  theme)
        print('')

# Welcome to jQueryDocs

jQueryDocs is a Sublime Text 3 Package which shows a selected jQuery Function on [api.jquery.com](http://api.jquery.com/).

***

### How to Install

#### Via Package Control

The easiest way to install is using [Sublime Package Control](https://sublime.wbond.net), where you can find this package by searching for `jQueryDocs`.

1. Open Command Palette using menu item `Tools -> Command Palette...` (<kbd>⇧</kbd><kbd>⌘</kbd><kbd>P</kbd> on Mac)
2. Choose `Package Control: Install Package`
3. Find `jQueryDocs` and hit <kbd>Enter</kbd>

#### Manual

You can also install the package manually:

1. [Download the .zip](https://github.com/Miw0/jQueryDocs/archive/master.zip)
2. Unzip and rename the folder to `jQueryDocs`
3. Copy the folder into `Packages` directory, which you can find using the menu item `Sublime Text -> Preferences -> Browse Packages...`

***

### How to use

Select a jQuery Function (without braces, dot or semicolon) and press the assigned key combination (Default <kbd>ALT</kbd>+<kbd>J</kbd>).
A new window will be created in your default browser loading [api.jquery.com](http://api.jquery.com/) with the
corresponding documentation page for the selected function.

#### Change default key binding

You can change the default key combination by including this in your user key binding settings

    { "keys": ["alt+j"], "command": "jquery_docs" }

***

### Thanks

jQueryDocs was created and is maintained by [Michael Worm](https://github.com/Miw0).

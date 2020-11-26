""" Configuration file for jupyter-qtconsole.


"""

# Set to display confirmation dialog on exit. You can always use 'exit' or
# 'quit', to force a direct exit without any confirmation.
c.JupyterConsoleApp.confirm_exit = False

# Answer yes to any prompts.
c.JupyterApp.answer_yes = False

# Whether to display a banner upon starting the QtConsole.
c.JupyterQtConsoleApp.display_banner = False

# Start the console window with the menu bar hidden.
c.JupyterQtConsoleApp.hide_menubar = True

# The maximum number of lines of text before truncation. Specifying a non-
#  positive number disables text truncation (not recommended).
# c.ConsoleWidget.buffer_size = 500

# Whether to automatically execute on syntactically complete input.
# If False, Shift-Enter is required to submit each execution. Disabling this is
# mainly useful for non-Python kernels, where the completion check would be
# wrong.
# c.ConsoleWidget.execute_on_complete_input = True

# The font family to use for the console. On OSX this defaults to Monaco, on
# Windows the default is Consolas with fallback of Courier, and on other
# platforms the default is Monospace.
# c.ConsoleWidget.font_family = ''

# The font size. If unconfigured, Qt will be entrusted with the size of the
# font.
c.ConsoleWidget.font_size = 13

# The visibility of the scrollar. If False then the scrollbar will be invisible
c.ConsoleWidget.scrollbar_visibility = False

# A CSS stylesheet. The stylesheet can contain classes for:
#      1. Qt: QPlainTextEdit, QFrame, QWidget, etc
#      2. Pygments: .c, .k, .o, etc. (see PygmentsHighlighter)
#      3. QtConsole: .error, .in-prompt, .out-prompt, etc
# c.JupyterWidget.style_sheet = ''

# If not empty, use this Pygments style for syntax highlighting. Otherwise, the
# style sheet is queried for Pygments style information.
c.JupyterWidget.syntax_style = 'stata-dark'

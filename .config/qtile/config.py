# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

colors = [
        "#282c34", "#282c34",   # black     -> 0
        "#e06c75", "#e06c75",   # red       -> 2
        "#98c379", "#98c379",   # green     -> 4
        "#e5c07b", "#e5c07b",   # yellow    -> 6
        "#61afef", "#61afef",   # blue      -> 8
        "#c678dd", "#c678dd",   # purp      -> 10
        "#56b6c2", "#56b6c2",   # cyan      -> 12
        "#abb2bf", "#abb2bf",   # white     -> 14
        ]

fonts = [
        "Caskaydia Cove Nerd Font Complete",        # default
        "Ubuntu Bold",                              # bold
        "Caskaydia Cove Nerd Font Complete Mono",   # console
        ]

mod = "mod1"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # APPS
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "1", lazy.spawn("firefox"), desc="Launch firefox"),

    # Toggle between different layouts as deined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Sound keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume 0 +2%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume 0 -2%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle"), desc="Mute master"),
]

# GROUPS
groups = []
group_names = ["a", "s", "d", "f", "g"]
group_labels = ["WWW", "DEV", "SYS", "DOC", "MUS"]
group_layouts = ["max", "monadtall", "monadtall", "monadtall", "max"]

for i in range(len(group_names)):
    groups.append(Group(
        name=group_names[i],
        label=group_labels[i],
        layout=group_layouts[i].lower()
        ))

for i in groups:
    keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),

            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
        ])

# LAYOUTS
layouts = [
    #layout.Columns(border_focus=colors[12], border_width=2, margin= 4),
    layout.Max(),
    layout.Matrix(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.MonadTall(border_normal=colors[0], border_focus=colors[12], border_width = 1, margin = 4),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# WIDGETS 
widget_defaults = dict(
        font=fonts[0],
        fontsize=10,
        padding=5,
        )

extension_defaults = widget_defaults.copy()

def barWidgets():
    return [
           widget.Sep(
               lineWidth = 0, 
               padding = 6, 
               foreground = colors[0],
               background = colors[0]
               ),
           widget.GroupBox(
               font=fonts[1], 
               fontsize = 9, 
               margin_y = 3,
               margin_x = 0, 
               padding = 5,
               border_width = 1, 
               active = colors[14], 
               inactive = colors[14],
               rounded = True,
               highlight_method = "text", 
               this_current_screen_border = colors[2], 
               this_screen_border = colors[0],
               other_current_screen_border = colors[0],
               other_screen_border = colors[0],
               foreground = colors[14],
               background = colors[0]
               ),
           widget.Sep(
               lineWidth = 0, 
               padding = 6, 
               foreground = colors[0],
               background = colors[0]
               ),
           widget.Prompt(
               font = fonts[2],
               padding = 10,
               foreground = colors[6],
               background = colors[0]
               ),
           widget.WindowName(
               fontsize = 9,
               foreground = colors[14],
               background = colors[0],
               padding = 5
               ),
           widget.TextBox(
               text='',
               #text='',
               background = colors[0],
               foreground = colors[6],
               padding = 0,
               fontsize = 24 
               ),
           widget.CurrentLayout(
                   font = fonts[1],
                   background = colors[6],
                   foreground = colors[0]
                   ),
           widget.TextBox(
               text='',
               background = colors[6],
               foreground = colors[2],
               padding = 0,
               fontsize = 24 
               ),
           widget.TextBox(
               "Vol: ",
               font = fonts[1],
               mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
               background = colors[2],
               foreground = colors[0]
               ),
           widget.Volume(
               fmt='{}',
               font = fonts[1],
               volume_down_command = "pactl -- set-sink-volume 0 -2%",
               volume_up_command = "pactl -- set-sink-volume 0 +2%",
               mute_command = "pactl set-sink-mute 0 toggle",
               #get_volume_command = 
               background = colors[2],
               foreground = colors[0]
               ),
           widget.TextBox(
               text='',
               background = colors[2],
               foreground = colors[10],
               padding = 0,
               fontsize = 24 
               ),
           widget.Systray(
                background = colors[10],
                foreground = colors[0]
                ),
           widget.Sep(
               lineWidth = 0, 
               padding = 6, 
               foreground = colors[10],
               background = colors[10]
               ),
           widget.Image(
                filename="~/.config/qtile/icons/calendar.svg",
                margin_y = 3,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty")},
                background = colors[10],
                foreground = colors[0]
            ),
           widget.Clock(
               format='%d/%m/%Y %H:%M', 
               font = fonts[1],
               foreground = colors[0],
               background = colors[10]
               ),
           #widget.QuickExit()
           ]

# SCREENS
screens = [
    Screen(
        wallpaper='~/Imágenes/background_1.png',
        wallpaper_mode='stretch',
        top=bar.Bar(
            barWidgets(),
            18,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
 

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess


@hook.subscribe.startup_once
def screen_fix():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


gruvbox_colors = {
    "dark0_hard": "#1d2021",
    "dark0": "#282828",
    "dark0_soft": "#32302f",
    "dark1": "#3c3836",
    "dark2": "#504945",
    "dark3": "#665c54",
    "dark4": "#7c6f64",
    "dark4_256": "#7c6f64",
    "gray_245": "#928374",
    "gray_244": "#928374",
    "light0_hard": "#f9f5d7",
    "light0": "#fbf1c7",
    "light0_soft": "#f2e5bc",
    "light1": "#ebdbb2",
    "light2": "#d5c4a1",
    "light3": "#bdae93",
    "light4": "#a89984",
    "light4_256": "#a89984",
    "bright_red": "#fb4934",
    "bright_green": "#b8bb26",
    "bright_yellow": "#fabd2f",
    "bright_blue": "#83a598",
    "bright_purple": "#d3869b",
    "bright_aqua": "#8ec07c",
    "bright_orange": "#fe8019",
    "neutral_yellow": "#d79921",
    "neutral_blue": "#458588",
    "neutral_purple": "#b16286",
    "neutral_aqua": "#689d6a",
    "neutral_orange": "#d65d0e",
    "faded_red": "#9d0006",
    "faded_green": "#79740e",
    "faded_yellow": "#b57614",
    "faded_blue": "#076678",
    "faded_purple": "#8f3f71",
    "faded_aqua": "#427b58",
    "faded_orange": "#af3a03",
}
mod = "mod4"
terminal = "alacritty"

keys = [
    ########################
    # WINDOWS SWITCHING
    ########################
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    ########################
    # TERMINAL
    ########################
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

########################
# GROUPS
########################
group_labels = ["", "", "", "", "阮", "", "", "", ""]
groups = [Group(i) for i in group_labels]

for group_key, group_label in enumerate(group_labels):
    group_key += 1
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(group_key),
                lazy.group[group_label].toscreen(),
                desc=f"Switch to group {group_label}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(group_key),
                lazy.window.togroup(group_label, switch_group=True),
                desc=f"Switch to & move focused window to group {group_label}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(border_focus="#A89984", border_width=2, margin=10),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="CaskadyaCove Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=10,
                    background=gruvbox_colors["faded_orange"],
                ),
                widget.CurrentLayout(
                    background=gruvbox_colors["faded_orange"],
                    font="CaskaydiaCove Nerd Font",
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=gruvbox_colors["faded_orange"],
                    background=gruvbox_colors["dark0_hard"],
                ),
                widget.GroupBox(
                    highlight_method="line",
                    foreground=gruvbox_colors["light0_soft"],
                    font="CaskaydiaCove Nerd Font",
                    background=gruvbox_colors["dark0_hard"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=gruvbox_colors["dark0_hard"],
                    background=gruvbox_colors["dark0_soft"],
                ),
                widget.Prompt(
                    foreground=gruvbox_colors["light0_soft"],
                    background=gruvbox_colors["dark0_soft"],
                    ),
                widget.WindowName(
                    foreground=gruvbox_colors["light0_soft"],
                    background=gruvbox_colors["dark0_soft"],
                    font="CaskaydiaCove Nerd Font",
                    ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=gruvbox_colors["dark0_soft"],
                    background=gruvbox_colors["faded_yellow"],
                    ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    background=gruvbox_colors["faded_yellow"],
                    font="CaskaydiaCove Nerd Font",
                    ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=gruvbox_colors["faded_yellow"],
                    background=gruvbox_colors["faded_red"],
                    ),
                widget.QuickExit(
                    default_text="",
                    countdown_format='{}',
                    font="CaskaydiaCove Nerd Font",
                    background=gruvbox_colors["faded_red"],
                    ),
                widget.Spacer(
                    length=13,
                    background=gruvbox_colors["faded_red"],
                    ),
            ],
            24,
            margin=[10, 10, 0, 10],
            opacity=1,
            background=gruvbox_colors["dark0_hard"]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
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

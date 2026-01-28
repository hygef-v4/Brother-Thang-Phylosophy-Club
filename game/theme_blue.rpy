init -1 python:
    # Shift Hue from Pink (~330) to Blue (~200) -> -130 degrees
    blue_tint = im.matrix.hue(-130)

    # Define as variables for use in Frame/Image constructors
    mw_textbox = im.MatrixColor("gui/textbox.png", blue_tint)
    mw_namebox = im.MatrixColor("gui/namebox.png", blue_tint)
    menu_bg = im.MatrixColor("gui/menu_bg.png", blue_tint)
    game_menu_bg = im.MatrixColor("gui/game_menu.png", blue_tint)
    
    # Overlay images
    overlay_game_menu = im.MatrixColor("gui/overlay/game_menu.png", blue_tint)
    overlay_confirm = im.MatrixColor("gui/overlay/confirm.png", blue_tint)
    
    # Generic Frame
    mw_frame = im.MatrixColor("gui/frame.png", blue_tint)
    
    # Bar images
    mw_bar_left = im.MatrixColor("gui/bar/left.png", blue_tint)
    # Use a lighter/desaturated version for the empty track (right), or just hue shift differently
    # Existing tint might be making it too dark/same color as left.
    # Let's try desaturating the original right bar and tinting it slightly blue but keeping brightness
    mw_bar_right = im.MatrixColor("gui/bar/right.png", im.matrix.desaturate() * im.matrix.tint(0.6, 0.8, 1.0))

# Keep image tags for 'add' statements if needed, or just use the variables.
image menu_bg = menu_bg
image game_menu_bg = game_menu_bg
image overlay_game_menu = overlay_game_menu


# Button backgrounds (if needed, though gui.rpy largely handles colors, these might be image based)
image choice_idle = im.MatrixColor("gui/button/choice_idle_background.png", blue_tint)
image choice_hover = im.MatrixColor("gui/button/choice_hover_background.png", blue_tint)
image slot_idle = im.MatrixColor("gui/button/slot_idle_background.png", blue_tint)
image slot_hover = im.MatrixColor("gui/button/slot_hover_background.png", blue_tint)

# Updates to definitions that might rely on string paths in screens.rpy
# We will use these image tags in screens.rpy

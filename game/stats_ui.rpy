# ================================================
# STATS UI SCREEN - Hiển thị stats trên màn hình
# ================================================

# Stats sidebar luôn hiển thị khi chơi
screen stats_display():
    # Style tag
    tag stats_ui
    zorder 50  # Lower than quick_menu (which is zorder 100)
    
    # Main container - ultra minimal glassmorphism
    frame:
        xalign 0.985
        yalign 0.03
        xsize 145  # More compact
        ymaximum 380  # Increased to fit new stats
        # Slightly more visible glassmorphism
        background Solid("#ffffff12")  # A bit more visible
        padding (6, 6)
        
        vbox:
            spacing 5
            
            # Very subtle header
            text "Thông số":
                size 12
                xalign 0.5
                color "#ffffff"  # Pure white, more visible
                outlines [(1, "#00000040", 0, 1)]  # Slightly stronger shadow
            
            null height 2
            
            # Day - minimal
            hbox:
                spacing 3
                text "Ngày [current_day] - [GameConfig.TIME_SLOTS[current_time_slot-1]]" size 9 color "#ffffffdd" outlines [(1, "#00000030", 0, 1)]
            
            null height 4
            
            # Stats - ultra thin, short bars
            # Học tập
            vbox:
                spacing 1
                text "Học tập" size 9 color "#ffffffdd" outlines [(1, "#00000035", 0, 1)]
                bar:
                    value stats.hoc_tap
                    range 100
                    xsize 120
                    ysize 4
                    left_bar Solid("#90caf9dd")
                    right_bar Solid("#00000000")
                    thumb Null()
                    left_gutter 0
                    right_gutter 0
                text "[stats.hoc_tap]" size 8 color "#ffffffcc" outlines [(1, "#00000030", 0, 1)]
            
            # Sức khỏe
            vbox:
                spacing 1
                text "Sức khỏe" size 9 color "#ffffffdd" outlines [(1, "#00000035", 0, 1)]
                bar:
                    value stats.doi_song
                    range 100
                    xsize 120
                    ysize 4
                    left_bar Solid("#80cbc4dd")
                    right_bar Solid("#00000000")
                    thumb Null()
                    left_gutter 0
                    right_gutter 0
                text "[stats.doi_song]" size 8 color "#ffffffcc" outlines [(1, "#00000030", 0, 1)]
            
            # Vũ Hải Nữ
            vbox:
                spacing 1
                text "Vũ Hải Nữ" size 9 color "#ffffffdd" outlines [(1, "#00000035", 0, 1)]
                bar:
                    value stats.rel_hainu
                    range 100
                    xsize 120
                    ysize 4
                    left_bar Solid("#f48fb1dd")  # Pink
                    right_bar Solid("#00000000")
                    thumb Null()
                    left_gutter 0
                    right_gutter 0
                text "[stats.rel_hainu]" size 8 color "#ffffffcc" outlines [(1, "#00000030", 0, 1)]
            
            # Võ Minh Xỉu
            vbox:
                spacing 1
                text "Võ Minh Xỉu" size 9 color "#ffffffdd" outlines [(1, "#00000035", 0, 1)]
                bar:
                    value stats.rel_xiu
                    range 100
                    xsize 120
                    ysize 4
                    left_bar Solid("#ffcc80dd")  # Orange
                    right_bar Solid("#00000000")
                    thumb Null()
                    left_gutter 0
                    right_gutter 0
                text "[stats.rel_xiu]" size 8 color "#ffffffcc" outlines [(1, "#00000030", 0, 1)]
            
            # Tiền - minimal
            vbox:
                spacing 1
                text "Tiền" size 9 color "#ffffffdd" outlines [(1, "#00000035", 0, 1)]
                text "[stats.tien:,]₫" size 8 color "#fff9c4" outlines [(1, "#00000035", 0, 1)]


# Coming Soon screen
screen coming_soon():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        background "#000000dd"
        padding (30, 30)
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "COMING SOON":
                size 40 
                xalign 0.5 
                color "#ffdd00" 
                bold True
                font "DejaVuSans-Bold.ttf"
            
            null height 20
            
            text "Cảm ơn bạn đã chơi!":
                size 24 
                xalign 0.5 
                color "#ffffff"
                font "DejaVuSans.ttf"
            
            null height 20
            
            text "Các ngày tiếp theo sẽ được cập nhật sớm!":
                size 18 
                xalign 0.5 
                color "#aaaaaa"
                font "DejaVuSans.ttf"
            
            null height 30
            
            textbutton "Về Menu Chính":
                xalign 0.5
                action MainMenu(confirm=False)
                text_font "DejaVuSans-Bold.ttf"
                text_size 24
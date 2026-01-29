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
        ymaximum 280  # Much shorter without relationships
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
                text "Ngày" size 9 color "#ffffffdd" outlines [(1, "#00000030", 0, 1)]
                text "[current_day]" size 10 bold True color "#e3f2fd" outlines [(1, "#00000040", 0, 1)]
            
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
                    left_gutter 0
                    right_gutter 0
                text "[stats.doi_song]" size 8 color "#ffffffcc" outlines [(1, "#00000030", 0, 1)]
            
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
            
            text "Ngày 1 của Chapter 1: EIKASIA đã hoàn thành.":
                size 18 
                xalign 0.5 
                color "#aaaaaa"
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
                action Return()
                text_font "DejaVuSans-Bold.ttf"
                text_size 24

# Coming Soon Chapter 3 screen
screen coming_soon_ch3():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        background "#000000dd"
        padding (30, 30)
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "CHAPTER 2: PISTIS":
                size 32
                xalign 0.5 
                color "#ff6b9d" 
                bold True
                font "DejaVuSans-Bold.ttf"
            
            text "HOÀN THÀNH!":
                size 40 
                xalign 0.5 
                color "#00ff88" 
                bold True
                font "DejaVuSans-Bold.ttf"
            
            null height 20
            
            text "Cảm ơn bạn đã chơi!":
                size 24 
                xalign 0.5 
                color "#ffffff"
                font "DejaVuSans.ttf"
            
            text "Bạn đã hoàn thành Chapter 2: PISTIS (Niềm Tin).":
                size 18 
                xalign 0.5 
                color "#aaaaaa"
                font "DejaVuSans.ttf"
            
            text "Đã học được về ngụ ngôn Hang động của Plato và con đường từ Eikasia đến Pistis.":
                size 16 
                xalign 0.5 
                color "#aaaaaa"
                font "DejaVuSans.ttf"
            
            null height 30
            
            text "COMING SOON":
                size 36 
                xalign 0.5 
                color "#ffdd00" 
                bold True
                font "DejaVuSans-Bold.ttf"
            
            text "Chapter 3: DIANOIA (Lý Trí)":
                size 24 
                xalign 0.5 
                color "#33ccff"
                bold True
                font "DejaVuSans-Bold.ttf"
            
            text "Những ngày tiếp theo với các nhân vật...":
                size 16 
                xalign 0.5 
                color "#aaaaaa"
                font "DejaVuSans.ttf"
            
            null height 30
            
            textbutton "Về Menu Chính":
                xalign 0.5
                action Return()
                text_font "DejaVuSans-Bold.ttf"
                text_size 24


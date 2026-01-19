# ================================================
# STATS UI SCREEN - Hiển thị stats trên màn hình
# ================================================

# Stats sidebar luôn hiển thị khi chơi
screen stats_display():
    # Style tag
    tag stats_ui
    zorder 100
    
    # Main container
    frame:
        xalign 0.98
        yalign 0.02
        xsize 250
        background Frame("gui/frame.png", 10, 10)
        padding (15, 15)
        
        vbox:
            spacing 10
            
            # Header
            text "STATS" size 24 bold True xalign 0.5 color "#ffffff"
            
            null height 5
            
            # Ngày
            hbox:
                spacing 5
                text "Ngày:" size 18 color "#aaaaaa"
                text "[current_day]" size 18 bold True color "#ffff00"
            
            null height 10
            
            # Học tập
            vbox:
                spacing 3
                text "Học tập" size 16 color "#00ccff"
                bar:
                    value stats.hoc_tap
                    range 100
                    xsize 220
                    left_bar Frame("gui/bar/left.png", 4, 4)
                    right_bar Frame("gui/bar/right.png", 4, 4)
                text "[stats.hoc_tap]/100" size 14 color "#ffffff"
            
            # Đời sống
            vbox:
                spacing 3
                text "Đời sống" size 16 color "#00ff88"
                bar:
                    value stats.doi_song
                    range 100
                    xsize 220
                    left_bar Frame("gui/bar/left.png", 4, 4)
                    right_bar Frame("gui/bar/right.png", 4, 4)
                text "[stats.doi_song]/100" size 14 color "#ffffff"
            
            # Tiền
            vbox:
                spacing 3
                text "Tiền" size 16 color "#ffdd00"
                text "{size=14}[stats.tien:,] VNĐ{/size}" color "#ffffff"
            
            null height 10
            
            # Tình cảm (chỉ hiển thị nếu đã gặp)
            if stats.met_ischyros:
                vbox:
                    spacing 2
                    text "❤ Ischyros" size 14 color "#ff6b9d"
                    bar:
                        value stats.rel_ischyros
                        range 100
                        xsize 220
                        left_bar Frame("gui/bar/left.png", 4, 4)
                        right_bar Frame("gui/bar/right.png", 4, 4)
            
            if stats.met_huong:
                vbox:
                    spacing 2
                    text "❤ Hương" size 14 color "#33ccff"
                    bar:
                        value stats.rel_huong
                        range 100
                        xsize 220
                        left_bar Frame("gui/bar/left.png", 4, 4)
                        right_bar Frame("gui/bar/right.png", 4, 4)
            
            if stats.met_hainu:
                vbox:
                    spacing 2
                    text "❤ Hải Nữ" size 14 color "#9966ff"
                    bar:
                        value stats.rel_hainu
                        range 100
                        xsize 220
                        left_bar Frame("gui/bar/left.png", 4, 4)
                        right_bar Frame("gui/bar/right.png", 4, 4)
            
            if stats.met_xiu:
                vbox:
                    spacing 2
                    text "❤ Xỉu" size 14 color "#ffcc00"
                    bar:
                        value stats.rel_xiu
                        range 100
                        xsize 220
                        left_bar Frame("gui/bar/left.png", 4, 4)
                        right_bar Frame("gui/bar/right.png", 4, 4)

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

screen achievements():
    tag menu
    use game_menu(_("Thành Tựu"), scroll="viewport"):
        style_prefix "about"
        vbox:
            spacing 20
            
            # 1. Fascist Ending
            if "fascist" in persistent.unlocked_endings:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#ff000033"), gui.frame_borders)
                    vbox:
                        text "{b}SECRET ENDING: HOẠ SĨ NGƯỜI ÁO{/b}" color "#ff0000" size 30
                        text "Triết lý: Từ Bỏ Dianoia (Tư Duy Phản Biện)" color "#ffffff"
                        text "Bạn đã giao nộp lý trí cho quyền lực. Thế giới chìm trong bóng tối." size 18 color "#aaaaaa"
            else:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#333333"), gui.frame_borders)
                    text "???" color "#aaaaaa" size 30

            # 2. Subjective Active (Xiu Route)
            if "subjective_active" in persistent.unlocked_endings:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#ff66aa33"), gui.frame_borders)
                    vbox:
                        text "{b}HAPPY ENDING: XIU ROUTE{/b}" color "#ff66aa" size 30
                        text "Triết lý: Hedonism (Chủ Nghĩa Hưởng Lạc)" color "#ffffff"
                        text "Bạn chọn chiếc hang êm ái thay vì đối mặt thực tại." size 18 color "#aaaaaa"
            else:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#333333"), gui.frame_borders)
                    text "???" color "#aaaaaa" size 30

            # 3. Subjective Passive (Bad End)
            if "subjective_passive" in persistent.unlocked_endings:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#aa000033"), gui.frame_borders)
                    vbox:
                        text "{b}BAD ENDING: VÒNG LẶP HƯ VÔ{/b}" color "#aa0000" size 30
                        text "Triết lý: Nihilism (Thuyết Hư Vô)" color "#ffffff"
                        text "Bạn hoài nghi tất cả sự tồn tại và mất đi khả năng thay đổi nó." size 18 color "#aaaaaa"
            else:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#333333"), gui.frame_borders)
                    text "???" color "#aaaaaa" size 30

            # 4. Metaphysical (Normal End)
            if "metaphysical" in persistent.unlocked_endings:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#ffffff33"), gui.frame_borders)
                    vbox:
                        text "{b}NORMAL ENDING: THỰC TẠI CHẤP NHẬN{/b}" color "#ffffff" size 30
                        text "Triết lý: Duy Vật Siêu Hình (Thụ Động)" color "#ffffff"
                        text "Bạn nhìn thấy thực tế nhưng cúi đầu trước nó. Bạn an toàn nhưng không tự do." size 18 color "#aaaaaa"
            else:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#333333"), gui.frame_borders)
                    text "???" color "#aaaaaa" size 30

            # 5. Dialectical (True End)
            if "dialectical" in persistent.unlocked_endings:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#ffdd0033"), gui.frame_borders)
                    vbox:
                        text "{b}TRUE ENDING: HÀNH TRÌNH TRIẾT HỌC{/b}" color "#ffdd00" size 30
                        text "Trạng thái: Noesis (Giác Ngộ)" color "#ffffff"
                        text "Bạn dùng mâu thuẫn để phát triển. Đây chính là Tự Do Đích Thực." size 18 color "#aaaaaa"
            else:
                frame:
                    xfill True
                    padding (20, 20)
                    background Frame(Solid("#333333"), gui.frame_borders)
                    text "???" color "#aaaaaa" size 30

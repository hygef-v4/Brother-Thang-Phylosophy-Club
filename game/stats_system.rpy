# ================================================
# STATS SYSTEM - Brother Thang Philosophy Club
# ================================================

init -1 python:
    class StatsManager:
        """Quản lý tất cả stats của game"""
        
        def __init__(self):
            # Core stats
            self.hoc_tap = GameConfig.STAT_INITIAL_HOC_TAP
            self.doi_song = GameConfig.STAT_INITIAL_DOI_SONG
            self.tien = GameConfig.STAT_INITIAL_TIEN
            
            # Relationship scores
            # self.rel_ischyros = GameConfig.REL_INITIAL_ISCHYROS  # REMOVED - character no longer exists
            self.rel_huong = GameConfig.REL_INITIAL_HUONG
            self.rel_hainu = GameConfig.REL_INITIAL_HAINU
            self.rel_xiu = GameConfig.REL_INITIAL_XIU
            
            # Flags
            self.dad_cutoff = False  # Bố cắt trợ cấp
            # self.met_ischyros = False  # REMOVED
            self.met_huong = False
            self.met_hainu = False
            self.met_xiu = False
            
        def clamp(self, value, min_val, max_val):
            """Clamp value giữa min và max"""
            return max(min_val, min(max_val, value))
        
        def modify_hoc_tap(self, amount):
            """Thay đổi học tập"""
            self.hoc_tap = self.clamp(
                self.hoc_tap + amount,
                GameConfig.STAT_MIN,
                GameConfig.STAT_MAX
            )
            return amount
        
        def modify_doi_song(self, amount):
            """Thay đổi đời sống"""
            self.doi_song = self.clamp(
                self.doi_song + amount,
                GameConfig.STAT_MIN,
                GameConfig.STAT_MAX
            )
            return amount
        
        def modify_tien(self, amount):
            """Thay đổi tiền"""
            self.tien = max(0, self.tien + amount)
            return amount
        
        def modify_relationship(self, char_name, amount, stat_multiplier=1.0):
            """
            Thay đổi tình cảm với nhân vật
            char_name: "huong", "hainu", "xiu" (ischyros removed)
            amount: số điểm thay đổi
            stat_multiplier: nhân với stats (Hải Nữ thích học tập, Hương thích đời sống)
            """
            final_amount = amount * stat_multiplier
            
            # Note: ischyros case removed
            if char_name == "huong":
                self.rel_huong = self.clamp(
                    self.rel_huong + final_amount,
                    GameConfig.REL_MIN,
                    GameConfig.REL_MAX
                )
            elif char_name == "hainu":
                self.rel_hainu = self.clamp(
                    self.rel_hainu + final_amount,
                    GameConfig.REL_MIN,
                    GameConfig.REL_MAX
                )
            elif char_name == "xiu":
                self.rel_xiu = self.clamp(
                    self.rel_xiu + final_amount,
                    GameConfig.REL_MIN,
                    GameConfig.REL_MAX
                )
            
            return final_amount

        def get_relationship(self, char_name):
            """Lấy giá trị tình cảm"""
            # Note: ischyros case removed
            if char_name == "huong":
                return self.rel_huong
            elif char_name == "hainu":
                return self.rel_hainu
            elif char_name == "xiu":
                return self.rel_xiu
            return 0
        
        # get_stat_multiplier_ischyros REMOVED - character no longer exists
        
        def get_stat_multiplier_huong(self):
            """Hương thích đời sống cao"""
            if self.doi_song >= 80:
                return 1.5
            elif self.doi_song >= 60:
                return 1.2
            else:
                return 1.0
        
        def get_stat_multiplier_hainu(self):
            """Hải Nữ (President) thích học tập cao"""
            # Changed: Hải Nữ is now president, prefers high study stats
            if self.hoc_tap >= 80:
                return 1.5
            elif self.hoc_tap >= 60:
                return 1.2
            else:
                return 1.0
        
        def get_stat_multiplier_xiu(self):
            """Xỉu thích cân bằng + tiền"""
            avg = (self.hoc_tap + self.doi_song) / 2
            if avg >= 70 and self.tien > 100000:
                return 1.5
            elif avg >= 50:
                return 1.2
            else:
                return 1.0
        
        def update_daily(self):
            """Gọi mỗi ngày mới - Returns dict of changes for display"""
            # Hồi stats
            hoc_tap_change = GameConfig.STAT_DAILY_HOC_TAP_REGEN
            self.modify_hoc_tap(hoc_tap_change)
            
            doi_song_change = GameConfig.STAT_DAILY_DOI_SONG_REGEN
            self.modify_doi_song(doi_song_change)
            
            # Xỉu relationship hồi
            xiu_rel_change = self.modify_relationship("xiu", 5)
            
            # Nhận tiền (nếu không bị cắt)
            if not self.dad_cutoff:
                base_money = GameConfig.STAT_DAILY_MONEY_BASE
            else:
                base_money = 0
            
            # Bonus từ Hải Nữ
            bonus_money = int(self.rel_hainu * 500)
            total_money = base_money + bonus_money
            
            self.modify_tien(total_money)
            
            # Return changes for notification display
            return {
                "hoc_tap": hoc_tap_change,
                "doi_song": doi_song_change,
                "rel_xiu": xiu_rel_change,
                "tien": total_money
            }

# Initialize stats globally
default stats = StatsManager()

# ================================================
# HELPER FUNCTIONS
# ================================================

init python:
    def show_stat_change(stat_name, amount):
        """Hiển thị thông báo khi stats thay đổi"""
        if amount > 0:
            symbol = "+"
            color = "#00ff00"
        else:
            symbol = ""
            color = "#ff0000"
        
        stat_display = {
            "hoc_tap": "Học tập",
            "doi_song": "Đời sống",
            "tien": "Tiền",
            # "rel_ischyros": "❤ Ischyros",  # REMOVED
            "rel_huong": "❤ Hương",
            "rel_hainu": "❤ Hải Nữ",
            "rel_xiu": "❤ Xỉu"
        }
        
        display_name = stat_display.get(stat_name, stat_name)
        
        # Skip if amount is 0
        if amount == 0:
            return
        
        # Show notification
        renpy.notify("{color=%s}%s %s%d{/color}" % (color, display_name, symbol, int(amount)))
        
        # Small pause to make notification visible (prevent overlap)
        renpy.pause(0.3, hard=False)


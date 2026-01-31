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
            self.rel_hainu = GameConfig.REL_INITIAL_HAINU
            self.rel_xiu = GameConfig.REL_INITIAL_XIU
            
            # Flags
            self.dad_cutoff = False  # Bố cắt trợ cấp
            
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
        
        def modify_relationship(self, char_name, amount):
            """
            Thay đổi tình cảm với nhân vật
            char_name: "hainu", "xiu"
            amount: số điểm thay đổi
            stat_multiplier: nhân với stats (Hải Nữ thích học tập, Hương thích đời sống)
            """
            
            if char_name == "hainu":
                self.rel_hainu = self.clamp(
                    self.rel_hainu + amount * self.get_stat_multiplier_hainu(),
                    GameConfig.REL_MIN,
                    GameConfig.REL_MAX
                )
            elif char_name == "xiu":
                self.rel_xiu = self.clamp(
                    self.rel_xiu + amount * self.get_stat_multiplier_xiu(),
                    GameConfig.REL_MIN,
                    GameConfig.REL_MAX
                )
            
            return self.get_relationship(char_name)

        def get_relationship(self, char_name):
            """Lấy giá trị tình cảm"""
            if char_name == "hainu":
                return self.rel_hainu
            elif char_name == "xiu":
                return self.rel_xiu
            return 0
        
        def get_stat_multiplier_xiu(self):
            """Xỉu thích đời sống cao"""
            if self.doi_song >= 80:
                return 2
            elif self.doi_song >= 40:
                return 1.5
            else:
                return 1.0
        
        def get_stat_multiplier_hainu(self):
            """Hải Nữ (President) thích học tập cao"""
            if self.hoc_tap >= 80:
                return 2
            elif self.hoc_tap >= 40:
                return 1.5
            else:
                return 1.0
        
        def update_daily(self):
            """Gọi mỗi ngày mới - Returns money changes for display"""
            
            # Nhận tiền (nếu không bị cắt)
            if not self.dad_cutoff:
                total_money = GameConfig.STAT_DAILY_MONEY_BASE
            else:
                total_money = 0
            
            self.modify_tien(total_money)
            
            # Return changes for notification display
            return total_money

# Initialize stats globally
default stats = StatsManager()

# ================================================
# HELPER FUNCTIONS
# ================================================

init python:
    def show_stat_change(stat_name, amount):
        """Hiển thị thông báo khi stats thay đổi"""
        if amount == 0:
            return
        elif amount > 0:
            symbol = "+"
            color = "#00ff00"
        else:
            symbol = ""
            color = "#ff0000"
        
        stat_display = {
            "hoc_tap": "Học tập",
            "doi_song": "Sức khỏe",
            "tien": "Tiền",

            "rel_hainu": "❤ Hải Nữ",
            "rel_xiu": "❤ Xỉu"
        }
        
        display_name = stat_display.get(stat_name)
        
        # Show notification
        renpy.notify("{color=%s}%s %s%d{/color}" % (color, display_name, symbol, int(amount)))
        
        # Small pause to make notification visible (prevent overlap)
        renpy.pause(0.3, hard=False)


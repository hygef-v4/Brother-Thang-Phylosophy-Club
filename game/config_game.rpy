# ================================================
# BROTHER THANG PHILOSOPHY CLUB - GAME CONFIG
# ================================================
# Central configuration file - Không hardcode!

default persistent.unlocked_endings = set()
init -1 python:
    # ========================================
    # GAME METADATA
    # ========================================
    class GameConfig:
        GAME_TITLE = "Brother Thang Philosophy Club"
        GAME_VERSION = "0.1.0 - MVP Day 1"
        DEVELOPER = "Kumo Studio"
        
        # ========================================
        # CHARACTER NAMES
        # ========================================
        CHAR_MAIN = "Võ Thắng"
        
        CHAR_HAINU = "Hải Nữ"  # Now club president (full name)
        CHAR_XIU = "Xỉu"  # Full name
        CHAR_DAD = "Võ Hưng"  # Full name - Đại Tá quân đội
        
        CHAR_T31 = "T31"
        
        # ========================================
        # STATS CONFIGURATION
        # ========================================
        STAT_MAX = 100
        STAT_MIN = 0
        STAT_INITIAL_HOC_TAP = 0
        STAT_INITIAL_DOI_SONG = 0
        STAT_INITIAL_TIEN = 100000
        
        # Daily changes
        STAT_DAILY_MONEY_BASE = 100000
        
        # ========================================
        # RELATIONSHIP CONFIGURATION
        # ========================================
        REL_MIN = 0
        REL_MAX = 100
        REL_INITIAL_HAINU = 0  # Start neutral
        REL_INITIAL_XIU = 0  # Changed from 50 to 0 - start neutral
        
        # ========================================
        # TIME SYSTEM
        # ========================================
        TIME_SLOTS = ["morning", "afternoon", "evening", "night"]
        CURRENT_CHAPTER = 1
        CURRENT_DAY = 1

# Initialize game config
default game_config = GameConfig()

# ========================================
# GAME VARIABLES
# ========================================
default current_day = 1
default current_chapter = 1
default current_time_slot = 1

# ========================================
# DEFINE CHARACTERS
# ========================================
define mc = Character(GameConfig.CHAR_MAIN, color="#FFFFFF")
define hainu = Character(GameConfig.CHAR_HAINU, color="#FFFFFF")  # President
define xiu = Character(GameConfig.CHAR_XIU, color="#FFFFFF")  # Recruits MC
define dad = Character(GameConfig.CHAR_DAD, color="#FFFFFF")  # Đại Tá
define narrator = Character(None)  # Cho narration
define robot = Character(GameConfig.CHAR_T31, image="t31")

# ========================================
# AUDIO DEFINITIONS (Tạm sử dụng DDLC audio)
# ========================================
# BGM - Define trực tiếp paths để tránh circular reference
define audio.main_theme = "<loop 22.073>bgm/1.ogg"
define audio.daily_life = "<loop 4.499>bgm/2.ogg"
define audio.club_theme = "<loop 4.618>bgm/3.ogg"
define audio.thinking = "<loop 10.893>bgm/6.ogg"
define audio.tense = "<loop 2.291>bgm/7.ogg"
define audio.sad = "<loop 9.938>bgm/8.ogg"

# SFX
define audio.phone_ring = "sfx/fall.ogg"  # Placeholder
define audio.notification = "sfx/pageflip.ogg"  # Placeholder
define audio.love_theme = "<loop 5.861>bgm/10.ogg"
define audio.happy = "<loop 4.444>bgm/5.ogg"

# New Varied Tracks
define audio.gym_theme = "<loop 4.499>bgm/4.ogg"  # Calm / Study
define audio.library_theme = "<loop 4.444>bgm/5.ogg"     # Upbeat / Active (Same as happy for now, or 5_monika)
define audio.argument = "<loop 4.444>bgm/6.ogg"       # Tense / Debate (Poem Panic)
define audio.deep_thought = "<loop 4.444>bgm/9.ogg"   # Sad / Introspective (My Feelings)
define audio.ending_sad = "<loop 4.444>bgm/10.ogg"    # Very sad / Ending (I Still Love You)

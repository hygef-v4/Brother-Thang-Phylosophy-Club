# ================================================
# CUSTOM IMAGE DEFINITIONS
# Brother Thang Philosophy Club
# ================================================

# Background - MC's Gaming Room
# Fit full screen (crop nếu cần để không có gray bars)
image bg mc_room = Transform("bg/mc_room.jpg", fit="cover", align=(0.5, 0.5))

# Character - Dad (Bố)
# Scale lên 85% để rõ hơn, position bottom center
image dad = Transform("dad.png", zoom=0.85, xalign=0.5, yalign=1.0)

# Variations (nếu cần)
image dad neutral = Transform("dad.png", zoom=0.85, xalign=0.5, yalign=1.0)
image dad angry = Transform("dad.png", zoom=0.85, xalign=0.5, yalign=1.0)

# Alias cho compatibility (không cần nữa)
# image bg residential_day = "bg/mc_room.jpg"

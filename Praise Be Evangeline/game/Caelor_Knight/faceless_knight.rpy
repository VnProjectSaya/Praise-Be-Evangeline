# ══════════════════════════════════════════════
# FACELESS KNIGHT — plain animated sprite (no face, no layeredimage)
# Just a body swap, no alpha — same technique as Eva. `show faceless_knight`
# directly; no attributes to pick since there's nothing else to layer.
# ══════════════════════════════════════════════

# No float exists in any chapter yet, so this defaults to Eva's calm
# timing (10s cycle, single flap at the top of the loop). Retime to match
# whenever a position transform gets written into a script.
image faceless_knight:
    "Caelor_Knight/Body_Anim_2_Knight.png"
    pause 0.5
    "Caelor_Knight/Body_Anim_1_Knight.png"
    pause 9.5
    repeat

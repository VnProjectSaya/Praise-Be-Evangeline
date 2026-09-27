
init python:

    def make_gold_rays(n=10, length=1600, width=14, color="#ffe7a0"):
        rays = [ ]
        for i in range(n):
            w = width if i % 2 == 0 else max(2, width // 3)
            rays.append(Transform(
                Solid(color, xysize=(w, length)),
                anchor=(0.5, 0.5), pos=(0.5, 0.5),
                rotate=i * 180.0 / n))
        return Fixed(*rays, xysize=(length, length))

    def gold_mote():
        return Transform(Solid("#fff3c4", xysize=(10, 10)), rotate=45, blend="add")

image gold_rays = make_gold_rays()
image gold_rays_fine = make_gold_rays(n=18, length=1300, width=5, color="#fff6d2")


image glory_bg = Transform("BG/GLORY/BG.jpg", zoom=0.64)

image glory_wings:
    zoom 0.64
    "BG/GLORY/wingframe1.png"
    pause 3.0
    "BG/GLORY/wingframe2.png" with Dissolve(1.0)
    pause 3.0
    "BG/GLORY/wingframe1.png" with Dissolve(1.0)
    repeat

image glory_bang_back:
    zoom 0.64
    "BG/GLORY/bang1behindbase_frame1.png"
    pause 3.0
    "BG/GLORY/bang1behindbase_frame2.png" with Dissolve(1.0)
    pause 3.0
    "BG/GLORY/bang1behindbase_frame1.png" with Dissolve(1.0)
    repeat

image glory_bang_front:
    zoom 0.64
    "BG/GLORY/bang2frontofbase_frame1.png"
    pause 3.0
    "BG/GLORY/bang2frontofbase_frame2.png" with Dissolve(1.0)
    pause 3.0
    "BG/GLORY/bang2frontofbase_frame1.png" with Dissolve(1.0)
    repeat

layeredimage glory_cg:
    always "glory_bg"
    always "glory_wings"
    always "glory_bang_back"

    group base:
        attribute normal default Transform("BG/GLORY/basenormal.png", zoom=0.64)
        attribute yandere Transform("BG/GLORY/baseyandere.png", zoom=0.64)
        attribute smile Transform("BG/GLORY/basesmile.png", zoom=0.64)

    always "glory_bang_front"

transform glory_rest:
    subpixel True
    anchor (0.5, 0.4) pos (0.5, 0.4)
    zoom 1.0

transform glory_settle:
    subpixel True
    anchor (0.5, 0.4) pos (0.5, 0.4)
    ease 2.0 zoom 1.0

transform glory_pulse:
    subpixel True
    anchor (0.5, 0.4) pos (0.5, 0.4)
    ease 0.12 zoom 1.015
    ease 0.18 zoom 1.0
    ease 0.12 zoom 1.015
    ease 0.4 zoom 1.0

transform glory_lean:
    subpixel True
    anchor (0.5, 0.4) pos (0.5, 0.4)
    ease 4.0 zoom 1.06

transform glory_close:
    subpixel True
    anchor (0.5, 0.4) pos (0.5, 0.4)
    ease 3.0 zoom 1.12

init python:
    import math
    import random

    class VoidCircle(renpy.Displayable):
        def __init__(self, radius, color="#000000", outline=None, outline_width=3, pad=2, **kwargs):
            super(VoidCircle, self).__init__(**kwargs)
            self.radius = int(radius)
            self.color = Color(color)
            self.outline = Color(outline) if outline else None
            self.outline_width = outline_width
            self.pad = int(pad)

        def render(self, width, height, st, at):
            c = self.radius + self.pad
            rv = renpy.Render(c * 2, c * 2)
            canvas = rv.canvas()
            if self.outline:
                canvas.circle(self.outline, (c, c), self.radius)
                canvas.circle(self.color, (c, c), max(1, self.radius - self.outline_width))
            else:
                canvas.circle(self.color, (c, c), self.radius)
            return rv

    class VoidBubbles(renpy.Displayable):
        def __init__(self, count=14, spread=60, rise=180, min_r=5, max_r=16, seed=7, **kwargs):
            super(VoidBubbles, self).__init__(**kwargs)
            rng = random.Random(seed)
            self.rise = rise
            self.spread = spread
            self.bubbles = [ ]
            for i in range(count):
                r = rng.randint(min_r, max_r)
                self.bubbles.append({
                    "d": VoidCircle(r, "#000000", "#8b0f0f", max(2, r // 4)),
                    "x": rng.uniform(-spread, spread),
                    "life": rng.uniform(1.2, 2.4),
                    "offset": rng.uniform(0.0, 2.4),
                    "sway": rng.uniform(4, 14),
                    "freq": rng.uniform(1.5, 3.5),
                    "rise": rise * rng.uniform(0.6, 1.2),
                    })

        def render(self, width, height, st, at):
            w = int(self.spread * 2 + 80)
            h = int(self.rise * 1.2 + 80)
            rv = renpy.Render(w, h)
            base = h - 40
            for b in self.bubbles:
                t = ((st + b["offset"]) % b["life"]) / b["life"]
                x = w / 2.0 + b["x"] + math.sin(st * b["freq"] + b["offset"]) * b["sway"]
                y = base - t * b["rise"]
                fade_in = min(1.0, t * 5.0)
                fade_out = 1.0 - max(0.0, t - 0.8) / 0.2
                pop = 1.0 + max(0.0, t - 0.8) * 2.5
                d = Transform(b["d"], alpha=fade_in * fade_out, zoom=(0.5 + t * 0.6) * pop)
                cr = renpy.render(d, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (int(x - cw / 2.0), int(y - ch / 2.0)))
            renpy.redraw(self, 0)
            return rv

# ---- gold light ----
image gold_halo = Solid("#ffd76a", xysize=(700, 700))
image gold_core = Solid("#fff4cc", xysize=(160, 160))
image gold_wash = Solid("#ffcf5a")
image gold_motes = SnowBlossom(gold_mote(), count=40, border=50, xspeed=(-15, 15), yspeed=(-90, -35), fast=True)

# ---- black light ----
image void_glow = VoidCircle(90, "#5a0000", pad=80)
image void_core = VoidCircle(46, "#000000", "#8b0f0f", 5)
image void_bubbles = VoidBubbles(count=14, spread=50, rise=190, seed=7)
image void_wash = Solid("#3a0d0d")
image void_flash = Solid("#000000")
image void_beam_rim = Solid("#6e0808", xysize=(191, 26))
image void_beam = Solid("#000000", xysize=(191, 12))
image void_beam_back_rim = Solid("#6e0808", xysize=(800, 26))
image void_beam_back = Solid("#000000", xysize=(800, 12))
image void_hole_glow = VoidCircle(90, "#5a0000", pad=70)
image void_hole = VoidCircle(32, "#000000", "#8b0f0f", 4)
image void_leak = VoidBubbles(count=10, spread=16, rise=170, min_r=3, max_r=9, seed=3)

# ---- corridor push scene ----
define RC_NIGHT_TINT = "#7482b8"
define RC_WALL_FLOOR = 0.95
define RC_SHADOW_BLUR = 20
define RC_SHADOW_LEAN = -40.0
define RC_TURN_TIME = 0.4

define RC_EVA_SHADOW_GAP = -0.07
define RC_EVA_SHADOW_ZOOM = 0.25
define RC_EVA_SHADOW_YSTRETCH = 2.0
define RC_EVA_SHADOW_WIDEN = 1.3

define RC_THER_SHADOW_GAP = -0.06
define RC_THER_SHADOW_ZOOM = 0.23
define RC_THER_SHADOW_YSTRETCH = 2.1
define RC_THER_SHADOW_WIDEN = 1.3

image rc_overcast = Solid("#0b1024")
image rc_overcast_red = Solid("#4a1414")

default rc_mv = {}
default rc_eva_face = -1.0        # same as eva's xzoom: -1 faces right, 1 faces left
default rc_ther_face = 1.0
default rc_eflip = -1.0
default rc_tflip = 1.0
default rc_ther_turn = 0.4        # seconds for Therion to turn around
default rc_shadow_alpha = 0.55
default rc_shadow_stretch = 1.0
default rc_stretch_cur = 1.0
default rc_clock = {}

init python:
    import time
    import math

    def rc_reset():
        store.rc_mv = {}
        store.rc_eva_face = -1.0
        store.rc_ther_face = 1.0
        store.rc_eflip = -1.0
        store.rc_tflip = 1.0
        store.rc_ther_turn = RC_TURN_TIME
        store.rc_shadow_alpha = 0.55
        store.rc_shadow_stretch = 1.0
        store.rc_stretch_cur = 1.0
        store.rc_clock = {}

    def rc_dt(key):
        now = time.time()
        last = store.rc_clock.get(key, now)
        store.rc_clock[key] = now
        return min(max(now - last, 0.0), 0.05), now

    def rc_turn(cur, target, dt, turn_time=None):
        step = dt * 2.0 / (turn_time or RC_TURN_TIME)
        if cur < target:
            return min(cur + step, target)
        return max(cur - step, target)

    # ---- position tracks: sprite and shadow both read these ----

    def rc_set(tag, x):
        store.rc_mv[tag] = [(x, x, 0.0, 0.0, "linear")]

    def rc_x(tag):
        segs = store.rc_mv.get(tag)
        if not segs:
            return 0.5
        now = time.time()
        for (x0, x1, t0, dur, warp) in segs:
            if now < t0:
                return x0
            if now < t0 + dur:
                return x0 + (x1 - x0) * renpy.atl.warpers[warp]((now - t0) / dur)
        return segs[-1][1]

    def rc_path(tag, *steps, **kw):
        # each step: (x, seconds) or (x, seconds, "warper"); same x = a pause
        t = time.time() + kw.get("delay", 0.0)
        x = rc_x(tag)
        segs = [ ]
        for step in steps:
            x1, dur = step[0], step[1]
            warp = step[2] if len(step) > 2 else "ease"
            segs.append((x, x1, t, dur, warp))
            x, t = x1, t + dur
        store.rc_mv[tag] = segs

    # ---- sprites ----

    def rc_eva_tf(trans, st, at):
        dt, now = rc_dt("eva")
        trans.xpos = rc_x("eva")
        trans.xzoom = rc_turn(trans.xzoom, store.rc_eva_face, dt)
        return 0

    def rc_ther_tf(trans, st, at):
        dt, now = rc_dt("therion")
        store.rc_tflip = rc_turn(store.rc_tflip, store.rc_ther_face, dt, store.rc_ther_turn)
        trans.xpos = rc_x("therion")
        trans.xzoom = store.rc_tflip
        return 0

    # ---- shadows, same look as the minigame ----

    def rc_eshadow_tf(trans, st, at):
        dt, now = rc_dt("eshadow")
        store.rc_eflip = rc_turn(store.rc_eflip, store.rc_eva_face, dt)
        trans.xpos = rc_x("eva") + RC_EVA_SHADOW_GAP
        trans.xzoom = store.rc_eflip * RC_EVA_SHADOW_WIDEN * (1.0 + 0.05 * math.sin(now * 1.3 + 1.0))
        trans.yzoom = RC_EVA_SHADOW_YSTRETCH * store.rc_stretch_cur * (1.0 + 0.06 * math.sin(now * 0.9))
        trans.rotate = RC_SHADOW_LEAN + 2.0 * math.sin(now * 0.7)
        trans.alpha += (store.rc_shadow_alpha - trans.alpha) * min(1.0, dt * 3.0)
        return 0

    def rc_tshadow_tf(trans, st, at):
        dt, now = rc_dt("tshadow")
        store.rc_stretch_cur += (store.rc_shadow_stretch - store.rc_stretch_cur) * min(1.0, dt * 1.5)
        trans.xpos = rc_x("therion") + RC_THER_SHADOW_GAP
        trans.xzoom = store.rc_tflip * RC_THER_SHADOW_WIDEN * (1.0 - 0.06 * math.sin(now * 1.7))
        trans.yzoom = RC_THER_SHADOW_YSTRETCH * store.rc_stretch_cur * (1.0 + 0.08 * math.sin(now * 1.1) + 0.03 * math.sin(now * 2.9))
        trans.rotate = RC_SHADOW_LEAN + 2.5 * math.sin(now * 0.8)
        trans.alpha += (store.rc_shadow_alpha - trans.alpha) * min(1.0, dt * 3.0)
        return 0


image tburst_bg     = Transform("BG/BURST/background.jpg", xysize=(1920, 1080))
image tburst_pupils = Transform("BG/BURST/pupils.png",     xysize=(1920, 1080))
image tburst_blood  = Transform("BG/BURST/bloodburst.png", xysize=(1920, 1080))

transform tburst_pupil_jit:
    subpixel True
    xpos 0 ypos 0
    block:
        xoffset 1.5 yoffset -1.0
        pause 0.04
        xoffset -1.0 yoffset 0.5
        pause 0.03
        xoffset 0.5 yoffset 1.2
        pause 0.05
        xoffset -1.8 yoffset -0.5
        pause 0.03
        xoffset 1.0 yoffset 0.8
        pause 0.04
        xoffset -0.5 yoffset -1.2
        pause 0.03
        xoffset 1.8 yoffset 0.3
        pause 0.05
        xoffset 0 yoffset 0
        pause 0.03
        repeat

image tburst_face:
    contains:
        "tburst_bg"
    contains:
        "tburst_pupils"
        tburst_pupil_jit

transform tburst_face_move:
    subpixel True
    align (0.5, 0.5)
    zoom 1.02
    xoffset 0 yoffset 0
    pause 0.08
    linear 0.04 xoffset -3
    linear 0.06 xoffset 2
    linear 0.08 xoffset 0
    block:
        ease 3.0 xoffset -3 yoffset 1
        ease 3.0 xoffset 3 yoffset -1
        repeat

transform tburst_blood_move:
    subpixel True
    anchor (0.552, 0.498)
    pos (0.552, 0.498)
    zoom 0.35 alpha 0.0
    xoffset 0 yoffset 0
    easein 0.12 zoom 1.04 alpha 1.0
    easeout 0.1 zoom 1.0
    linear 0.03 xoffset 14 yoffset -6
    linear 0.03 xoffset -11 yoffset 4
    linear 0.03 xoffset 7 yoffset -3
    linear 0.03 xoffset -4 yoffset 2
    linear 0.04 xoffset 2 yoffset -1
    linear 0.05 xoffset 0 yoffset 0
    block:
        ease 3.0 xoffset 8 yoffset -4 zoom 1.012
        ease 3.0 xoffset -8 yoffset 4 zoom 1.0
        repeat


image evadeath_bg    = Transform("BG/evadeath/BG.png",    xysize=(1920, 1080))
image evadeath_eva   = Transform("BG/evadeath/EVABASE.png",   xysize=(1920, 1080))
image evadeath_hand1 = Transform("BG/evadeath/hand1.png", xysize=(1920, 1080))
image evadeath_hand2 = Transform("BG/evadeath/hand2.png", xysize=(1920, 1080))
image evadeath_hand3 = Transform("BG/evadeath/hand3.png", xysize=(1920, 1080))
image evadeath_hand4 = Transform("BG/evadeath/hand4.png", xysize=(1920, 1080))

transform evadeath_cam:
    subpixel True
    align (0.5, 0.5)
    zoom 1.0
    block:
        ease 5.0 zoom 1.025
        ease 5.0 zoom 1.0
        repeat

transform evadeath_shake1:
    subpixel True
    block:
        xoffset 1.5 yoffset -1
        pause 0.05
        xoffset -1 yoffset 1
        pause 0.06
        xoffset 1 yoffset 0.5
        pause 0.05
        xoffset -1.5 yoffset -0.5
        pause 0.06
        repeat

transform evadeath_shake2:
    subpixel True
    block:
        xoffset 3.5 yoffset -2
        pause 0.04
        xoffset -3 yoffset 1.5
        pause 0.04
        xoffset 2 yoffset 2.5
        pause 0.05
        xoffset -3.5 yoffset -1.5
        pause 0.04
        xoffset 1 yoffset -2.5
        pause 0.04
        repeat

transform evadeath_shake3:
    subpixel True
    block:
        xoffset 6 yoffset -3
        pause 0.03
        xoffset -5 yoffset 3
        pause 0.03
        xoffset 3 yoffset 4
        pause 0.04
        xoffset -6 yoffset -2
        pause 0.03
        xoffset 2 yoffset -4
        pause 0.03
        xoffset -3 yoffset 2
        pause 0.04
        repeat


transform evadeath_hand1_move:   # left edge, reaches right
    subpixel True
    xoffset -350 alpha 0.0
    easein 0.35 xoffset 0 alpha 1.0
    block:
        ease 0.45 xoffset 28 yoffset -10
        ease 0.3 xoffset 12 yoffset 4
        ease 0.5 xoffset 34 yoffset -6
        ease 0.4 xoffset 0 yoffset 0
        repeat

transform evadeath_hand2_move:   # top right, reaches down-left
    subpixel True
    xoffset 300 yoffset -200 alpha 0.0
    easein 0.35 xoffset 0 yoffset 0 alpha 1.0
    block:
        ease 0.5 xoffset -26 yoffset 18
        ease 0.35 xoffset -8 yoffset 6
        ease 0.45 xoffset -32 yoffset 22
        ease 0.5 xoffset 0 yoffset 0
        repeat

transform evadeath_hand3_move:   # bottom right, reaches up-left
    subpixel True
    xoffset 250 yoffset 300 alpha 0.0
    easein 0.35 xoffset 0 yoffset 0 alpha 1.0
    block:
        ease 0.4 xoffset -20 yoffset -24
        ease 0.45 xoffset -6 yoffset -8
        ease 0.35 xoffset -28 yoffset -30
        ease 0.55 xoffset 0 yoffset 0
        repeat

transform evadeath_hand4_move:   # bottom center, reaches up
    subpixel True
    yoffset 400 alpha 0.0
    easein 0.35 yoffset 0 alpha 1.0
    block:
        ease 0.55 xoffset 6 yoffset -30
        ease 0.3 xoffset -4 yoffset -12
        ease 0.5 xoffset 8 yoffset -36
        ease 0.4 xoffset 0 yoffset 0
        repeat
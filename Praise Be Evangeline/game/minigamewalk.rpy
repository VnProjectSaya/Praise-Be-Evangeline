
define MG_START = 0.66
define MG_END = 0.12
define MG_RIGHT_LIMIT = 0.72
define MG_SPEED = 0.08
define MG_FIRST_THOUGHT = 0.05
define MG_TURN_TIME = 0.4
define MG_TURN_WAIT = 0.5

define MG_NIGHT_TINT = "#7482b8"

define MG_WALL_FLOOR = 0.95
define MG_SHADOW_BLUR = 20
define MG_SHADOW_LEAN = -40.0

define MG_EVA_SHADOW_GAP = -0.07
define MG_EVA_SHADOW_ZOOM = 0.25
define MG_EVA_SHADOW_YSTRETCH = 2.0
define MG_EVA_SHADOW_WIDEN = 1.3
define MG_EVA_SHADOW_ALPHA = 0.55

define MG_SHADOW_GAP = 0.6
define MG_SHADOW_DROP = 0.15
define MG_SHADOW_ZOOM = 0.24
define MG_SHADOW_YSTRETCH = 2.3
define MG_SHADOW_WIDEN = 1.4
define MG_SHADOW_ALPHA = 0.65

default mg_x = MG_START
default mg_face = 1.0
default mg_eflip = 1.0
default mg_left = False
default mg_right = False
default mg_stage = 0
default mg_moved = False
default mg_pending = None
default mg_pending_at = 0.0
default mg_shadow_x = MG_START + MG_SHADOW_GAP
default mg_shadow_on = True
default mg_clock = {}

init python:
    import time
    import math

    def mg_dt(key):
        now = time.time()
        last = store.mg_clock.get(key, now)
        store.mg_clock[key] = now
        return min(max(now - last, 0.0), 0.05), now

    def mg_turn(cur, target, dt):
        step = dt * 2.0 / MG_TURN_TIME
        if cur < target:
            return min(cur + step, target)
        return max(cur - step, target)

    def mg_reset():
        store.mg_x = MG_START
        store.mg_face = 1.0
        store.mg_eflip = 1.0
        store.mg_left = False
        store.mg_right = False
        store.mg_stage = 0
        store.mg_moved = False
        store.mg_pending = None
        store.mg_pending_at = 0.0
        store.mg_shadow_x = MG_START + MG_SHADOW_GAP
        store.mg_shadow_on = True
        store.mg_clock = {}

    def mg_resume():
        store.mg_left = False
        store.mg_right = False
        store.mg_clock.pop("step", None)

    def mg_step():
        dt, now = mg_dt("step")

        if store.mg_pending:
            if now >= store.mg_pending_at:
                result = store.mg_pending
                store.mg_pending = None
                return result
            return None

        left = store.mg_left and not store.mg_right
        right = store.mg_right and not store.mg_left

        if right and store.mg_stage == 0:
            right = False

        if left:
            store.mg_face = 1.0
            store.mg_x = max(MG_END, store.mg_x - MG_SPEED * dt)
            store.mg_moved = True
        elif right:
            store.mg_face = -1.0
            store.mg_x = min(MG_RIGHT_LIMIT, store.mg_x + MG_SPEED * dt)
            store.mg_moved = True

        store.mg_shadow_on = store.mg_face > 0

        if store.mg_stage == 0 and store.mg_x <= MG_START - MG_FIRST_THOUGHT:
            store.mg_stage = 1
            return "steps"

        if store.mg_stage == 1 and store.mg_face < 0:
            store.mg_stage = 2
            store.mg_pending = "look_back"
            store.mg_pending_at = now + MG_TURN_WAIT
            return None

        if store.mg_stage == 2 and store.mg_face > 0:
            store.mg_stage = 3
            store.mg_pending = "look_front"
            store.mg_pending_at = now + MG_TURN_WAIT
            return None

        if store.mg_x <= MG_END:
            store.mg_stage = 4
            return "end"

        return None


    def mg_eva_tf(trans, st, at):
        dt, now = mg_dt("eva")
        trans.xpos = store.mg_x
        trans.xzoom = mg_turn(trans.xzoom, store.mg_face, dt)
        trans.yoffset = 32 + 8 * math.cos(now * math.pi / 2.0)
        return 0

    def mg_eshadow_tf(trans, st, at):
        dt, now = mg_dt("eshadow")
        store.mg_eflip = mg_turn(store.mg_eflip, store.mg_face, dt)
        trans.xpos = store.mg_x + MG_EVA_SHADOW_GAP

        trans.xzoom = store.mg_eflip * MG_EVA_SHADOW_WIDEN * (1.0 + 0.05 * math.sin(now * 1.3 + 1.0))
        trans.yzoom = MG_EVA_SHADOW_YSTRETCH * (1.0 + 0.06 * math.sin(now * 0.9))
        trans.rotate = MG_SHADOW_LEAN + 2.0 * math.sin(now * 0.7)
        return 0

    def mg_vshadow_tf(trans, st, at):
        dt, now = mg_dt("vshadow")
        target = store.mg_x + MG_SHADOW_GAP

        pull = 0.25 + 0.75 * (0.5 + 0.5 * math.sin(now * 3.0)) ** 2
        store.mg_shadow_x += (target - store.mg_shadow_x) * min(1.0, dt * 2.6 * pull)
        trans.xpos = store.mg_shadow_x

        gap = max(-1.0, min(1.0, (target - store.mg_shadow_x) * 10))

        trans.yzoom = MG_SHADOW_YSTRETCH * (1.0 + 0.12 * math.sin(now * 1.1) + 0.05 * math.sin(now * 2.9))
        trans.xzoom = MG_SHADOW_WIDEN * (1.0 - 0.10 * math.sin(now * 1.7))
        trans.rotate = MG_SHADOW_LEAN + 4.0 * gap + 3.0 * math.sin(now * 0.8)

        alpha_target = MG_SHADOW_ALPHA if store.mg_shadow_on else 0.0
        trans.alpha += (alpha_target - trans.alpha) * min(1.0, dt * 8.0)
        return 0


screen eva_shadow_walk():
    on "show" action Function(mg_resume)

    key "keydown_K_LEFT" action SetVariable("mg_left", True)
    key "keyup_K_LEFT" action SetVariable("mg_left", False)
    key "keydown_K_a" action SetVariable("mg_left", True)
    key "keyup_K_a" action SetVariable("mg_left", False)

    key "keydown_K_RIGHT" action SetVariable("mg_right", True)
    key "keyup_K_RIGHT" action SetVariable("mg_right", False)
    key "keydown_K_d" action SetVariable("mg_right", True)
    key "keyup_K_d" action SetVariable("mg_right", False)

    timer 0.016 repeat True action Function(mg_step)

    if not mg_moved:
        text "Use the arrow keys to walk":
            xalign 0.5
            yalign 0.9
            size 32
            color "#FEF8EA"
            outlines [(3, "#00000099", 0, 0)]
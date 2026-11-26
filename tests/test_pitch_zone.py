import pytest
import game.pitch_zone as mod

CASES = [
    ("seam_spin_unwrap", (1,)),
    ("release_time_backtrack", (1,)),
    ("strikezone_rebuild", (1,)),
    ("occlusion_track_filter", (1,)),
    ("challenge_rule_snapshot", (1,)),
    ("atbat_cache_key", (1,)),
    ("load_pitch", (1,)),
    ("track_ball", (1,)),
    ("judge_pitch", (1,)),
    ("present_pitch", (1,)),
    ("validate_pitch", (1,)),
    ("metrics_pitch", (1,)),
    ("audit_pitch", (1,)),
    ("fallback_pitch", (1,)),
    ("determinism_pitch", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

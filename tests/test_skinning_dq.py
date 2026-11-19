import pytest
from render import skinning_dq as mod

CASES = [
    ("dq", 'm.dq_normalize(2.0) == approx(1.0, rel=1e-3)'),
    ("palette", 'm.palette_index(2, 1, 4) == 3'),
    ("root", 'm.apply_root_motion((1.0, 2.0), (3.0, 4.0)) == approx((4.0, 6.0))'),
    ("delta", 'm.gpu_cpu_delta(1.0, 3.0) == approx(2.0)'),
    ("blend", 'm.blend_shape_weight(0.0, 1.0, 0.5) == approx(0.5)'),
    ("nonuniform", 'm.nonuniform_scale(2.0, 1.0) == approx(2.0)'),
    ("lag", 'm.bone_lag(10.0, 8.0, 1.0) == approx(8.0)'),
    ("lod", 'm.lod_weight_map(1.0, 0.5) == approx(0.5)'),
    ("constraint", 'm.constraint_order(1, True) == 1'),
    ("cache", 'm.cache_version("m", "s") == "m:s"'),
    ("slot", 'm.bone_slot(1, 2) == "1:2"'),
    ("normal", 'm.normal_scale(2.0, 2.0) == approx(1.0)'),
    ("twist", 'm.twist_correction(180.0, 90.0) == approx(90.0)'),
    ("bind", 'm.bind_pose((1.0, 2.0), (0.0, 0.0)) == approx((1.0, 2.0))'),
    ("matrix", 'm.matrix_weight(0.5, 0.5) == approx(1.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})

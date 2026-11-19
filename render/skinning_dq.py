"""第 61 批：角色做大幅度扭腰，肩部网格塌陷成尖角，武器挂点又滑出掌心：蒙皮只..."""

def dq_normalize(value):
    """双四元数归一。"""
    raise NotImplementedError("TODO: dq_normalize")

def palette_index(index, offset, size):
    """LOD 调色板索引。"""
    raise NotImplementedError("TODO: palette_index")

def apply_root_motion(position, delta):
    """根运动应用。"""
    raise NotImplementedError("TODO: apply_root_motion")

def gpu_cpu_delta(cpu, gpu):
    """GPU/CPU 骨骼差。"""
    raise NotImplementedError("TODO: gpu_cpu_delta")

def blend_shape_weight(base, shape, weight):
    """混合形状顺序。"""
    raise NotImplementedError("TODO: blend_shape_weight")

def nonuniform_scale(scale, normal):
    """非均匀缩放。"""
    raise NotImplementedError("TODO: nonuniform_scale")

def bone_lag(current, previous, max_lag):
    """异步骨骼滞后。"""
    raise NotImplementedError("TODO: bone_lag")

def lod_weight_map(weight, ratio):
    """权重重采样。"""
    raise NotImplementedError("TODO: lod_weight_map")

def constraint_order(constraint, skinned):
    """约束顺序。"""
    raise NotImplementedError("TODO: constraint_order")

def cache_version(mesh_id, skin_id):
    """蒙皮缓存键。"""
    raise NotImplementedError("TODO: cache_version")

def bone_slot(slot, batch):
    """骨骼槽位键。"""
    raise NotImplementedError("TODO: bone_slot")

def normal_scale(normal, scale):
    """法线缩放。"""
    raise NotImplementedError("TODO: normal_scale")

def twist_correction(angle, limit):
    """扭转修正。"""
    raise NotImplementedError("TODO: twist_correction")

def bind_pose(position, inverse):
    """绑定姿势。"""
    raise NotImplementedError("TODO: bind_pose")

def matrix_weight(weight_a, weight_b):
    """权重合并。"""
    raise NotImplementedError("TODO: matrix_weight")

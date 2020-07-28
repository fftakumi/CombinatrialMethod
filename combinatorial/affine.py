import numpy as np


def clip_xy(ref_xy, img_shape):
    # x座標について置換
    ref_x = np.where((0 <= ref_xy[:, :, 0]) & (ref_xy[:, :, 0] < img_shape[0]), ref_xy[:, :, 0], -1)
    # y座標について置換
    ref_y = np.where((0 <= ref_xy[:, :, 1]) & (ref_xy[:, :, 1] < img_shape[1]), ref_xy[:, :, 1], -1)

    # 結合して返す
    return np.dstack([ref_x, ref_y])


def affine(data, magnification=1, rotation=0, tx=0, ty=0, hf=1, vf=1):
    height, width = data.shape
    y, x = np.mgrid[:height, :width]
    xy = np.dstack([x, y, np.ones((height, width))])
    # ===========================================================================================================================
    affine_center2ori = np.array([[1, 0, width / 2],
                                  [0, 1, height / 2],
                                  [0, 0, 1]])
    affine_ori2center = np.array([[1, 0, -width / 2],
                                  [0, 1, -height / 2],
                                  [0, 0, 1]])
    affine_trans = np.array([[1, 0, tx],
                             [0, 1, ty],
                             [0, 0, 1]])

    affine_flip = np.array([[hf, 0, 0],
                            [0, vf, 0],
                            [0, 0, 1]])

    affine_rot_mag = np.array([[magnification * np.cos(rotation), magnification * np.sin(rotation), 0],
                            [magnification * -np.sin(rotation), magnification * np.cos(rotation), 0],
                            [0, 0, 1]])
    affine = affine_trans @ affine_center2ori @affine_flip @ affine_rot_mag @ affine_ori2center
    # ===========================================================================================================================
    inv_affine = np.linalg.inv(affine)
    ref_xy = np.einsum('ijk,lk->ijl', xy, inv_affine)[..., :2]

    # 参照座標の周りの座標
    linear_xy = {}
    linear_xy['upleft'] = ref_xy.astype(int)
    linear_xy['downleft'] = linear_xy['upleft'] + [1, 0]
    linear_xy['upright'] = linear_xy['upleft'] + [0, 1]
    linear_xy['downright'] = linear_xy['upleft'] + [1, 1]
    upleft_diff = ref_xy - linear_xy['upleft']

    # (1-xの差)と(1-yの差)の積を計算
    linear_weight = {}
    linear_weight['upleft'] = (1 - upleft_diff[..., 0]) * (1 - upleft_diff[..., 1])
    linear_weight['downleft'] = upleft_diff[..., 0] * (1 - upleft_diff[..., 1])
    linear_weight['upright'] = (1 - upleft_diff[..., 0]) * upleft_diff[..., 1]
    linear_weight['downright'] = upleft_diff[..., 0] * upleft_diff[..., 1]
    linear_with_weight = {}
    for direction in linear_xy.keys():
        l_xy = linear_xy[direction]
        l_xy = clip_xy(l_xy, (height, width))
        l_weight = linear_weight[direction]
        linear_with_weight[direction] = l_weight * data[l_xy[:, :, 0], l_xy[:, :, 1]]
    data_linear = sum(linear_with_weight.values())
    return data_linear

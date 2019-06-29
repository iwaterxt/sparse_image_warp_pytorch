# sparse_image_warp_pytorch
Provides a pytorch implementation of sparse_image_warp and an example of spec_augment.

Original implementation comes from [zcaceres](https://github.com/zcaceres/spec_augment).

But there are several errors in their implementation:

 * In their implementation they didn't add boundary points to source and destination. The idea is to sample a point and its destination after warpping but we want to keep boundary point the same. Since they didn't do this they need to add [small noise](https://github.com/zcaceres/spec_augment/blob/master/SparseImageWarp.ipynb?short_path=7ed82fd#L202) instead of zeros to lhs matrix.
 * cross_squared_distance_matrix
 
 Example of time warpping:
 
![time warp](https://github.com/bobchennan/sparse_image_warp_pytorch/blob/master/ret.png)

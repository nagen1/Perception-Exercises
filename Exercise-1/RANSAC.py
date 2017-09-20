# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')

# Voxel Grid filter
vox = cloud.make_voxel_grid_filter()

LEAF_SIZE = 1
vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)

cloud_filtered = vox.filter()

filename = 'voxel-downampled.pcd'

# PassThrough filter
passthrough = cloud_filtered.make_passthrough_filter()

#Assign axis and range to the passthrough filter object
filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
axis_min = 0
axis_max = 2

passthrough.set_filter_limits(axis_min, axis_max)

#Finally user the filter function to obtain the resultant point cloud
cloud_filtered = passthrough.filter()
filename = 'pass_through_filtered.pcd'
#pcl.save(cloud_filtered, filename)

# RANSAC plane segmentation


# Extract inliers

# Save pcd for table
# pcl.save(cloud, filename)
pcl.save(cloud_filtered, filename)

# Extract outliers


# Save pcd for tabletop objects

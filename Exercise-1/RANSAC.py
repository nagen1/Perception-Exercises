# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')

# Voxel Grid filter
vox = cloud.make_voxel_grid_filter()

LEAF_SIZE = 1
vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)

cloud_filtered = vox.filter()

# PassThrough filter
passthrough = cloud_filtered.make_passthrough_filter()

#Assign axis and range to the passthrough filter object
filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
axis_min = 0.6
axis_max = 1.1

passthrough.set_filter_limits(axis_min, axis_max)

#Finally user the filter function to obtain the resultant point cloud
cloud_filtered = passthrough.filter()
filename = 'pass_through_filtered.pcd'


# RANSAC plane segmentation
 # create the segmentation object
seg = cloud_filtered.make_segmenter()

 #Set the model
seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_model_type(pcl.SAC_RANSAC)

max_distance = 0.01
seg.set_distance_threshold(max_distance)

inliers, coefficients = seg.segment()
extract_inliers = cloud_filtered.extract(inliers, negative=False)
filename = 'extracted_inliers.pcd'

extract_outliers = cloud_filtered.extract(inliers, negative=True)
filename = 'extracted_outliers.pcd'


outlier_filter = cloud_filtered.make_statistical_outlier_filter()
outlier_filter.set_mean_k(50)

x = 1.0
outlier_filter.set_std_dev_mul_thresh(x)
cloud_filtered = outlier_filter.filter()

pcl.save(extract_outliers, filename)

# Extract inliers

# Save pcd for table
#pcl.save(extract_inliers, filename)

# Extract outliers


# Save pcd for tabletop objects

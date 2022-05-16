def better_than_average(class_points, your_points):
    av_st = sum(class_points)/len(class_points)
    if av_st > your_points:
        return False
    else:
        return True
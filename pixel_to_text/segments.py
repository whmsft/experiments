import cv2
import numpy as np

def connected_components_with_stats(threshold, connectivity, dtype):
    # Label the connected components in the thresholded image
    label_map = np.zeros_like(threshold, dtype=np.int32)
    label = 1
    for i in range(threshold.shape[0]):
        for j in range(threshold.shape[1]):
            if threshold[i, j] != 0 and label_map[i, j] == 0:
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if label_map[x, y] == 0:
                        label_map[x, y] = label
                        if x > 0 and threshold[x-1, y] != 0:
                            stack.append((x-1, y))
                        if x < threshold.shape[0]-1 and threshold[x+1, y] != 0:
                            stack.append((x+1, y))
                        if y > 0 and threshold[x, y-1] != 0:
                            stack.append((x, y-1))
                        if y < threshold.shape[1]-1 and threshold[x, y+1] != 0:
                            stack.append((x, y+1))
                label += 1

    # Compute the statistics for each connected component
    num_labels = label - 1
    labels = np.arange(1, num_labels+1, dtype=np.int32)
    stats = np.zeros((num_labels, 5), dtype=np.int32)
    for i in range(1, num_labels+1):
        component = label_map == i
        stats[i-1, cv2.CC_STAT_LEFT] = np.min(np.where(component)[1])
        stats[i-1, cv2.CC_STAT_TOP] = np.min(np.where(component)[0])
        stats[i-1, cv2.CC_STAT_WIDTH] = np.max(np.where(component)[1]) - stats[i-1, cv2.CC_STAT_LEFT] + 1
        stats[i-1, cv2.CC_STAT_HEIGHT] = np.max(np.where(component)[0]) - stats[i-1, cv2.CC_STAT_TOP] + 1
        stats[i-1, cv2.CC_STAT_AREA] = np.sum(component)
        m00 = np.sum(component)
        m10 = np.sum(np.dot(component, np.arange(threshold.shape[1])))
        m01 = np.sum(np.dot(np.arange(threshold.shape[0])[:, np.newaxis], component))
        if m00 == 0:
            stats[i-1, cv2.CC_STAT_LEFT] = 0
            stats[i-1, cv2.CC_STAT_TOP] = 0
            stats[i-1, cv2.CC_STAT_WIDTH] = 0
            stats[i-1, cv2.CC_STAT_HEIGHT] = 0
            stats[i-1, cv2.CC_STAT_AREA] = 0
            stats[i-1, cv2.CC_STAT_LEFT] = 0
            stats[i-1, cv2.CC_STAT_TOP] = 0
        else:
            stats[i-1, cv2.CC_STAT_CENTROID] = np.array([m10/m00, m01/m00])

    return label_map, labels, stats, None, None


image = cv2.imread('E:/dio.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

connectivity = 4
#output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)
output = connected_components_with_stats(thresh, connectivity, cv2.CV_32S)

num_labels = output[0]
labels = output[1]
stats = output[2]

for i in range(1, num_labels):
    x, y, w, h, area = stats[i]
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    character = image[y:y+h, x:x+w]
    cv2.imwrite(f'character_{i}.png', character)
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import random
import math


# Euclidian Distance between two d-dimensional points
def eucldist(p0, p1):
    dist = 0.0
    for i in range(0, len(p0)):
        dist += (p0[i] - p1[i]) ** 2
    return math.sqrt(dist)

# K-Means Algorithm
def kmeans(k, datapoints):
    # d - Dimensionality of Datapoints
    d = len(datapoints[0])

    # Limit the iterations
    Max_Iterations = 100
    i = 0

    cluster = [0] * len(datapoints)
    prev_cluster = [-1] * len(datapoints)

    # Choose Centers for the Clusters
    cluster_centers = []
    for i in range(0, k):
        new_cluster = []

        cluster_centers += [random.choice(datapoints)]

        force_recalculation = False

    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation):

        prev_cluster = list(cluster)
        force_recalculation = False
        i += 1

        # Update Point's Cluster Alligiance
        for p in range(0, len(datapoints)):
            min_dist = float("inf")

            # min_distance against all centers
            for c in range(0, len(cluster_centers)):

                dist = eucldist(datapoints[p], cluster_centers[c])

                if (dist < min_dist):
                    min_dist = dist
                    cluster[p] = c  # Reassign Point to new Cluster

        # Update Cluster's Position
        for k in range(0, len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0, len(datapoints)):
                if (cluster[p] == k):  # If this point belongs to the cluster
                    for j in range(0, d):
                        new_center[j] += datapoints[p][j]
                    members += 1

            for j in range(0, d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members)

                else:
                    new_center = random.choice(datapoints)
                    force_recalculation = True
                    print("Forced Recalculation...")

            cluster_centers[k] = new_center

    print("the Results :")
    print( "Clusters", cluster_centers)
    print ("Iterations", i)
    print ("Assignments", cluster)


# TESTING THE PROGRAM #
if __name__ == "__main__":

    #insert the dataset
    datapoints = [(2, 2), (4, 6), (7, 8), (11, 13)]

    k = 3  # K - Number of Clusters

    kmeans(k, datapoints)
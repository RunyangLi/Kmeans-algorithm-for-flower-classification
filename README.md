# Kmeans-algorithm-for-flower-classification
A Python program that use K-means based on Tensorflow
The code is published as follows

K-Means Clustering
Advantages: Easy to implement
Disadvantages: May converge to local minima, and converges slowly on large datasets
Applicable Data Types: Numerical data
K-means is an algorithm that discovers K clusters in a given dataset. The number of clusters K is specified by the user, and each cluster is described by its 'centroid,' which is the center of all points in the cluster.
K-Means Workflow
First, randomly determine K initial points as centroids. Then, assign each point in the dataset to a cluster. Specifically, for each point, find the nearest centroid and assign it to the cluster corresponding to that centroid. After this step, the centroid of each cluster is updated to the average of all points in that cluster.
The pseudocode for the above process is as follows:

  Create k points as initial centroids (often randomly selected)
  While the cluster assignment of any point changes
      For each data point in the dataset
          For each centroid
              Calculate the distance between the centroid and the data point
          Assign the data point to the nearest cluster
      For each cluster, calculate the mean of all points in the cluster and use it as the new centroid

      
General K-Means Process
Collect Data: Using any method
Prepare Data: Numerical data is needed to calculate distances, and nominal data can be mapped to binary data for distance calculation
Analyze Data: Using any method
Train Algorithm: Not applicable to unsupervised learning, as there is no training process in unsupervised learning
Test Algorithm: Apply the clustering algorithm and observe the results. Quantitative error metrics such as the sum of squared errors can be used to evaluate the algorithm's results
Use Algorithm: Can be used for any desired application. Typically, cluster centroids can represent the data of the entire cluster to make decisions
Improving Clustering Performance with Post-Processing
The matrix containing the cluster assignment results stores the error of each point, i.e., the squared distance from the point to the cluster centroid. This error can determine whether the user's predefined parameter K is correct and whether the generated clusters are good.
SSE (Sum of Squared Error): A metric used to measure clustering performance.
A smaller SSE value indicates that data points are closer to their centroids, and the clustering effect is better. Since the error is squared, points farther from the center are given more weight. One way to definitely reduce the SSE value is to increase the number of clusters, but this goes against the goal of clustering. The goal of clustering is to improve the quality of clusters while keeping the cluster data unchanged.
To keep the total number of clusters unchanged, two clusters can be merged. It is easy to visualize clustering on two-dimensional data. For multidimensional data, there are two quantifiable methods: merging the nearest centroids or merging two centroids that result in the smallest increase in SSE. The first approach is achieved by calculating the distances between all centroids and then merging the two closest points. The second method requires merging two clusters and calculating the total SSE value. The above process must be repeated for all possible pairs of clusters until the best pair to merge is found.
Bisecting K-Means Algorithm
The bisecting k-means algorithm is designed to overcome the problem of k-means algorithm converging to local minima. The bisecting k-means algorithm first treats all points as one cluster, then splits this cluster into two. Subsequently, one of the clusters is chosen for further division, depending on whether dividing it can maximize the reduction of SSE value. The above SSE-based division process is repeated until the user-specified number of clusters is obtained.
The pseudocode for bisecting k-means is as follows:
复制
  Treat all points as one cluster
  While the number of clusters is less than k
      For each cluster
          Calculate the total error
          Perform k-means (k=2) on the given cluster
          Calculate the total error after splitting the cluster into two
      Choose the cluster to split that results in the smallest error
Applying Bisecting K-Means to Geographical Data
Collect Data: Using Yahoo!PlaceFinder API to collect data
Prepare Data: Retain only latitude and longitude information
Analyze Data: Use Matplotlib to build a two-dimensional data map containing clusters and maps
Train Algorithm: Training is not applicable to unsupervised learning
Test Algorithm: Use the biKmeans() function
Use Algorithm: The final output is a map containing clusters and cluster centers
Relevant Formulas


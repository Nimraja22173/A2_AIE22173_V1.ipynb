#2)Write a function to implement k-NN classifier. k is a variable and based on that the count of neighbors should be selected.
from collections import Counter

def euclidean_distance(vector1, vector2):
    return sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)) ** 0.5

def k_nearest_neighbors(training_data, test_instance, k=3):
    distances = [(euclidean_distance(test_instance, training_instance[0]), training_instance[1]) for training_instance in training_data]
    sorted_distances = sorted(distances, key=lambda x: x[0])
    k_nearest_labels = [label for _, label in sorted_distances[:k]]
    most_common_label = Counter(k_nearest_labels).most_common(1)[0][0]
    return most_common_label

def main():
    # User input for training data
    training_data = []
    num_train_instances = int(input("Enter the number of training instances: "))

    for _ in range(num_train_instances):
        features = [float(x) for x in input("Enter features (comma-separated values): ").split(',')]
        label = input("Enter the label for this instance: ")
        training_data.append((features, label))

    # User input for test instance
    test_instance = [float(x) for x in input("Enter test instance features (comma-separated values): ").split(',')]

    # User input for k
    k_value = int(input("Enter the value of k:"))

    # Perform k-NN classification
    predicted_label = k_nearest_neighbors(training_data, test_instance, k=k_value)

    # Print the result
    print(f"The predicted label for the test instance is: {predicted_label}")

if __name__ == "__main__":
    main()

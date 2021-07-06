from project.datasets import Simple, Split, Xor

N = 100


def simple_classifier(x):
    "Classify with simple decision boundary based on position of x_0."

    return 1.0 if x[0] > 0.5 else 0.0




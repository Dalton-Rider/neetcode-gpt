class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        alpha = learning_rate
        for i in range(iterations):
           derivative = 2 * x
           x_new = x - alpha * derivative
           x = x_new
        return round(x, 5)


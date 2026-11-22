class Solution:
  def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    # Objective function: f(x) = x^2 where x is weight and x^2 is loss
    # Derivative:         f'(x) = 2x the slope
    # Update rule:        x = x - learning_rate * f'(x)
    # Round final answer to 5 decimal places
    # if iterations == 0: return init
    
    x = init

    for _ in range(iterations):
      x -= learning_rate  * 2 * x
    
    return round(x, 5)

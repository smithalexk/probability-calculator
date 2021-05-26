import copy
import random
# Consider using the modules imported above.

class Hat(object):
    def __init__(self, **kwargs):
        self.contents = kwargs
    
    @property
    def contents(self):
        return self._contents
    
    @contents.setter
    def contents(self, in_dict):
        if not isinstance(in_dict, dict):
            raise TypeError("Variable is not dictionary")
        self._contents = [key for key in in_dict.keys() for _ in range(in_dict[key])]
    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            o_ball = copy.copy(self.contents)
            self.contents.clear()
            return o_ball

        o_ball = []
        for _ in range(num_balls):
            r_idx = random.randint(0,len(self.contents)-1)
            d_ball = self.contents[r_idx]
            o_ball.append(d_ball)
            self.contents.remove(d_ball)

        return o_ball
    
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
    prob = 0
    for _ in range(num_experiments):
        exp_balls = [key for key in expected_balls.keys() for _ in range(expected_balls[key])]
        temp_hat = copy.deepcopy(hat)

        o_exp = temp_hat.draw(num_balls_drawn)
        
        for bb in exp_balls:
            if bb not in o_exp:
                break
            
            o_exp.remove(bb)
            
        else:
            prob += 1

    
    return prob / num_experiments

        
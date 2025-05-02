import random
import numpy as np
class DQN:
    def __init__(self, input_dims, hidden_dims, output_dims, gamma, learning_rate):
        self.input_dims = input_dims
        self.hidden_dims = hidden_dims
        self.output_dims = output_dims
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.neural_network = {}
        self.target_network = {}
        self.neural_network['W1'] = np.random.rand(self.input_dims, self.hidden_dims) - 0.5
        self.neural_network["w2"] = np.random.rand(self.hidden_dims, self.output_dims) - 0.5
        self.neural_network["b1"] = np.random.rand(1, self.hidden_dims) - 0.5
        self.neural_network["b2"] = np.random.rand(1, self.output_dims) - 0.5
        self.target_network = self.neural_network.copy()
    
    def forward_prop(self, states):
        w1 = self.neural_network["W1"]
        w2 = self.neural_network["w2"]
        b1 = self.neural_network["b1"]
        b2 = self.neural_network["b2"]
        
        X = np.array(states, dtype=np.float32)
        if X.ndim == 1:
            X = X.reshape(1, -1)

        Z1 = np.dot(X, w1) + b1
        A1 = self.Relu(Z1)
        Z2 = np.dot(A1, w2) + b2
        A2 = Z2  # No softmax — raw Q-values

        return Z1, A1, Z2, A2


    def softmax(self, x):
        x_max = np.max(x)
        exp_x = np.exp(x - x_max)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def Relu(self, x):
        return np.maximum(0, x)

    def get_action(self, state):
    # Exploration vs Exploitation
        if random.random() < self.epsilon:
            action = random.randint(0, 4)  
        else:
            action = self.dqn.make_predictions(state)  # Best action (exploitation)
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

        return action
    
    def make_predictions(self, X): 
        _, _, _, A2 = self.forward_prop(X)
        action = np.argmax(A2, axis=1)[0]  # Highest Q-value
        return action
    
    def get_probs(self, X): 
        _, _, _, A2 = self.forward_prop(X)
        return A2
    
    def back_prop(self, Z1, A1, Z2, state_old, pred, target):
        dZ2 = (target - pred)
        dZ2 = np.expand_dims(dZ2, axis=0)  
        dW2 = A1.T.dot(dZ2)
        dB2 = np.sum(dZ2)
        dZ1 = dZ2.dot(self.neural_network['w2'].T) * self.relu_derivative(Z1)
        dW1 = state_old.T.dot(dZ1)
        dB1 = np.sum(dZ1)
        return dW1, dW2, dB1, dB2
    

    def update_gradients(self, dW1, dW2, dB1, dB2, lr): 
        max_grad_norm = 1.0
        dW1 = np.clip(dW1, -max_grad_norm, max_grad_norm)
        dW2 = np.clip(dW2, -max_grad_norm, max_grad_norm)
        dB1 = np.clip(dB1, -max_grad_norm, max_grad_norm)
        dB2 = np.clip(dB2, -max_grad_norm, max_grad_norm)
        self.neural_network['W1'] -= dW1*lr
        self.neural_network["w2"] -= dW2*lr
        self.neural_network["b1"] -= dB1*lr
        self.neural_network["b2"] -= dB2*lr
        
    def relu_derivative(self, x):
        return (x > 0).astype(float)

        



    def softmax_derivative(self, z):
        s = self.softmax(z).reshape(-1, 1)  # column vector
        return np.diagflat(s) - np.dot(s, s.T)





        

    
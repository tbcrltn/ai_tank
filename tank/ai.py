import numpy as np
import random
from collections import deque
from dqn import DQN
MAX_MEMORY = 500_000
BATCH_SIZE = 100

class AI:
    def __init__(self, player, bullet, walls, computer):
        self.player = player
        self.bullet = bullet
        self.walls = walls
        self.computer = computer
        self.epsilon = 1.0
        self.epsilon_min = 0.1  # Minimum epsilon value
        self.epsilon_decay = 0.9999# Decay rate
        self.n_games = 0
        self.dqn = DQN(input_dims=6, hidden_dims=128, output_dims=5, gamma=.94, learning_rate=0.0001)
        self.memory = deque(maxlen=MAX_MEMORY)
        self.collision_counter = 0


    def bullet_position(self):
        closest_bullet = None
        min_dist = float('inf')

        for bullet in self.bullet.bullets:
            x = bullet.x
            y = bullet.y
            enemyx = self.computer.enemy.x
            enemyy = self.computer.enemy.y
            dist = np.linalg.norm([enemyx - x, enemyy - y])
            
            if dist < min_dist:
                min_dist = dist
                closest_bullet = bullet

        if closest_bullet:
            return closest_bullet.x, closest_bullet.y
        else:
            return 0, 0
    
    def player_pos(self):
        return self.player.player.x, self.player.player.y
    
    def enemy_pos(self): 
        return self.computer.enemy.x, self.computer.enemy.y
    def remember(self, state, action_index, reward, next_state, done):
        self.memory.append((state, action_index, reward, next_state, done))
    
    
    def get_states(self):
        states = []
        width, height = 1280, 720
        states.append(self.player_pos()[0]/width)
        states.append(self.player_pos()[1]/height)
        states.append(self.bullet_position()[0]/width)
        states.append(self.bullet_position()[1]/height)
        #print(self.bullet_position()[0], self.bullet_position()[1])
        states.append(self.enemy_pos()[0]/width)
        states.append(self.enemy_pos()[1]/height)
        normalized_list = [x / 500 for x in states]
        return normalized_list
    
    def get_action(self, state):
    # Epsilon-greedy strategy
        if random.random() < self.epsilon:
            action = random.randint(0, 4)  # Integer action
        else:
            action = self.dqn.make_predictions(state)  # Should return an integer

        # Decay epsilon
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

        return action  # Return just the index, not a one-hot list

    
    def get_prob_distrbution(self, state): 
        move = self.dqn.get_probs(state)
        return move
    
    def get_collision_reward(self, collision):
        if collision:
            self.collision_counter+=1
            return -0.2
        else:
            self.collision_counter = 0
            return 0.1
    
    def get_damage_reward(self, damage): 
        if damage: 
            return 0
        else: 
            return 0
        
    def get_player_dist_reward(self):
        enemy = np.array(self.enemy_pos())
        player = np.array(self.player_pos())
        dist = np.linalg.norm(enemy - player)
        return 0#-dist / 1000

    
    def get_reward(self, collision, damage): 
        reward = self.get_collision_reward(collision)
        reward += self.get_damage_reward(damage)
        reward += self.get_player_dist_reward()
        reward -= 0.1
        reward = max(min(reward, 10), -10)

        #print(reward)
        return reward
    
    def train_short_term(self, state_old, action_index, reward, new_state, done):
        state_old = np.array(state_old, dtype=np.float32).reshape(1, -1)
        new_state = np.array(new_state, dtype=np.float32).reshape(1, -1)

        Z1, A1, Z2, pred = self.dqn.forward_prop(state_old)
        pred = pred.flatten()
        target = pred.copy()

        # Predict Q-values for next state
        _, _, _, next_pred = self.dqn.forward_prop(new_state)
        next_pred = next_pred.flatten()

        Q_new = reward if done else reward + self.dqn.gamma * np.max(next_pred)
        target[action_index] = Q_new

        dW1, dW2, dB1, dB2 = self.dqn.back_prop(Z1, A1, Z2, state_old, pred, target)
        self.dqn.update_gradients(dW1, dW2, dB1, dB2, self.dqn.learning_rate)


    def train_long_term_memory(self):
        if not len(self.memory) < BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)

            for state, action_index, reward, next_state, done in mini_sample:
                state = np.array(state, dtype=np.float32).reshape(1, -1)
                next_state = np.array(next_state, dtype=np.float32).reshape(1, -1)

                Z1, A1, Z2, pred = self.dqn.forward_prop(state)
                pred = pred.flatten()
                target = pred.copy()

                _, _, _, next_pred = self.dqn.forward_prop(next_state)
                next_pred = next_pred.flatten()
                

                Q_new = reward if done else reward + self.dqn.gamma * np.max(next_pred)
                target[action_index] = Q_new

                print(f"[Short-term] Pred before training: {pred}")
                print(f"[Short-term] Target: {target}")

                dW1, dW2, dB1, dB2 = self.dqn.back_prop(Z1, A1, Z2, state, pred, target)
                self.dqn.update_gradients(dW1, dW2, dB1, dB2, self.dqn.learning_rate)
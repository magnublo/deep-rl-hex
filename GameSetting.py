import yaml
from definitions import ROOT_DIR, DATA_DIR
from datetime import datetime
import random
import string
import time
import tensorflow as tf


class GameSetting:
    def __init__(self):
        configfile = yaml.load(open(ROOT_DIR+"WhichSetting.yaml"))
        game_config = yaml.load(open(ROOT_DIR+configfile["filename"]))
        neural_net_config = yaml.load(open(ROOT_DIR+"NeuralNetSetting.yaml"))
        self.G = game_config["G"]
        self.P = game_config["P"]
        self.M = game_config["M"]
        self.verbose = game_config["verbose"]
        self.size = game_config["size"]
        self.activation_function = neural_net_config['activation_function']
        self.hidden_function = neural_net_config['hidden_function']
        self.output_function = neural_net_config['output_function']
        self.network_dimensions = self.read_network_dimensions(neural_net_config['hidden_layers'])
        self.optimizer = neural_net_config['optimizer']
        self.loss_function = neural_net_config['loss_function']
        self.metrics = eval("tf.keras.metrics."+neural_net_config['metrics'])
        self.epochs = int(neural_net_config['epochs'])
        self.learning_rate = float(neural_net_config['learning_rate'])
        self.epsilon = float(neural_net_config['epsilon'])

    def read_network_dimensions(self, hidden_layer_dims):

        network_dimensions = [self.size**2]

        if type(hidden_layer_dims) == int:
            network_dimensions.append(hidden_layer_dims)
        elif (hidden_layer_dims is ""):
            network_dimensions.append(self.default_hidden_layer_dims(hidden_layer_dims))
        elif type(hidden_layer_dims) != int:
            for i in str.split(hidden_layer_dims,","):
                i = int(i)
                if i >0:
                    network_dimensions.append(i)
                else:
                    network_dimensions.append(self.size**2)

        network_dimensions.append(self.size**2)
        return network_dimensions

    def default_hidden_layer_dims(self, hidden_layer_dims):
        #Here we need to hardcode an appropriate hidden layer configuration which works as default
        #if no hidden layer dimensions are defined in the configuration.
        pass
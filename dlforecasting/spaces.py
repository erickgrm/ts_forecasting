

arma_space = {
    'p': hp.choice('p', list(range(0, 10, 1))),
    'q': hp.choice('q', list(range(0, 10, 1)))
    }

arima_space = {
    'p': hp.choice('p', list(range(0, 10, 1))),
    'd': hp.choice('d', [0,1,2])
    'q': hp.choice('q', list(range(0, 10, 1)))
    }

exp_space = {
    'smoothing_level': hp.uniform('smoothing_level', 0.0, 1.0),
    'optimized': hp.choice('optimized', [False])
    }

holt_space = {
    'smoothing_level': hp.uniform('smoothing_level', 0.0, 1.0),
    'smoothing_slope': hp.uniform('smoothing_slope', 0.0, 1.0),
    'optimized': hp.choice('optimized', [False])
    }

damped_holt_space = {
    'smoothing_level': hp.uniform('smoothing_level', 0.0, 1.0),
    'smoothing_slope': hp.uniform('smoothing_slope', 0.0, 1.0),
    'damping_slope': hp.uniform('damping_slope', 0.001, 0.999),
    'optimized': hp.choice('optimized', [False])
    }

perceptron_space = {
    'hidden_neurons_1': hp.choice('hidden_neurons_1', list(range(1, 100, 3))),
    'hidden_neurons_2': hp.choice('hidden_neurons_2', list(range(1, 50, 2))), 
    'activation_1': hp.choice('activation_1', ['relu', 'linear', 'sigmoid']),
    'activation_2': hp.choice('activation_2', ['relu', 'linear', 'sigmoid'])
    }

rnn_space = {
    'window_size': hp.choice('window_size', list(range(5, 60, 5), 
    'rnn_layers': hp.choice('rnn_layers', [2,3]),
    'units_rnn_1': hp.choice('units_rnn_1', list(range(30, 100, 10))),
    'units_rnn_2': hp.choice('units_rnn_2', list(range(30, 100, 10))),
    'units_rnn_3': hp.choice('units_rnn_3', list(range(30, 100, 10))),
    'last_dense': hp.choice('last_dense', [True, False])
    }

lstm_space = {
    'window_size': hp.choice('window_size', list(range(5, 60, 5), 
    'lstm_layers': hp.choice('lstm_layers', [2,3]),
    'units_lstm_1': hp.choice('units_lstm_1', list(range(30, 100, 10))),
    'units_lstm_2': hp.choice('units_lstm_2', list(range(30, 100, 10))),
    'units_lstm_3': hp.choice('units_lstm_3', list(range(30, 100, 10))),
    'last_dense': hp.choice('last_dense', [True, False])
    }

attentionlstm_space = {
    'window_size': hp.choice('window_size', list(range(5, 60, 5), 
    'lstm_layers': hp.choice('lstm_layers', [2,3]),
    'units_lstm_1': hp.choice('units_lstm_1', list(range(30, 100, 10))),
    'units_lstm_2': hp.choice('units_lstm_2', list(range(30, 100, 10))),
    'units_lstm_3': hp.choice('units_lstm_3', list(range(30, 100, 10))),
    'last_dense': hp.choice('last_dense', [True, False])
        }

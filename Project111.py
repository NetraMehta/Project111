from random import random
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

population_mean = statistics.mean(data)
print('Population mean:', population_mean)

population_std_dev = statistics.stdev(data)

def random_set_of_means(counter):
    data_set = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

sample_mean = statistics.mean(mean_list)
sample_std_dev = statistics.stdev(mean_list)

print('Sample mean:', sample_mean)
print('Sample standard deviation:', sample_std_dev)

first_std_deviation_start, first_std_deviation_end = sample_mean - sample_std_dev, sample_mean + sample_std_dev
second_std_deviation_start, second_std_deviation_end = sample_mean - (2*sample_std_dev), sample_mean + (2*sample_std_dev)
third_std_deviation_start, third_std_deviation_end = sample_mean - (3*sample_std_dev), sample_mean + (3*sample_std_dev)

fig = ff.create_distplot([mean_list], ['Reading time'], show_hist = False)
fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 1.4], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 1'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 1'))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 2'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 2'))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 3'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 3'))
fig.show()

df2 = pd.read_csv('sample_2.csv')
data2 = df['reading_time'].tolist()

sample2_mean = statistics.mean(data2)
print('Sample 2 mean:', sample2_mean)

fig = ff.create_distplot([mean_list], ['Reading time'], show_hist = False)
fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 1.4], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [sample2_mean, sample2_mean], y = [0, 1.4], mode = 'lines', name = 'Mean of sample 2'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 1'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 1.4], mode = 'lines', name = 'Standard deviation 2'))
fig.show()

z_score = (sample2_mean - sample_mean)/sample_std_dev
print(z_score)
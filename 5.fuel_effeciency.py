import numpy as np
fuel_efficiency = np.array([25, 30, 22, 28, 20, 35, 27])
average_efficiency = np.mean(fuel_efficiency)
model1_efficiency = fuel_efficiency[0] 
model2_efficiency = fuel_efficiency[2] 
percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100
print("Average fuel efficiency:", average_efficiency, "mpg")
print("Percentage improvement between two car models:", percentage_improvement, "%")

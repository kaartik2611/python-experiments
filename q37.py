import matplotlib.pyplot as plt

mi_scores = {
    '1'  : 8, 
    '2'  : 12, 
    '3'  : 10 , 
    '4'  : 7, 
    '5'  : 7, 
    '6'  : 9, 
    '7'  : 5, 
    '8'  : 10, 
    '9'  : 8, 
    '10' : 10,
    '11' : 9, 
    '12' : 8, 
    '13' : 7, 
    '14' : 7, 
    '15' : 11, 
    '16' : 12, 
    '17' : 12, 
    '18' : 15, 
    '19' : 12, 
    '20' : 13, 
}
plt.scatter(mi_scores.keys(),mi_scores.values())
plt.xlabel('Overs')
plt.ylabel('Runs Per Over')
plt.title('Runs scored by Mumbai Indians in 2020 IPL Final')
plt.show()

print(f'Average Run Rate: {sum(mi_scores.values())/20}')

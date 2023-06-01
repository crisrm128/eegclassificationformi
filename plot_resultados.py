import pickle
import matplotlib.pyplot as plt

# Cargar el objeto history desde el primer archivo
with open('./historial-TCNET/history_crossval_alltrials_default_1.pkl', 'rb') as file:
    history_1 = pickle.load(file)

# Cargar el objeto history desde el segundo archivo
with open('./historial-ATCNET/history_crossval_alltrials_default_1.pkl', 'rb') as file:
    history_2 = pickle.load(file)

# Plot de accuracy
plt.plot(history_1['accuracy'])
#plt.plot(history_1['val_accuracy'])
plt.plot(history_2['accuracy'])
#plt.plot(history_2['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train EEG-TCNet','Train EEG-ATCNet'], loc='lower right')
plt.savefig('./Plots/crossval_alltrials_default_accuracy.png')  # Guardar la gráfica en un archivo PNG
plt.show()

# Plot de loss
plt.plot(history_1['loss'])
#plt.plot(history_1['val_loss'])
plt.plot(history_2['loss'])
#plt.plot(history_2['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train EEG-TCNet', 'Train EEG-ATCNet'], loc='upper right')
plt.savefig('./Plots/crossval_alltrials_default_loss.png')  # Guardar la gráfica en un archivo PNG
plt.show()

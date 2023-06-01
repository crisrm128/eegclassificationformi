# Técnicas de aprendizaje profundo para la clasificación de señales EEG de imaginación motora

Este repositorio colecciona los diferentes programas y códigos que han sido estudiados como parte de la literatura y desarrollados para mejorar los sistemas de clasificación de señales EEG de imaginación motora.

Este proyecto es el resultado del Trabajo de Fin de Grado desarrollado por mí (Cristina Romero Mirete) durante el cuarto curso del Grado en Ingeniería Robótica de la Universidad de Alicante.

## Estructura de carpetas y ficheros

Todas las arquitecturas utilizan el conjunto de datos ['BCI Competition IV 2a'](https://www.bbci.de/competition/iv/#datasets).

- **EstadoArte**. En ella se recogen las metodologías adaptadas para _Google Colab_ de los siguientes trabajos: 
  - **ARL-Models**. Recoge las arquitecturas de EEGNet, DeepConvNet y ShallowConvNet. [Enlace al trabajo](https://github.com/vlawhern/arl-eegmodels). 
  - **CNN-2D-EdgarMoyete**. Se implementa el trabajo ['EEG Classification with CNN'](https://github.com/EdgarMoyete/EEG-Classification-with-CNN). Se ha generado adicionalmente el fichero _Etiquetas.m_ para poder 
  - **ML-DL-JamesMcIntyre**. Se prueba el trabajo ['Machine Learning and Deep Learning for Motor Imagery Classification using Electroencephalography '](https://github.com/James-Mc1ntyre/DeepLearningProject). El modelo de _Machine Learning_ no se ha podido ejecutar por el elevado tiempo de ejecución para la extracción de características.
  - **MMCNN-ECML-PKDD**. Ejecución del modelo desarrollado en el trabajo [MMCNN: A Multi-branch Multi-scale Convolutional Neural Network for Motor Imagery Classification](https://github.com/ziyujia/ECML-PKDD_MMCNN).
  - **MOABB**. Pruebas y desarrollo de _benchmarks_ a partir del trabajo [Mother of all BCI Benchmarks](https://github.com/NeuroTechX/moabb).

- **EEG-TCNet**. [Trabajo original](https://github.com/iis-eth-zurich/eeg-tcnet) añadiendo la posibilidad de entrenamiento con el conjunto de entrenamiento completo, preprocesamiento de las señales EEG y validación cruzada _k-fold_ y de una sola división.

- **EEG-ATCNet**. [Trabajo original](https://github.com/Altaheri/EEG-ATCNet) añadiendo la posibilidad de entrenamiento con el conjunto de entrenamiento completo, preprocesamiento de las señales EEG y validación cruzada _k-fold_ y de una sola división.

- **ssl-for-mi**. Adaptación del modelo de aprendizaje autosupervisado del trabajo [ssl-for-mi](https://github.com/nutapol97/ssl-for-mi) para el conjunto de datos mencionado y extracción de los vectores de características correspondientes.

- **plot_resultados.py**. Este archivo permite generar gráficas a partir de los ficheros '.pkl' generados en los modelos de EEG-TCNet y EEG-ATCNet.

## Anotaciones

El motivo por el cual los _commits_ son tan recientes entre sí es debido a que, como se trabajó en _Google Colab_, la gestión de versiones se realizó en _Google Drive_.

Para poder probar este repositorio, es necesario descargarlo y subirlo al almacenamiento de _Google Drive_, dentro de una carpeta llamada 'TFG', para que no haya problema a la hora de la lectura de ficheros.

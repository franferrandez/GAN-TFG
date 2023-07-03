# GAN-TFG
Este repositorio contiene los scripts en Python y Jupiter Notebooks que he utilizado para desarrollar mi TFG para la [Universidad de Alicante](https://ua.es).


## Contexto
Brevemente, el trabajo consiste en realizar un estudio cronológico a través de las GANs (Generative Adversarial Netowrks) que han surgido con el paso de los años. La finalidad es comparar una arquitectura temprana frente a otra más antigua para determinar si verdaderamente ha habido una evolución en el campo de la generación de imágenes.

A grandes rasgos, una GAN está compuesta por dos redes neuronales. Una generativa (G), encargada de crear imágenes falsas y otra discriminadora (D) que tratará de detectarlas. Siguiendo esta lógica se sumergerán en un entrenamiento donde cada una de ellas compatirá por ser mejor que la otra logrando así resultados increíbles.


## Estructura
El repositorio consta de dos carpetas principales:

- La primera contiene el código que he necesitado para poner en marcha la [DCGAN](https://arxiv.org/abs/1511.06434) donde he utilizado como referencia la documentación de PyTorch [DCGAN Tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html#introduction).

- La segunda contiene el código de [Alias-Free GAN](https://arxiv.org/abs/2106.12423), en este caso está extraído de su [repositorio](https://github.com/NVlabs/stylegan3) y contiene un scipt python que ejecuta su contenido para generar imágenes de forma automática.


## Ejecución

El código de la DCGAN es un documento Google Colaboratory donde lo único que necesitamos para poder ejecutarlo es descargar el dataset de [CelebA](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) Align&Cropped Images y extraer el zip dentro de una carpeta llamada data/. Las imágenes deberán estar en data/img_align_celeba/.

El código de StyleGAN3 contiene un script en Python llamado runner.py que genera una tanda de imágenes, las que hemos utilizado para el estudio.


## Dependencias
  - DCGAN: Python3 y CUDA 11.8
  - StyleGAN3: En nuestro caso hemos necesitado GCC, Docker, CUDA toolkit container y CONDA porque hemos generado las imágenes mediante Docker, pero a continuación tenemos su [documentación](https://github.com/franferrandez/GAN-TFG/tree/master/stylegan3#readme).

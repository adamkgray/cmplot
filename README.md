# CM Plot

Visualise a confusion matrix like the main image on Wikipedia 'Sensitivity and specificty' page.

## About

Recently while reviewing metrics related to precision and recall, I came across this image on Wikipedia:

<img src="/Sensitivity_and_specificity_1.01.png" width="50%" height="50%">

The idea is that you can roughly show the performance of a classification task while also getting a sense of precision and recall at the same time.

I had been training some binomial classification models and thought it'd be nice to try visualising them like this. My interest was piqued when I found there is no existing tool for it! So I had no choice but to write a lib to do it myself.

After some tooling, I was able to make matplotlib make something like this:

<img src="/plot.png" width="50%" height="50%">
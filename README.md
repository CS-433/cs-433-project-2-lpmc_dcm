# Machine Learning: Project 2

  

_This is the README file for the project 2 of the ML course (CS-433) we did in collaboration with EPFL Transport and Mobility Laboratory._

* Subject:
  * Regularized maximum likelihood estimation for discrete choice models.

* Names:
  * Thomas Benchetrit: <thomas.benchetrit@epfl.ch>
  * Romain Palazzo: <romain.palazzo@epfl.ch>
  * Eliott Zemour: <eliott.zemour@epfl.ch>

* Supervisors (EPFL TRANSP-OR lab):
  * Nicola Ortelli
  * Michel Bierlaire

  

The dataset used is London Passenger Mode Choice (LPMC) revealed-preference data. A description of the features can be found [here](https://transp-or.epfl.ch/documents/technicalReports/CS_LPMC.pdf).

Full details of the framework, dataset, and the models it was used to develop are given in Hillel et al. (2018): [https://doi.org/10.1680/jsmic.17.00018](https://doi.org/10.1680/jsmic.17.00018).
  
##
#### Pylogit package:

The code for this project is based on Python [pylogit](https://github.com/timothyb0912/pylogit) package by [Timothy Brathwaite](https://github.com/timothyb0912).

This package is designed for "_performing maximum likelihood estimation of conditional logit models and similar discrete choice models_".

#### Contributions to the initial code:

As part of this project, we implemented Ridge and LASSO regularization methods, as well as Box-Cox tranformations.

* Regularization methods:
  * added file `reg.py: L1() and L2()` methods.

  * modified files:
    * `choice_calcs.py`: `calc_probabilities(), [lines 144-189], calc_log_likelihood() [lines 349-364] and calc_gradient()[lines 472-615]`: The gradient for a $\lambda$ parameter is given by : A remplir. Entre crochet les lignes de modifications de chaque methode
    * `conditional_logit.py`: `fit_mle()` function now taking regularization hyperparameters $\lambda_R$ (`ridge`) and $\lambda_L$ (`lasso`) as arguments. These arguments are then passed to any method that needs them.

* Box Cox transform:
  * use of Python [`scipy.special.boxcox()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.boxcox.html)
  * modified files
    * `choice_calcs.py: calc_probabilities(), calc_log_likelihood() and calc_gradient()`: see comment lines.
    * `estimation.py`: `estimate()` now specifies boundaries for boxcox parameters: $\lambda_{cox} \geq 0$. These constraints are then passed to [`scipy.optimize.minimize()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html). The minimization method is also changed from ['BFGS'](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-bfgs.html#optimize-minimize-bfgs) to ['L-BFGS-B'](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html#optimize-minimize-lbfgsb).

  
##
#### How to use

* __Create long format data: `create_large_data.py`__
  This file allows us to convert the original LPMC data to long format, and proceed to segmentation w.r.t gender, age, season, travel purpose.

  

* __Compute the parameter estimates for a given model (specification): `main.py`__
  This file generates a choice model by creating an ordered dictionnary (`collections.OrderedDict`) through the `create_specification.py` file. This dictionnary will determine the functionnal form of the utility functions. Then,  `conditional_logit.fit_mle()` is called to perform the maximum likelihood estimation and returns the final log-likelihood $\mathcal{L}(\hat{\beta})$, as well as the parameters estimates $\hat{\beta}$.

  

* __Perform the grid search over regularization hyperparameters: `grid_search.py`__
  This file perfoms a grid_search over $\lambda_R$ and $\lambda_L$ and stores the following results to be used in  `eval_regularization.py`:
  * The number of parameters $\beta$ pushed towards 0. More precisely those estimated below 1e-6, between 1e-4 and 1e-6, between 1e-2 and 1e-4 and above 1e-2.
  * The array of estimated (regularized) parameters.

  

* __Evaluate the regularization results and compare the hyperparameters combination of the grid search: `eval_regularization.py`__
  This file compares the efficiency of regularization hyperparameters and plots the log-likelihod in terms of the number of added parameters. This is allowed by passing an index list to `fit_mle()` through the argument `keep_ind`.

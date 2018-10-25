# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
AveragedPerceptronBinaryClassifier
"""

__all__ = ["AveragedPerceptronBinaryClassifier"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.linear_model._averagedperceptronbinaryclassifier import \
    AveragedPerceptronBinaryClassifier as core
from ..internal.utils.utils import trace


class AveragedPerceptronBinaryClassifier(
        core, BasePredictor, ClassifierMixin):
    """

    Machine Learning Averaged Perceptron Binary Classifier

    .. remarks::
        Perceptron is a classification algorithm that makes its predictions
        based on a linear function. I.e., for an instance with feature values
        *f0, f1,..., f_D-1*, , the prediction is given by the sign of
        *sigma[0,D-1] ( w_i * f_i)*, where *w_0, w_1,...,w_D-1* are the
        weights
        computed by the algorithm.

        Perceptron is an online algorithm, i.e., it processes the instances
        in
        the training set one at a time. The weights are initialized to be 0,
        or
        some random values. Then, for each example in the training set, the
        value of *sigma[0, D-1] (w_i * f_i)* is computed. If this value has
        the
        same sign as the label of the current example, the weights remain the
        same. If they have opposite signs, the weights vector is updated by
        either subtracting or adding (if the label is negative or positive,
        respectively) the feature vector of the current example, multiplied
        by a
        factor *0 < a <= 1*, called the learning rate. In a generalization of
        this algorithm, the weights are updated by adding the feature vector
        multiplied by the learning rate, and by the gradient of some loss
        function (in the specific case described above, the loss is hinge-
        loss,
        whose gradient is 1 when it is non-zero).

        In Averaged Perceptron (AKA voted-perceptron), the weight vectors are
        stored, together with a weight that counts the number of iterations
        it
        survived (this is equivalent to storing the weight vector after every
        iteration, regardless of whether it was updated or not). The
        prediction
        is then calculated by taking the weighted average of all the sums
        *sigma[0, D-1] (w_i * f_i)* or the different weight vectors.


        **Reference**

            `Wikipedia entry for Perceptron
            <https://en.wikipedia.org/wiki/Perceptron>`_

            `Large Margin Classification Using the Perceptron Algorithm
            <http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.48.8200>`_

            `Discriminative Training Methods for Hidden Markov Models
            <http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.18.6725>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param loss: The default is :py:class:`'hinge' <nimbusml.loss.Hinge>`. Other
        choices are :py:class:`'exp' <nimbusml.loss.Exp>`, :py:class:`'log'
        <nimbusml.loss.Log>`, and :py:class:`'smoothed_hinge'
        <nimbusml.loss.SmoothedHinge>`. For more information, please see the
        documentation page about losses, [Loss](xref:nimbusml.loss).

    :param learning_rate: Learning rate.

    :param decrease_learning_rate: Decrease learning rate.

    :param l2_regularizer_weight: L2 Regularization Weight.

    :param num_iterations: Number of iterations.

    :param init_wts_diameter: Sets the initial weights diameter that specifies
        the range from which values are drawn for the initial weights. These
        weights are initialized randomly from within this range. For example,
        if the diameter is specified to be ``d``, then the weights are
        uniformly distributed between ``-d/2`` and ``d/2``. The default value
        is ``0``, which specifies that all the  weights are set to zero.

    :param reset_weights_after_x_examples: Number of examples after which
        weights will be reset to the current average.

    :param do_lazy_updates: Instead of updating averaged weights on every
        example, only update when loss is nonzero.

    :param recency_gain: Extra weight given to more recent updates.

    :param recency_gain_multi: Whether Recency Gain is multiplicative (vs.
        additive).

    :param averaged: Do averaging?.

    :param averaged_tolerance: The inexactness tolerance for averaging.

    :param initial_weights: Initial Weights and bias, comma-separated.

    :param shuffle: Whether to shuffle for each training iteration.

    :param streaming_cache_size: Size of cache when trained in Scope.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`LogisticRegressionClassifier
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        `Types </nimbusml/concepts/types#column-types>`_

    .. index:: models, classification, perceptron

    Example:
       .. literalinclude:: /../nimbusml/examples/AveragedPerceptronBinaryClassifier.py
               :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            loss='hinge',
            learning_rate=1.0,
            decrease_learning_rate=False,
            l2_regularizer_weight=0.0,
            num_iterations=1,
            init_wts_diameter=0.0,
            reset_weights_after_x_examples=None,
            do_lazy_updates=True,
            recency_gain=0.0,
            recency_gain_multi=False,
            averaged=True,
            averaged_tolerance=0.01,
            initial_weights=None,
            shuffle=True,
            streaming_cache_size=1000000,
            feature=None,
            label=None,
            **params):

        if 'feature_column' in params:
            raise NameError(
                "'feature_column' must be renamed to 'feature'")
        if feature:
            params['feature_column'] = feature
        if 'label_column' in params:
            raise NameError(
                "'label_column' must be renamed to 'label'")
        if label:
            params['label_column'] = label
        BasePredictor.__init__(self, type='classifier', **params)
        core.__init__(
            self,
            normalize=normalize,
            caching=caching,
            loss=loss,
            learning_rate=learning_rate,
            decrease_learning_rate=decrease_learning_rate,
            l2_regularizer_weight=l2_regularizer_weight,
            num_iterations=num_iterations,
            init_wts_diameter=init_wts_diameter,
            reset_weights_after_x_examples=reset_weights_after_x_examples,
            do_lazy_updates=do_lazy_updates,
            recency_gain=recency_gain,
            recency_gain_multi=recency_gain_multi,
            averaged=averaged,
            averaged_tolerance=averaged_tolerance,
            initial_weights=initial_weights,
            shuffle=shuffle,
            streaming_cache_size=streaming_cache_size,
            **params)
        self.feature = feature
        self.label = label

    @trace
    def predict_proba(self, X, **params):
        '''
        Returns probabilities
        '''
        return self._predict_proba(X, **params)

    @trace
    def decision_function(self, X, **params):
        '''
        Returns score values
        '''
        return self._decision_function(X, **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)

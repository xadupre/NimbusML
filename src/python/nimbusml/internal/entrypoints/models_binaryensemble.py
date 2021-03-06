# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Models.BinaryEnsemble
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def models_binaryensemble(
        models,
        predictor_model=None,
        model_combiner='Median',
        validate_pipelines=True,
        **params):
    """
    **Description**
        Combine binary classifiers into an ensemble

    :param models: The models to combine into an ensemble (inputs).
    :param model_combiner: The combiner used to combine the scores
        (inputs).
    :param validate_pipelines: Whether to validate that all the
        pipelines are identical (inputs).
    :param predictor_model: The trained model (outputs).
    """

    entrypoint_name = 'Models.BinaryEnsemble'
    inputs = {}
    outputs = {}

    if models is not None:
        inputs['Models'] = try_set(
            obj=models,
            none_acceptable=False,
            is_of_type=list)
    if model_combiner is not None:
        inputs['ModelCombiner'] = try_set(
            obj=model_combiner,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Median',
                'Average',
                'Vote'])
    if validate_pipelines is not None:
        inputs['ValidatePipelines'] = try_set(
            obj=validate_pipelines, none_acceptable=True, is_of_type=bool)
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint

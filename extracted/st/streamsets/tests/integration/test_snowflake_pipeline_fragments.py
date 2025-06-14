# Copyright 2022 StreamSets Inc.

# fmt: off
import json

import pytest

from streamsets.sdk.utils import SeekableList, get_random_string

# fmt: on

STAGE_NAMES = [
    {'label': 'Snowflake Table', 'type': 'origin'},
    {'label': 'Snowflake SQL Evaluator', 'type': 'processor'},
    {'label': 'Trash', 'type': 'destination'},
    {'label': 'Column Renamer', 'type': 'processor'},
]


@pytest.mark.snowflake
@pytest.mark.parametrize(
    'permutation',
    (
        ['Origins', {'0': ['0']}],
        ['Processors', {'1': ['1']}],
        ['Destinations', {'2': ['2']}],
        ['Origins', {'0': ['1'], '1': ['1']}],
        ['Processors', {'1': ['3'], '3': ['3']}],
        ['Destinations', {'1': ['2'], '2': ['2']}],
        ['Origins', {'0': ['1', '3'], '1': ['1'], '3': ['3']}],
        ['Origins', {'0': ['1+0', '1+1'], '1+0': ['1+0'], '1+1': ['1+1']}],
        ['Destinations', {'0': ['2'], '1': ['2'], '2': ['2']}],
    ),
)
def test_create_fragments(sch, permutation):
    """Each parameter represents a label and fragment graph. The numbers are the indices of the variable STAGE_NAMES.
    e.g. ['Origins', {'0': ['1+0', '1+1'], '1+0': ['1+0'], '1+1': ['1+1']}] represents a fragment:
            'Snowflake Table' >> ['Snowflake SQL Evaluator 0', 'Snowflake SQL Evaluator 1']
    with label 'Origins'
    """
    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake', fragment=True)
    stages = {}
    label, graph = permutation
    for node in graph:
        component = node
        if '+' in node:
            component = node.split('+')[0]
        stages[node] = pipeline_builder.add_stage(**STAGE_NAMES[int(component)])
    for node, neighbors in graph.items():
        if [node] != neighbors:
            stages[node] >> [stages[neighbor] for neighbor in neighbors]
    fragment = pipeline_builder.build('test_sample_pipeline_fragment')
    sch.publish_pipeline(fragment)

    try:
        issues = json.loads(fragment._data['pipelineDefinition'])['issues']
        if issues['issueCount'] == 1:
            assert issues['pipelineIssues'][0]['message'] == 'VALIDATION_0001 - The pipeline is empty'
        else:
            assert json.loads(fragment._data['pipelineDefinition'])['issues']['issueCount'] == 0
        assert json.loads(fragment._data['pipelineDefinition'])['metadata']['labels'][0] == label
    finally:
        sch.delete_pipeline(fragment)


@pytest.mark.snowflake
@pytest.mark.parametrize(
    'permutation',
    (
        ['0', 'Trash'],
        ['Snowflake Table', '2'],
        ['Snowflake Table', '1', 'Trash'],
        ['0_1', 'Trash'],
        ['Snowflake Table', '1_2'],
        ['Snowflake Table', '1_3', 'Trash'],
        ['0', 'Snowflake SQL Evaluator', '2'],
        ['0', '1', 'Trash'],
        ['Snowflake Table', '1', '2'],
        ['0', '1_3', 'Trash'],
        ['0', '1', '2'],
        ['0_1', '2'],
        ['0', '1_3', '2'],
    ),
)
def test_import_fragments_linear_pipelines(sch, permuted_fragments, permutation):
    """Each parameter represents a linear pipeline. The numbers represent fragment names.
    e.g. ['0', '1_3', 'Trash'] represents a pipeline:
            Fragment(name='fragment_from_sdk_0') >> Fragment(name='fragment_from_sdk_1_3') >> 'Trash'.
    """
    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake')
    stages = []
    for component in permutation:
        if component in [s['label'] for s in STAGE_NAMES]:
            stages.append(pipeline_builder.add_stage(**next((s for s in STAGE_NAMES if s['label'] == component))))
        else:
            fragment_name = 'fragment_from_sdk_{}'
            stages.append(pipeline_builder.add_fragment(permuted_fragments.get(name=fragment_name.format(component))))
    for i in range(len(stages) - 1):
        stages[i] >> stages[i + 1]

    pipeline_name = 'test_linear_snowflake_pipeline_using_fragments{}'.format(get_random_string())
    pipeline = pipeline_builder.build(pipeline_name)
    try:
        sch.publish_pipeline(pipeline)
        assert json.loads(pipeline._data['pipelineDefinition'])['issues']['issueCount'] == 0
    finally:
        sch.delete_pipeline(pipeline)


@pytest.mark.snowflake
@pytest.mark.parametrize(
    'permutation',
    (
        {'0': ['Trash+0', 'Trash+1'], 'Trash+0': ['Trash+0'], 'Trash+1': ['Trash+1']},
        {'0': ['1', '3'], '1': ['Trash+0'], '3': ['Trash+1'], 'Trash+0': ['Trash+0'], 'Trash+1': ['Trash+1']},
        {
            '0': ['Snowflake SQL Evaluator', 'Column Renamer'],
            'Snowflake SQL Evaluator': ['Trash+0'],
            'Column Renamer': ['Trash+1'],
            'Trash+0': ['Trash+0'],
            'Trash+1': ['Trash+1'],
        },
        {'0': ['1', '3'], '1': ['Trash'], '3': ['Trash'], 'Trash': ['Trash']},
        {
            '0': ['Snowflake SQL Evaluator', 'Column Renamer'],
            'Snowflake SQL Evaluator': ['Trash'],
            'Column Renamer': ['Trash'],
            'Trash': ['Trash'],
        },
        {'0': ['1', '3'], '1': ['2'], '3': ['2'], '2': ['2']},
        {'0': ['1_3'], '1_3': ['Trash+0', 'Trash+1'], 'Trash+0': ['Trash+0'], 'Trash+1': ['Trash+1']},
        {'0': ['1_3+0', '1_3+1'], '1_3+0': ['2'], '1_3+1': ['2'], '2': ['2']},
    ),
)
def test_import_fragments_non_linear_pipelines(sch, permuted_fragments, permutation):
    """Each parmter represents a non-linear pipeline graph. The numbers represent fragment names.
    e.g. {'0': ['Snowflake SQL Evaluator', 'Column Renamer'],
          'Expression Evaluator': ['Trash+0'],
          'Column Renamer': ['Trash+1'],
          'Trash+0': ['Trash+0'],
          'Trash+1': ['Trash+1']} represents a pipeline:
                Fragment(name='fragment_from_sdk_0') >> ['Expression Evaluator', 'Column Renamer']
                'Snowflake SQL Evaluator' >> 'Trash 0'
                'Column Renamer' >> 'Trash 1'
    """
    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake')
    stages = {}
    for node in permutation:
        component = node
        if '+' in node:
            component = node.split('+')[0]
        if component in [s['label'] for s in STAGE_NAMES]:
            stages[node] = pipeline_builder.add_stage(**next((s for s in STAGE_NAMES if s['label'] == component)))
        else:
            fragment_name = 'fragment_from_sdk_{}'
            stages[node] = pipeline_builder.add_fragment(permuted_fragments.get(name=fragment_name.format(component)))
    for node, neighbors in permutation.items():
        if [node] != neighbors:
            stages[node] >> [stages[neighbor] for neighbor in neighbors]
    pipeline = pipeline_builder.build('test_non_linear_pipeline_using_fragments')
    sch.publish_pipeline(pipeline)

    try:
        assert json.loads(pipeline._data['pipelineDefinition'])['issues']['issueCount'] == 0
    finally:
        sch.delete_pipeline(pipeline)


@pytest.mark.snowflake
def test_pipeline_fragment_with_multiple_output_lanes(sch):
    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake', fragment=True)
    dev_data_generator = pipeline_builder.add_stage('Snowflake Table', type='origin')
    expression_evaluator = pipeline_builder.add_stage('Snowflake SQL Evaluator')
    field_renamer = pipeline_builder.add_stage('Column Renamer')
    dev_data_generator >> [expression_evaluator, field_renamer]
    fragment = pipeline_builder.build('fragment_with_multiple_output_lanes')
    sch.publish_pipeline(fragment)

    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake')
    # fragment = sch.pipelines.get(fragment=True, name='Test Fragment')
    fragment_stage = pipeline_builder.add_fragment(fragment)

    trash1 = pipeline_builder.add_stage('Trash')
    trash2 = pipeline_builder.add_stage('Trash')

    fragment_stage >> trash1
    fragment_stage >> trash2

    pipeline = pipeline_builder.build('test_pipeline_to_test_fragment_with_multiple_output_lanes')
    sch.publish_pipeline(pipeline)

    try:
        assert json.loads(pipeline._data['pipelineDefinition'])['issues']['issueCount'] == 0
    finally:
        sch.delete_pipeline(pipeline)
        sch.delete_pipeline(fragment)


@pytest.mark.snowflake
def test_pipeline_fragment_parameter_name_prefix_set_in_ui_info(sch):
    """parameterNamePrefix is set in the uiInfo section of the stage definition."""
    PARAMETER_NAME_PREFIX = 'SOMESILLYTHING'

    fragment_builder = sch.get_pipeline_builder(engine_type='snowflake', fragment=True)
    fragment_builder.add_stage('Snowflake SQL Evaluator')
    fragment = fragment_builder.build('Fragment for parameter name prefix test')
    try:
        sch.publish_pipeline(fragment)

        pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake')
        fragment_stage = pipeline_builder.add_fragment(fragment, parameter_name_prefix=PARAMETER_NAME_PREFIX)
        assert fragment_stage._data['uiInfo']['parameterNamePrefix'] == PARAMETER_NAME_PREFIX
    finally:
        sch.delete_pipeline(fragment)


@pytest.mark.snowflake
def test_update_pipelines_with_different_fragment_version(sch):
    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake', fragment=True)
    pipeline_builder.add_stage('Snowflake Table', type='origin')
    fragment = pipeline_builder.build('fragment to update')
    sch.publish_pipeline(fragment)

    pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake')
    snowflake_table = pipeline_builder.add_fragment(fragment)
    trash = pipeline_builder.add_stage('Trash')
    snowflake_table >> trash
    pipeline = pipeline_builder.build('pipeline using old version of fragment')
    sch.publish_pipeline(pipeline)

    fragment.name = 'updated fragment'
    sch.publish_pipeline(fragment)

    try:
        from_fragment_version = fragment.commits.get(version='1')
        to_fragment_version = fragment.commits.get(version='2')
        assert len(pipeline.commits) == 1
        sch.update_pipelines_with_different_fragment_version(
            pipelines=[pipeline], from_fragment_version=from_fragment_version, to_fragment_version=to_fragment_version
        )
        assert len(pipeline.commits) == 2
    finally:
        sch.delete_pipeline(sch.pipelines.get(pipeline_id=pipeline.pipeline_id))
        sch.delete_pipeline(sch.pipelines.get(pipeline_id=fragment.pipeline_id, fragment=True))


@pytest.fixture(scope='module')
def permuted_fragments(sch):
    # Indices of STAGE_NAMES
    permutations = [[0], [1], [2], [3], [0, 1], [1, 2], [1, 3]]
    fragments = SeekableList()
    for perm in permutations:
        pipeline_builder = sch.get_pipeline_builder(engine_type='snowflake', fragment=True)
        stages = []
        # Add all stages to pipeline builder
        for idx in perm:
            stages.append(pipeline_builder.add_stage(**STAGE_NAMES[idx]))
        # Connect them in a linear way
        for i in range(len(stages) - 1):
            stages[i] >> stages[i + 1]
        fragment = pipeline_builder.build('fragment_from_sdk_{}'.format('_'.join(map(str, perm))))
        sch.publish_pipeline(fragment)
        fragments.append(fragment)

    try:
        yield fragments
    finally:
        for fragment in fragments:
            sch.delete_pipeline(fragment)

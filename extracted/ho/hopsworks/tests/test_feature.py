#
#   Copyright 2022 Hopsworks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#


from hsfs import feature, feature_group


class TestFeature:
    def test_from_response_json(self, backend_fixtures):
        # Arrange
        json = backend_fixtures["feature"]["get"]["response"]

        # Act
        f = feature.Feature.from_response_json(json)

        # Assert
        assert f.name == "intt"
        assert f.type == "int"
        assert f.description == "test_description"
        assert f.primary is True
        assert f.partition is False
        assert f.hudi_precombine_key is True
        assert f.online_type == "int"
        assert f.default_value == "1"  # default value should be specified as string
        assert f._feature_group_id == 15
        assert not f.on_demand

    def test_from_response_json_on_demand(self, backend_fixtures):
        # Arrange
        json = backend_fixtures["feature"]["get_on_demand"]["response"]

        # Act
        f = feature.Feature.from_response_json(json)

        # Assert
        assert f.name == "intt"
        assert f.type == "int"
        assert f.description == "test_description"
        assert f.primary is True
        assert f.partition is False
        assert f.hudi_precombine_key is True
        assert f.online_type == "int"
        assert f.default_value == "1"  # default value should be specified as string
        assert f._feature_group_id == 15
        assert f.on_demand

    def test_from_response_json_basic_info(self, backend_fixtures):
        # Arrange
        json = backend_fixtures["feature"]["get_basic_info"]["response"]

        # Act
        f = feature.Feature.from_response_json(json)

        # Assert
        assert f.name == "intt"
        assert f.type is None
        assert f.description is None
        assert f.primary is False
        assert f.partition is False
        assert f.hudi_precombine_key is False
        assert f.online_type is None
        assert f.default_value is None
        assert f._feature_group_id is None

    def test_like(self):
        # Arrange
        f = feature.Feature("feature_name")

        # Act
        filter_obj = f.like("max%")

        # Assert
        assert filter_obj._feature == f
        assert filter_obj._condition == filter_obj.LK
        assert filter_obj._value == "max%"

    def test_name_sanitizing(self):
        # Arrange
        spaced_name = "col 1"
        upper_name = "Col1"
        both = "Bravo Col"

        # Act
        spaced_feature = feature.Feature(name=spaced_name)
        upper_feature = feature.Feature(name=upper_name)
        both_feature = feature.Feature(name=both)

        # Assert
        assert spaced_feature.name == "col_1"
        assert upper_feature.name == "col1"
        assert both_feature.name == "bravo_col"

    def test_get_fully_qualified_feature_name_without_prefix_and_without_use_fqn(self):
        # Arrange
        f = feature.Feature("feature_name")
        fg = feature_group.FeatureGroup(
            name="test",
            version=1,
            featurestore_id=99,
            primary_key=[],
            partition_key=[],
            id=10,
            event_time="event_time",
            featurestore_name="test_fs",
        )

        # Act
        result = f._get_fully_qualified_feature_name(fg)

        # Assert
        assert result == "feature_name"

    def test_get_fully_qualified_feature_name_with_prefix_and_without_use_fqn(self):
        # Arrange
        f = feature.Feature("feature_name")
        fg = feature_group.FeatureGroup(
            name="test",
            version=1,
            featurestore_id=99,
            primary_key=[],
            partition_key=[],
            id=10,
            event_time="event_time",
            featurestore_name="test_fs",
        )

        # Act
        result = f._get_fully_qualified_feature_name(fg, prefix="prefix_")

        # Assert
        assert result == "prefix_feature_name"

    def test_get_fully_qualified_feature_name_without_prefix_and_with_use_fqn(self):
        # Arrange
        f = feature.Feature("feature_name", use_fully_qualified_name=True)
        fg = feature_group.FeatureGroup(
            name="test",
            version=1,
            featurestore_id=99,
            primary_key=[],
            partition_key=[],
            id=10,
            event_time="event_time",
            featurestore_name="test_fs",
        )

        # Act
        result = f._get_fully_qualified_feature_name(fg)

        # Assert
        assert result == "test_fs_test_1_feature_name"

    def test_get_fully_qualified_feature_name_with_prefix_and_with_use_fqn(self):
        # Arrange
        f = feature.Feature("feature_name", use_fully_qualified_name=True)
        fg = feature_group.FeatureGroup(
            name="test",
            version=1,
            featurestore_id=99,
            primary_key=[],
            partition_key=[],
            id=10,
            event_time="event_time",
            featurestore_name="test_fs",
        )

        # Act
        result = f._get_fully_qualified_feature_name(fg, prefix="prefix_")

        # Assert
        assert result == "test_fs_test_1_feature_name"
